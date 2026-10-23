#!/usr/bin/env python3
"""Build the focused VMX Java API reference from the pinned allwpilib source."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
API = ROOT / 'apidocs/vmxonwpi'
STUDICA = ('TitanQuad', 'TitanQuadEncoder', 'Cobra', 'Servo', 'ServoContinuous', 'Lidar')
# The Java counterparts of VMX_WPILIB_HEADERS in build_apidocs.py.
WPILIB = (
    'DigitalInput', 'DigitalOutput', 'DigitalSource', 'DigitalGlitchFilter',
    'AnalogInput', 'AnalogGyro', 'AnalogTrigger', 'AnalogTriggerOutput',
    'Counter', 'CounterBase', 'Encoder', 'PWM', 'Servo',
    'motorcontrol/PWMMotorController', 'Relay', 'AddressableLED',
    'BuiltInAccelerometer', 'I2C', 'SPI', 'SerialPort', 'AsynchronousInterrupt',
    'SynchronousInterrupt', 'Notifier', 'Timer', 'DriverStation', 'DSControlWord',
    'GenericHID', 'Joystick', 'RobotController', 'RobotState', 'RuntimeType',
    'Threads', 'CAN', 'PowerDistribution', 'Compressor', 'Solenoid',
    'DoubleSolenoid', 'PneumaticsBase', 'PneumaticsModuleType', 'PneumaticHub',
    'PneumaticsControlModule', 'SpeedController', 'smartdashboard/SendableBuilder',
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--allwpilib', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=ROOT / 'site/vmxonwpi/javadocs')
    parser.add_argument('--java-home', type=Path)
    args = parser.parse_args()
    source, output = args.allwpilib.resolve(), args.output.resolve()
    config = json.loads((API / 'source.json').read_text())
    if subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip() != config['ref']:
        parser.error('allwpilib HEAD must match apidocs/vmxonwpi/source.json')
    if (output == ROOT or output == source or ROOT.is_relative_to(output)
            or source.is_relative_to(output) or output.is_relative_to(source)
            or (output.is_relative_to(ROOT) and not output.is_relative_to(ROOT / 'site'))):
        parser.error('output must be inside site/ or outside both source checkouts')
    def tool(name):
        return str(args.java_home / 'bin' / name) if args.java_home else name

    dependencies = json.loads((API / 'java-dependencies.json').read_text())
    cache = ROOT / '.site/java-dependencies'
    cache.mkdir(parents=True, exist_ok=True)
    jars = []
    for dep in dependencies:
        path = cache / dep['file']
        if not path.exists():
            request = urllib.request.Request(dep['url'], headers={'User-Agent': 'VMX-on-WPI-Javadoc'})
            with urllib.request.urlopen(request, timeout=120) as response:
                data = response.read()
            if hashlib.sha256(data).hexdigest() != dep['sha256']:
                raise RuntimeError('Download checksum mismatch: ' + dep['file'])
            path.write_bytes(data)
        if hashlib.sha256(path.read_bytes()).hexdigest() != dep['sha256'] or not zipfile.is_zipfile(path):
            raise RuntimeError('Dependency checksum mismatch: ' + dep['file'])
        jars.append(str(path))
    java = source / 'wpilibj/src/main/java'
    studica = java / 'com/studica/frc'
    wpilib = java / 'edu/wpi/first/wpilibj'
    documented = [studica / (name + '.java') for name in STUDICA]
    documented += [wpilib / (name + '.java') for name in WPILIB]
    # Resolve new compatibility adapters and DTR against the official 2026 jars.
    compile_sources = sorted(studica.glob('*.java')) + [
        wpilib / 'SpeedController.java', wpilib / 'smartdashboard/SendableBuilder.java',
        wpilib / 'SerialPort.java', source / 'hal/src/main/java/edu/wpi/first/hal/SerialPortJNI.java']
    for path in documented + compile_sources:
        if not path.is_file():
            parser.error('Missing Java input: ' + str(path))
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.javadocs-', dir=output.parent) as temporary:
        build = Path(temporary)
        classes, empty, html = build / 'classes', build / 'empty', build / 'html'
        classes.mkdir()
        empty.mkdir()
        classpath = os.pathsep.join(jars)
        subprocess.run([tool('javac'), '--release', '17', '-encoding', 'UTF-8',
                        '-proc:none', '-sourcepath', str(empty), '-classpath', classpath,
                        '-d', str(classes), *map(str, compile_sources)], check=True)
        command = [tool('javadoc'), '-quiet', '-public', '-notimestamp', '-encoding', 'UTF-8',
                   '-docencoding', 'UTF-8', '-charset', 'UTF-8', '-Xdoclint:all,-missing',
                   '-sourcepath', str(empty), '-classpath', str(classes) + os.pathsep + classpath,
                   '-d', str(html), '-windowtitle', 'VMX on WPI Java API',
                   '-doctitle', 'VMX on WPI Java API · ' + config['version'],
                   '-overview', str(API / 'java-overview.html'), '-tag', 'pre:a:Precondition:',
                   '-header', '<a href="/vmxonwpi/">Guides</a> · <a href="/vmxonwpi/apidocs/">C++ API</a>',
                   *map(str, documented)]
        result = subprocess.run(command, text=True, capture_output=True)
        (ROOT / '.site/vmxonwpi-javadocs-warnings.log').write_text(result.stdout + result.stderr)
        if result.returncode:
            print(result.stdout + result.stderr)
            result.check_returncode()
        required = ['index.html', 'allclasses-index.html', 'com/studica/frc/Lidar.Port.html']
        required += ['com/studica/frc/' + name + '.html' for name in STUDICA]
        required += ['edu/wpi/first/wpilibj/' + name + '.html' for name in WPILIB]
        for name in required:
            if not (html / name).is_file():
                raise RuntimeError('Missing Javadoc page: ' + name)
        for path in html.rglob('*.html'):
            text = path.read_text()
            if str(source) in text or str(ROOT) in text:
                raise RuntimeError('Local source path leaked into ' + path.name)
        for name in ('TitanBus', 'LidarProtocol'):
            if (html / 'com/studica/frc' / (name + '.html')).exists():
                raise RuntimeError('Internal helper was published: ' + name)
        (html / 'build-info.json').write_text(json.dumps({**config,
            'javadoc': subprocess.check_output([tool('javadoc'), '--version'], text=True).strip(),
            'dependencies': dependencies,
            'inputSources': [str(path.relative_to(source)) for path in documented]}, indent=2) + '\n')
        if output.exists():
            shutil.rmtree(output)
        html.rename(output)
    print(f'Java API docs: {output} ({len(documented)} source files)')
    print('Diagnostics: .site/vmxonwpi-javadocs-warnings.log')


if __name__ == '__main__':
    main()
