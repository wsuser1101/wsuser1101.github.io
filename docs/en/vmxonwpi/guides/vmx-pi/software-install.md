---
title: Install WPILib and VMX2026
---

## Install WPILib 2026

Download and install the official **WPILib 2026.2.2** release for your development computer. Select the installer for your operating system and CPU architecture.

[WPILib 2026.2.2 release and installers](https://github.com/wpilibsuite/allwpilib/releases/tag/v2026.2.2)

Use the WPILib VS Code installation created by that installer when creating and deploying robot projects. Do not use a 2027 W4Studica project or extension for this workflow.

## Install the VMX2026 extension

Download the latest `.vsix` from the VMX2026 extension releases page. The current release is **2.0.3**.

[VMX2026 extension releases](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases)

In WPILib VS Code, open **Extensions**, select the `…` menu, choose **Install from VSIX…**, and open the downloaded file. Restart VS Code if it asks you to.

## Robot-side software

The VMX-pi needs 64-bit Ubuntu 24.04 or 26.04, Studica's `vmxpi-hal` package, and the VMX Robot Manager service. Java robot projects also require Java 17 on the robot:

```sh
sudo apt install openjdk-17-jre-headless
```

See [VMX-Pi Setup](vmx-pi-setup.md) for the robot prerequisites and the [Robot Manager repository](https://github.com/VMXONWPI/wpi-robot-manager) for package installation.
