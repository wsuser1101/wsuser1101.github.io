---
title: Hardware Support
---

VMX on WPI uses the WPILib 2026 HAL backend for the VMX-pi. Robot code can use WPILib classes on the supported `linuxarm64` target. C++ and Java robot programs are supported; Java requires Java 17 on the robot.

| Area | Support notes |
|---|---|
| Driver Station | Uses the WPILib Driver Station protocol. Robot outputs remain disabled until the Driver Station is attached and enabled. |
| Digital I/O, analog, encoders, PWM | Implemented by the VMX-pi HAL using Studica's VMX library. Check the board and SDK channel documentation before wiring. |
| I2C and manual SPI | Supported through the HAL backend. Automatic SPI transfers are not supported by the current VMX SDK. |
| Analog triggers | Raw analog triggers are supported. Averaged and filtered triggers are not supported by the current VMX SDK. |
| DMA, DutyCycle, radio LED, user rails | Not available on the VMX-pi HAL backend. Unsupported operations return an error or do nothing where WPILib defines a no-op. |
| VMX native library | Studica's `libvmxpi_hal_cpp.so` is supplied by the robot image/package and is not included in the VMX2026 release archives. |

The HAL has host-side regression tests, but those do not replace tests with the actual VMX-pi, sensors, motor controllers, and Driver Station. Verify each I/O path and safety behavior on the hardware before using it in a robot.

See the [VMX HAL implementation notes](https://github.com/VMXONWPI/allwpilib/blob/main/vmx/README.md) and [GradleRIO VMX-pi deployment notes](https://github.com/VMXONWPI/GradleRIO/blob/main/VMX.md).

## Studica device classes

TitanQuad, TitanQuadEncoder, Cobra, Servo, ServoContinuous and the original
Studica 360-degree Lidar are implemented in the development-source wpilibc /
wpilibj libraries. They are not yet part of the current extension release.
See [Studica APIs](studica-api.md) for supported models, matching libraries,
C++ / Java examples and hardware verification limits.
