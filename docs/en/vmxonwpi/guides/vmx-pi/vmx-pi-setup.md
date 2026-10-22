---
title: VMX-Pi Setup
---

## Download the VMX on WPI image

VMX on WPI will be distributed as a bootable VMX-pi image. The goal is a ready-to-deploy robot: flash the image, power on the VMX-pi, connect the development computer to the robot's Wi-Fi hotspot, and deploy a WPILib project over that local connection. Internet access is not required for the robot-to-computer deployment connection. The image is intended to include the tested **64-bit Ubuntu 26.04.1 LTS** base and the robot-side VMX HAL, Robot Manager, and hotspot setup, so you do not need to install these packages by hand.

The image release link, version, login details, and checksum will be listed here when the first VMX on WPI image is published. Use the release notes for the exact image contents and credentials; do not substitute a W4Studica 2027 image.

## Write the image to storage

After downloading the image, use Raspberry Pi Imager to write it to the robot's SD card or storage device.

1. Select the Raspberry Pi model that matches the robot.
2. Open the operating-system list and choose **Use custom**.
3. Select the VMX on WPI image file.
4. Select the robot's storage device and verify its name and capacity.
5. Confirm the write. **This erases all data on the selected device.**
6. Wait for both writing and verification to finish before removing the card.

## First boot

Power on the robot, join the VMX hotspot from the development computer using the SSID and password listed in the image release notes, then deploy to the robot's hotspot address. The image starts the `robot_manager` service and configures NetworkManager, the Wi-Fi hotspot and wired networking, CPU and Wi-Fi performance settings, and the `/home/lvuser` runtime directory. Its implementation is maintained in the [VMXONWPI/wpi-robot-manager repository](https://github.com/VMXONWPI/wpi-robot-manager).

For connection addresses and network commands, see [VMX-Pi Network](vmx-pi-network.md). For the computer-side WPILib setup, see [Install WPILib and VMX2026](software-install.md).
