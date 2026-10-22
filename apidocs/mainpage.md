# W4Studica C++ API

**2027.0.0-alpha-7-w4.beta.6 · Beta**

C++ reference for WPILib on Studica VMX-pi. Use the **Classes** and
**Namespaces** menus, the navigation tree, or search to find an API.

| API | Start here |
| --- | --- |
| WPILib | @ref wpi "WPILib namespace" — robot framework, hardware interfaces, math and utilities |
| Studica Drivers | @ref studica_driver "Studica device classes" — Titan, sensors and peripheral devices |
| W4Studica VMX | @ref wpilibvmx "VMX integration" — shared hardware access, backend and control helpers |

## VMX essentials

- @ref wpilibvmx::SharedVMX "SharedVMX()": share one VMXPi instance across Studica devices.
- @ref wpilibvmx::StudicaTitan "StudicaTitan": send single enable/disable frames for Titan control.
- @ref wpilibvmx::TitanEnableGuard "TitanEnableGuard": follow enabled/E-stop state and send keepalives.
- @ref wpilibvmx::ControlLoopWatchdog "ControlLoopWatchdog": independently check control-loop and fresh DS input deadlines.

## VMX support

| Interface | Status |
| --- | --- |
| Digital input/output, analog input, encoder | Implemented; configure the VMX channel mapping |
| Onboard IMU | Implemented; roll/pitch axes and Z angular-rate sign still need hardware verification |
| Titan and Studica-specific devices | Use the Studica C++ APIs with SharedVMX; use StudicaTitan with TitanEnableGuard for enable control |
| WPILib PWM, DutyCycle and I2C hardware integration | Deferred |

An API appearing in this reference does not establish VMX hardware support.
HAL simulation APIs and internal integration classes are also listed for reference.

## Guides and releases

- [W4Studica documentation](/W4Studica/)
- [Beta release](https://github.com/W4Studica/allwpilib/releases/tag/v2027.0.0-alpha-7-w4.beta.6)
- [VMX integration source and hardware record](https://github.com/W4Studica/allwpilib/tree/a2eaade996868bb5ec13c5ec2d00f1d931facb00/simulation/halsim_vmx)

This reference is generated from the pinned beta source. The VMX HAL SDK is not
included. Robot programs are C++ only.
