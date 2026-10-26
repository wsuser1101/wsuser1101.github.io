---
title: Troubleshooting
---

## The build fails with `VMXPi.h: No such file or directory`

The VMX HAL headers and library belong to Studica and are not part of the W4Studica download. A new project fetches them from your robot once. Connect the VMX-Pi and run a deploy, or fetch them directly:

```sh
./gradlew fetchVmxSdksystemcore
```

The last word is the name of the deploy target in your `build.gradle` (`systemcore` in a project created with the W4Studica extension). After the first fetch, builds work without the robot, even after `clean`.

## Deploy cannot find the robot, or the first connection is slow

Wi-Fi power saving on your computer can delay the first reply from the VMX-Pi by several seconds. Turn off power saving for the Wi-Fi adapter. On Linux with NetworkManager:

```sh
nmcli connection modify <connection name> 802-11-wireless.powersave 2
```

Also check that the PC joined the VMX-Pi hotspot or is wired with an automatic (DHCP) address. See [VMX-Pi Network](vmx-pi-network.md).

## The next start fails with `initMboxBlock: init mbox zaps failed`

The previous program was killed before it could clean up. Reboot the VMX-Pi. A normal stop takes about a second.

## A motor does not turn

A Titan ignores commands until it is enabled. Use `wpilibvmx::StudicaTitan` with `wpilibvmx::TitanEnableGuard`, send speed commands at least every 150 ms, and do not call `studica_driver::Titan::Enable()`. See [Start Robot Coding](start-robot-coding.md).

## A servo or PWM output does nothing

Look at the program output on the VMX-Pi:

```sh
journalctl -u robot_manager -f
```

A working PWM channel prints `HALSim VMX: PWM <n> -> VMX channel <m>`. If it is missing, `HALSIMVMX_PWM_MAP` is not set or does not list that channel. See [Hardware Support](hardware-support.md). PWM output is new in Beta 6 and has not been tested on a robot yet, so please report what you see.

## A WPILib input or output has no effect

The program log says which maps are missing, for example `HALSIMVMX_DIO_MAP is not set; no DIO channels mapped`. Map the channels as described in [Hardware Support](hardware-support.md).

## The log fills with `[GetSingle] Failed to write config!`

The Cobra sensor does not answer on the I2C bus. It is not connected, or its wiring is wrong. The program keeps running, and the Cobra values read as -1.
