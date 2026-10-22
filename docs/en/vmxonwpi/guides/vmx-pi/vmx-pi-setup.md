---
title: VMX-Pi Setup
---

## Robot requirements

VMX on WPI is tested with a Raspberry Pi 4 running **64-bit Ubuntu 26.04.1 LTS** and the Studica `vmxpi-hal` package. The VMX HAL's `libvmxpi_hal_cpp.so` and headers come from Studica and are not bundled with WPILib or the Robot Manager package.

Prepare a 64-bit Ubuntu 26.04 ARM64 system image for the VMX-pi. If you use a prebuilt image, verify that it includes the VMX-pi HAL before deploying. The image distribution link used by the lab is temporary; ask the project maintainer for the current image and its checksum before flashing it.

## Write the image to storage

Use Raspberry Pi Imager to write the compatible image to the robot's SD card or storage device.

1. Select the Raspberry Pi model that matches the robot.
2. Open the operating-system list and choose **Use custom**.
3. Select the Ubuntu 26.04 ARM64 VMX-pi image.
4. Select the robot's storage device and verify its name and capacity.
5. Confirm the write. **This erases all data on the selected device.**
6. Wait for both writing and verification to finish before removing the card.

## First boot

Connect the robot to Ethernet or its Wi-Fi access point and sign in as `ubuntu`. Change any default password before putting the robot on a shared network. Install the VMX Robot Manager package; its repository includes instructions to build the `.deb` from source:

[VMXONWPI/wpi-robot-manager](https://github.com/VMXONWPI/wpi-robot-manager)

The package configures the `robot_manager` service, NetworkManager integration, wired networking, CPU and Wi-Fi performance settings, and the `/home/lvuser` runtime directory. The Studica `vmxpi-hal` package must also be present.

For connection addresses and network commands, see [VMX-Pi Network](vmx-pi-network.md). For the computer-side WPILib setup, see [Install WPILib and VMX2026](software-install.md).
