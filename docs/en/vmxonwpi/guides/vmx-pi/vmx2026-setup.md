---
title: Connect a Project to VMX-Pi
---

The VMX2026 extension changes the GradleRIO deploy target and selects a compatible VMX HAL. You do not need to copy HAL files or add the W4Studica library to `build.gradle` manually.

## Connect the project

With a WPILib 2026 Groovy project open in WPILib VS Code:

1. Run **VMX2026: Change the deploy target to VMX-Pi (from RoboRIO)**.
2. Run **VMX2026: Update VMX2026 Version**. The extension downloads and verifies the matching GradleRIO and VMX HAL release pair.
3. Review your `build.gradle` and confirm the deploy target is `VmxPi` and the platform is `linuxarm64`.
4. Set your team number in WPILib preferences or pass it to Gradle with `-PteamNumber=1234`.
5. Use `./gradlew build` to build and `./gradlew deploy -PteamNumber=1234` to deploy.

The target uses SSH/SFTP to log in to the robot. The default username and password are `ubuntu` and `password`; change the password on the robot and configure credentials for your own network.

## C++ and Java

The VMX-pi target supports both C++ and Java projects. C++ programs use the VMX HAL for `linuxarm64`; the VMX-pi robot image must provide Studica's `vmxpi-hal` shared library. Java projects also need a Java 17 runtime on the robot:

```sh
sudo apt install openjdk-17-jre-headless
```

For examples, see the [GradleRIO C++ project](https://github.com/VMXONWPI/GradleRIO/tree/main/examples/vmx-cpp) and [Java project](https://github.com/VMXONWPI/GradleRIO/tree/main/examples/vmx-java).

## Offline dependencies

Run **VMX2026: Save VMX2026 Offline** while online before relying on Gradle `--offline`. The command checks the dependencies used by the project and confirms an offline build. If you change dependencies or switch targets, prepare offline use again.
