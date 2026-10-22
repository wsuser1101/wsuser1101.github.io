---
title: Troubleshooting
---

## Gradle says a dependency is not cached in offline mode

`--offline` only works after Gradle has downloaded every project dependency. Connect the development computer to the Internet and run **VMX2026: Save VMX2026 Offline** in WPILib VS Code. Let the online resolution, build, and offline verification finish before deploying offline. See [VS Code Setup](vscode-setup.md).

## Deployment fails with an SFTP `No such file` error

Install the current [VMX2026 extension release](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases) (2.0.3 or newer). Earlier versions could leave the RoboRIO `/home/lvuser/deploy` path in a VMX project. The VMX target must deploy static files under its configured login home, normally `/home/ubuntu/deploy`.

## `robot_manager` is not running

Check and start the service on the robot:

```sh
sudo systemctl status robot_manager --no-pager
sudo systemctl restart robot_manager
sudo journalctl -u robot_manager -n 100 --no-pager
```

If the unit is missing, install the VMX Robot Manager package from the [wpi-robot-manager repository](https://github.com/VMXONWPI/wpi-robot-manager). Also confirm that the deployed `/home/ubuntu/robotCommand` exists and is executable.

## SSH or deployment cannot reach the robot

Confirm that the development computer is connected to the robot's access point or the same router, or that its wired connection uses DHCP. The robot's direct Ethernet address is `172.22.11.2`; the access point address is `10.TE.AM.2`. See [VMX-Pi Network](vmx-pi-network.md).

## Java program fails to start

Install the Java 17 runtime on the VMX-pi:

```sh
sudo apt install openjdk-17-jre-headless
```

## C++ code cannot find `VMXPi.h`

Standard WPILib code does not need to include `VMXPi.h`. If your C++ code uses the Studica SDK directly, the robot must have the `vmxpi-hal` package. Use the SDK-fetch instructions in the [GradleRIO VMX-pi notes](https://github.com/VMXONWPI/GradleRIO/blob/main/VMX.md).

## Program output or robot logs are missing

```sh
sudo journalctl -u robot_manager -f
```

The service also writes `/home/lvuser/FRC_UserProgram.log`. Check `robot_manager` status first if neither log changes.
