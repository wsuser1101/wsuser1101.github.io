#!/usr/bin/env python3
"""Generate standalone Doxygen Awesome API docs without changing the library checkout."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
API = ROOT / "apidocs"
W4_MODULES = ("apriltag", "cameraserver", "cscore", "datalog", "drivers", "fields",
           "hal", "ntcore", "commandsv2", "telemetry", "tunables", "wpilibc",
           "wpimath", "wpinet", "wpiutil", "romiVendordep", "xrpVendordep")
# VMX-specific interfaces plus the WPILib hardware APIs backed by this port.
VMX_HEADERS = ("MauMap.h", "MauInternal.h", "MauTime.h", "MauClockInternal.h",
               "MauErrors.h", "Translator/include/FileHandler.h",
               "Translator/include/MauEnumConverter.h",
               "DriveStation/include/MauDriveData.h",
               "DriveStation/include/DriverComms.hpp",
               "DriveStation/include/PacketReader.h",
               "DriveStation/include/TcpPacketBuffer.h", "navX/include/AHRS_Mau.h")
VMX_STUDICA_HEADERS = ("TitanQuad.h", "TitanQuadEncoder.h", "Cobra.h", "Servo.h",
                       "ServoContinuous.h", "Lidar.h")
VMX_WPILIB_HEADERS = (
    "DigitalInput.h", "DigitalOutput.h", "DigitalSource.h", "DigitalGlitchFilter.h",
    "AnalogInput.h", "AnalogGyro.h", "AnalogTrigger.h", "AnalogTriggerOutput.h",
    "AnalogTriggerType.h", "Counter.h", "CounterBase.h", "Encoder.h",
    "PWM.h", "Servo.h", "motorcontrol/PWMMotorController.h", "Relay.h",
    "AddressableLED.h", "BuiltInAccelerometer.h", "I2C.h", "SPI.h", "SerialPort.h",
    "AsynchronousInterrupt.h", "SynchronousInterrupt.h", "Notifier.h", "Timer.h",
    "DriverStation.h", "DSControlWord.h", "GenericHID.h", "Joystick.h",
    "RobotController.h", "RobotState.h", "RuntimeType.h", "Threads.h",
    "CAN.h", "PowerDistribution.h", "Compressor.h", "CompressorConfigType.h",
    "Solenoid.h", "DoubleSolenoid.h", "PneumaticsBase.h", "PneumaticsModuleType.h",
    "PneumaticHub.h", "PneumaticsControlModule.h")


def quoted(value):
    return '"' + str(value).replace("\\", "/").replace('"', '\\"') + '"'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", choices=("w4studica", "vmxonwpi"), default="w4studica")
    parser.add_argument("--allwpilib", type=Path, default=ROOT.parent / "allwpilib")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--doxygen", default="doxygen")
    args = parser.parse_args()
    is_vmx = args.project == "vmxonwpi"
    project_api = API / "vmxonwpi" if is_vmx else API
    project_path = "vmxonwpi" if is_vmx else "W4Studica"
    source = args.allwpilib.resolve()
    output = (args.output or ROOT / "site" / project_path / "apidocs").resolve()
    config = json.loads((project_api / "source.json").read_text())
    if subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip() != config["ref"]:
        parser.error("allwpilib HEAD must match the pinned ref in " + str(project_api / "source.json"))
    if output == ROOT or output == source or ROOT.is_relative_to(output) or source.is_relative_to(output):
        parser.error("output must not replace a source checkout or its parent")
    theme = API / "theme"
    provenance = json.loads((theme / "SOURCE.json").read_text())
    for name, expected in provenance["sha256"].items():
        if hashlib.sha256((theme / name).read_bytes()).hexdigest() != expected:
            parser.error("Vendored theme checksum mismatch: " + name)
    inputs = []
    for module in (() if is_vmx else W4_MODULES):
        public = source / module / "src/main/native/include"
        if not public.is_dir():
            parser.error("Missing public header directory: " + str(public))
        inputs.append(public)
        generated = source / module / "src/generated/main/native/include"
        if generated.is_dir():
            inputs.append(generated)
    if not is_vmx:
        inputs += [source / "studica_drivers",
                   source / "simulation/halsim_vmx/src/main/native/include",
                   source / "simulation/halsim_vmx/src/studica/native/include"]
    if any(not path.is_dir() for path in inputs):
        parser.error("Incomplete VMX/Studica public sources")
    if is_vmx:
        backend = source / "hal/src/main/native/mau"
        hal_public = source / "hal/src/main/native/include"
        wpilib_public = source / "wpilibc/src/main/native/include"
        headers = [backend / name for name in VMX_HEADERS]
        headers += [wpilib_public / "frc" / name for name in VMX_WPILIB_HEADERS]
        headers += [wpilib_public / "studica" / name for name in VMX_STUDICA_HEADERS]
        headers += [wpilib_public / "frc/SpeedController.h",
                    wpilib_public / "frc/smartdashboard/SendableBuilder.h"]
        # Match standard HAL declarations to implementations added by this port.
        # Compatibility stubs are included too; the main page lists their limits.
        headers += [hal_public / "hal" / (cpp.stem + ".h")
                    for cpp in sorted(backend.glob("*.cpp"))
                    if (hal_public / "hal" / (cpp.stem + ".h")).is_file()
                    and cpp.stem != "HAL"]
        headers += [hal_public / "hal" / name for name in (
            "HALBase.h", "Types.h", "DriverStationTypes.h", "AddressableLEDTypes.h",
            "CANAPITypes.h", "I2CTypes.h", "SPITypes.h")]
        headers = sorted(set(headers))
        for path in headers:
            if not path.is_file():
                parser.error("Missing VMX interface header: " + str(path))
        inputs = [backend, hal_public, wpilib_public]
    else:
        # Never recurse into Studica's examples or SDK files.
        headers = sorted({p for directory in inputs for pattern in ("*.h", "*.hpp")
                          for p in (directory.glob(pattern) if directory.name == "studica_drivers"
                                    else directory.rglob(pattern))})
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".apidocs-", dir=output.parent) as temporary:
        build = Path(temporary)
        header = build / "header.html"
        subprocess.run([args.doxygen, "-w", "html", str(header), str(build / "footer.html"),
                        str(build / "default.css")], check=True, capture_output=True, text=True)
        extra = [theme / "doxygen-awesome-darkmode-toggle.js", theme / "doxygen-awesome-paragraph-link.js"]
        scripts = '\n'.join('<script src="$relpath^' + file.name + '"></script>' for file in extra)
        scripts += '\n<script>DoxygenAwesomeDarkModeToggle.init(); DoxygenAwesomeParagraphLink.init();</script>\n'
        header.write_text(header.read_text().replace("</head>", scripts + "</head>"))
        replacements = {
            "PROJECT_NAME": quoted("VMX on WPI C++ API" if is_vmx else "W4Studica C++ API"),
            "PROJECT_BRIEF": quoted("WPILib hardware APIs with VMX implementations · VMX extensions" if is_vmx else "WPILib · Studica Drivers · VMX"),
            "VERSION": quoted(config["version"]), "BUILD_DIRECTORY": quoted(build),
            "INPUT": " ".join(quoted(p) for p in headers + [project_api / "mainpage.md"]),
            "STRIP_PATHS": " ".join(quoted(p) for p in inputs + [source, API]),
            "MAINPAGE": quoted(project_api / "mainpage.md"), "HEADER": quoted(header),
            "STYLESHEETS": " ".join(quoted(p) for p in [theme / "doxygen-awesome.css", API / "custom.css"]),
            "EXTRA_FILES": " ".join(quoted(p) for p in extra),
            "WARNINGS": quoted(build / "warnings.log"),
        }
        doxyfile = (API / "Doxyfile.in").read_text()
        for name, value in replacements.items():
            doxyfile = doxyfile.replace("@" + name + "@", value)
        (build / "Doxyfile").write_text(doxyfile)
        subprocess.run([args.doxygen, str(build / "Doxyfile")], cwd=source, check=True)
        html = build / "html"
        for name in ("index.html", "annotated.html", "namespaces.html", "doxygen-awesome.css", "custom.css", "search/searchdata.js"):
            if not (html / name).is_file():
                raise RuntimeError("Doxygen output is missing " + name)
        for path in html.rglob("*.html"):
            text = path.read_text()
            if str(source) in text or str(ROOT) in text:
                raise RuntimeError("Local source path leaked into " + path.name)
        warnings = (build / "warnings.log").read_text() if (build / "warnings.log").exists() else ""
        # Keep warnings for maintainers outside the published site.
        (ROOT / ".site").mkdir(exist_ok=True)
        warning_log = ROOT / ".site" / ("vmxonwpi-apidocs-warnings.log" if is_vmx else "apidocs-warnings.log")
        warning_log.write_text(warnings)
        shutil.copy2(theme / "LICENSE", html / "Doxygen-Awesome-LICENSE.txt")
        (html / "build-info.json").write_text(json.dumps({**config, "theme": provenance,
            "doxygen": subprocess.check_output([args.doxygen, "--version"], text=True).strip(),
            "documentedHeaders" if is_vmx else "publicHeaders": len(headers),
            "inputHeaders": [str(p.relative_to(source)) for p in headers]}, indent=2) + "\n")
        if output.exists():
            shutil.rmtree(output)
        html.rename(output)
    print("API docs: " + str(output))
    print(("VMX interface headers: " if is_vmx else "Public headers: ") + str(len(headers)))
    print("Parser warning lines: " + str(len(warnings.splitlines())) + " (see " + str(warning_log.relative_to(ROOT)) + ")")


if __name__ == "__main__":
    main()
