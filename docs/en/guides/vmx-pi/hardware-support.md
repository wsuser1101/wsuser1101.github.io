---
title: Hardware Support
---

This page lists which VMX-pi hardware robot code can use through WPILib classes, how to connect WPILib channel numbers to VMX channels, and what has been checked on a real robot.

## What works through WPILib classes

| WPILib class | VMX hardware | Setting | Status |
|---|---|---|---|
| `DigitalInput`, `DigitalOutput` | FlexDIO, HiCurrDIO (output only), CommDIO | `HALSIMVMX_DIO_MAP` | Checked on a VMX-pi |
| `AnalogInput` | AnalogIn | `HALSIMVMX_ANALOG_MAP` | Checked on a VMX-pi |
| `Encoder` | FlexDIO pairs | `HALSIMVMX_DIO_MAP` (both channels) | Checked on a VMX-pi |
| `OnboardIMU` (use `FLAT`) | navX: yaw, roll, pitch, rates, acceleration | `HALSIMVMX_IMU` | Yaw and Z acceleration checked. Roll, pitch and Z-rate directions are not verified |
| `PWM`, `Servo`, PWM motor controllers | FlexDIO, HiCurrDIO, CommDIO 26 and 27 | `HALSIMVMX_PWM_MAP` | In Beta 6, **not yet tested on a robot** |
| `RobotController` battery voltage | VMX system voltage | none | In Beta 6, **not yet tested on a robot** |

Not available through WPILib classes:

- **I2C**, **DutyCycle** and **DutyCycleEncoder**. Use the Studica classes instead, for example `Cobra` for I2C.
- **Interrupts.** The WPILib 2027 alpha 7 HAL has no interrupt API.
- **IMU quaternion.** `OnboardIMU::GetQuaternion()` and `GetRotation3d()` return zeros. Build the rotation from the angles: `wpi::math::Rotation3d{imu.GetAngleX(), imu.GetAngleY(), imu.GetYaw()}`. Create the IMU with `OnboardIMU::FLAT`; other mount orientations are not handled.
- **Java.** Robot programs are C++ only.

Studica devices that have no WPILib equivalent (`Titan`, `Ultrasonic`, `Sharp`, `Cobra`, `Colore`, `Parsec`, `LightTower`) use the Studica classes. Always pass `wpilibvmx::SharedVMX()` to them, as described in [Start Robot Coding](start-robot-coding.md).

## Connect WPILib channels to VMX channels

WPILib channel numbers are not VMX channel numbers, so each channel you use must be mapped. Add the settings to the `wpilibCpp` artifact in your project's `build.gradle`. They are passed to the program as environment variables when it runs on the VMX-pi.

```groovy
artifacts {
    wpilibCpp(getArtifactTypeClass('WPILibNativeArtifact')) {
        environment.put('HALSIMVMX_DIO_MAP', '0:0,1:1')
        environment.put('HALSIMVMX_ANALOG_MAP', '0:22')
        environment.put('HALSIMVMX_PWM_MAP', '0:12')
        environment.put('HALSIMVMX_IMU', '1')
    }
    // ...
}
```

This example maps WPILib DIO 0 and 1 to VMX channels 0 and 1 (also used for an `Encoder` on 0 and 1), `AnalogInput` 0 to AnalogIn 22, and `PWM` 0 to HiCurrDIO 12, and turns on the navX as the `OnboardIMU`.

Each entry is `<WPILib channel>:<VMX channel>`. Separate entries with commas and no spaces. Channels that are not mapped are ignored. The robot log reports a map that is missing, malformed, or maps two WPILib channels to one VMX channel.

An `Encoder` uses two DIO channels, so map both. A VMX channel serves one function at a time.

### VMX channels

| Type | Channels | Functions |
|---|---|---|
| FlexDIO | 0 to 11 | Digital in/out, PWM, encoders. Encoder pairs are (0,1) (2,3) (4,5) (6,7) (8,9): A is the even channel, B the odd one |
| HiCurrDIO | 12 to 21 | Digital output and PWM only |
| AnalogIn | 22 to 25 | Analog input |
| CommDIO | 26 to 33 | 26 and 27: digital in/out, PWM, I2C. 28 to 33: UART and SPI |

These are VMX channel indexes. Whether they match the numbers printed on the board has not been checked yet. Avoid CommDIO 26 to 33 for anything else while a program uses I2C, UART or SPI.

For the full design, see [`DESIGN.md`](https://github.com/W4Studica/allwpilib/blob/main/simulation/halsim_vmx/DESIGN.md) and the measured results in [`HARDWARE_CHECKLIST.md`](https://github.com/W4Studica/allwpilib/blob/main/simulation/halsim_vmx/HARDWARE_CHECKLIST.md).
