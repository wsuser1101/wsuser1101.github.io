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
MODULES = ("apriltag", "cameraserver", "cscore", "datalog", "drivers", "fields",
           "hal", "ntcore", "commandsv2", "telemetry", "tunables", "wpilibc",
           "wpimath", "wpinet", "wpiutil", "romiVendordep", "xrpVendordep")


def quoted(value):
    return '"' + str(value).replace("\\", "/").replace('"', '\\"') + '"'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allwpilib", type=Path, default=ROOT.parent / "allwpilib")
    parser.add_argument("--output", type=Path, default=ROOT / "site/apidocs")
    parser.add_argument("--doxygen", default="doxygen")
    args = parser.parse_args()
    source = args.allwpilib.resolve()
    output = args.output.resolve()
    config = json.loads((API / "source.json").read_text())
    if subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip() != config["ref"]:
        parser.error("allwpilib HEAD must match the pinned ref in apidocs/source.json")
    if output == ROOT or output == source or ROOT.is_relative_to(output) or source.is_relative_to(output):
        parser.error("output must not replace a source checkout or its parent")
    theme = API / "theme"
    provenance = json.loads((theme / "SOURCE.json").read_text())
    for name, expected in provenance["sha256"].items():
        if hashlib.sha256((theme / name).read_bytes()).hexdigest() != expected:
            parser.error("Vendored theme checksum mismatch: " + name)
    inputs = []
    for module in MODULES:
        public = source / module / "src/main/native/include"
        if not public.is_dir():
            parser.error("Missing public header directory: " + str(public))
        inputs.append(public)
        generated = source / module / "src/generated/main/native/include"
        if generated.is_dir():
            inputs.append(generated)
    vendor = source / "studica/drivers"
    inputs += [vendor,
               source / "studica/include",
               source / "simulation/halsim_studica/src/main/native/include"]
    if any(not path.is_dir() for path in inputs):
        parser.error("Incomplete VMX/Studica public sources")
    # Enumerate public headers: never recurse into Studica's examples or SDK files.
    headers = sorted({p for directory in inputs for pattern in ("*.h", "*.hpp")
                      for p in (directory.glob(pattern) if directory == vendor
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
            "VERSION": quoted(config["version"]), "BUILD_DIRECTORY": quoted(build),
            "INPUT": " ".join(quoted(p) for p in headers + [API / "mainpage.md"]),
            "STRIP_PATHS": " ".join(quoted(p) for p in inputs + [source, API]),
            "MAINPAGE": quoted(API / "mainpage.md"), "HEADER": quoted(header),
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
        (ROOT / ".site/apidocs-warnings.log").write_text(warnings)
        shutil.copy2(theme / "LICENSE", html / "Doxygen-Awesome-LICENSE.txt")
        (html / "build-info.json").write_text(json.dumps({**config, "theme": provenance,
            "doxygen": subprocess.check_output([args.doxygen, "--version"], text=True).strip(),
            "publicHeaders": len(headers)}, indent=2) + "\n")
        if output.exists():
            shutil.rmtree(output)
        html.rename(output)
    print("API docs: " + str(output))
    print("Public headers: " + str(len(headers)))
    print("Parser warning lines: " + str(len(warnings.splitlines())) + " (see .site/apidocs-warnings.log)")


if __name__ == "__main__":
    main()
