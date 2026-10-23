---
title: Start Robot Coding
---

Create a normal **WPILib 2026 C++ or Java** robot project in WPILib VS Code, then connect it to VMX-pi with the [VMX2026 extension](vscode-setup.md). Keep robot logic in your project; the extension changes the build and deploy configuration for the VMX-pi target.

## Build and deploy

From the project folder:

```sh
./gradlew build
./gradlew deploy -PteamNumber=1234
```

Replace `1234` with your FRC team number. GradleRIO connects to the robot at its wired or team-based Wi-Fi address, stops `robot_manager`, uploads the program and runtime libraries, then starts the service again. The service runs the deployed `robotCommand` and restarts it if it exits unexpectedly.

For a Java project, install Java 17 on the robot. For C++, the robot image must provide Studica's VMX HAL shared library. See [VMX-Pi Setup](vmx-pi-setup.md).

## Use WPILib APIs

Use the standard WPILib classes provided by the 2026 project template, such as `TimedRobot`, `DigitalInput`, `Encoder`, `AnalogInput`, `PWM`, and `BuiltInAccelerometer`, subject to the [hardware support notes](hardware-support.md). The VMX-pi HAL owns the VMX connection; do not install or copy another HAL into the project.

You can also use the Studica VMX SDK directly in C++ when your application needs a feature outside the WPILib API. The SDK is supplied by the robot's `vmxpi-hal` package. Follow the [GradleRIO VMX-pi notes](https://github.com/VMXONWPI/GradleRIO/blob/main/VMX.md) for the SDK fetch task and CMake/Gradle setup.

## Robot logs

The robot manager writes service output to systemd and `/home/lvuser/FRC_UserProgram.log`:

```sh
sudo journalctl -u robot_manager -f
```

For setup and deployment details, see [Connect a Project to VMX-Pi](vmx2026-setup.md).

## Studica device APIs

For Titan motors, Titan encoders, Cobra, Studica servos and the original 360-degree
LiDAR, see [Studica APIs](studica-api.md). The guide includes C++ and Java
examples and explains which matching release libraries are required.
