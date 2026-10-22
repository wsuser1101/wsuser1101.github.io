# VMX on WPI C++ API

**WPILib 2026.2.2 · VMX HAL 2026.2.2-vmx.2**

C++ reference generated from the VMX on WPI release source. Use **Classes**,
**Namespaces**, the navigation tree, or search to find an API.

| API | Start here |
| --- | --- |
| Robot framework and I/O | @ref frc "frc namespace" — robot lifecycle, Driver Station, sensors and outputs |
| Command-based programming | @ref frc2 "frc2 namespace" — commands, subsystems, scheduling and triggers |
| NetworkTables | @ref nt "nt namespace" — networked robot data |
| Utilities | @ref wpi "wpi namespace" — shared WPILib utilities |
| HAL | Public `hal/` headers — hardware abstraction implemented by the VMX-pi backend |

## Common starting points

- @ref frc::TimedRobot "TimedRobot": periodic robot lifecycle methods.
- @ref frc::DriverStation "DriverStation": robot enable state and operator input.
- @ref frc::DigitalInput "DigitalInput": digital input channels.
- @ref frc::PWM "PWM": PWM outputs.
- @ref frc2::CommandScheduler "CommandScheduler": schedule and run commands.

## VMX-pi hardware support

This reference includes WPILib public APIs. An API appearing here does not mean
the corresponding hardware feature is supported by the VMX-pi backend.

Digital I/O, analog input, encoders, PWM, I2C and manual SPI use the VMX HAL backend.
Automatic SPI transfers, averaged/filtered analog triggers, DMA and DutyCycle
hardware are not supported. Check the hardware guide and verify behavior on the
robot before using an interface.

The proprietary Studica VMX SDK headers and `libvmxpi_hal_cpp.so` are not included
in this reference. This is the WPILib 2026 API; W4Studica 2027-specific drivers
and integration classes belong to the separate W4Studica API reference.

## Guides and source

- [VMX on WPI guides](/vmxonwpi/)
- [한국어 안내](/ko/vmxonwpi/)
- [Hardware support](/vmxonwpi/guides/vmx-pi/hardware-support/)
- [Release source](https://github.com/VMXONWPI/allwpilib/tree/7a10d27fe5bb3291e9a8fc62db0e3d400982d530)
- [VMX HAL implementation notes](https://github.com/VMXONWPI/allwpilib/blob/7a10d27fe5bb3291e9a8fc62db0e3d400982d530/vmx/README.md)

This page documents C++. VMX on WPI also supports Java robot projects; Java
API documentation is outside this reference.
