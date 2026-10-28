# W4Studica C++ API

**2027.0.0-alpha-7-w4.beta.7 · Beta**

C++ reference for WPILib on Studica VMX-pi. Use the **Classes** and
**Namespaces** menus, the navigation tree, or search to find an API.

| API | Start here |
| --- | --- |
| WPILib | @ref wpi "WPILib namespace" — robot framework, hardware interfaces, math and utilities |
| Studica integration | @ref wpi::studica "Studica namespace" — Titan control, shared hardware access and RTC readings |
| Original Studica drivers | @ref studica_driver "Studica device classes" — exposed as `wpi::studica::drivers` |

The original driver classes retain their upstream namespace in this reference.
Include headers such as `wpi/studica/drivers/Titan.hpp` and use the
`wpi::studica::drivers` namespace alias in robot programs.

## VMX essentials

- @ref wpi::studica::Titan "Titan": integrates the original Titan driver with enable keepalives and control-loop/Driver Station freshness checks. Feed the control loop after a successful control cycle, and feed the Driver Station only when a fresh valid packet arrives.
- @ref wpi::studica::SharedVMX "SharedVMX()": share one VMXPi connection across Studica devices.
- @ref wpi::studica::MakeDriver "MakeDriver()": construct an original Studica driver using the shared VMX connection.
- @ref wpi::studica::ReadRtc "ReadRtc()": read raw RTC calendar fields. A successful read does not establish that the clock is set correctly; the fields are not converted to Unix time.

## VMX support

| Interface | Status |
| --- | --- |
| Digital input/output, analog input, encoder | Implemented with fixed VMX channel mappings |
| PWM, DutyCycle and I2C | Hardware backend implemented; I2C port 1 opens on its first transaction |
| Onboard IMU | Automatically connected; quaternion data supported; mounting corrections still need hardware verification |
| Titan and Studica-specific devices | Use `wpi::studica::Titan` for integrated Titan control, or `MakeDriver()` for original drivers |
| RTC | Raw calendar reads supported through `ReadRtc()` |
| Digital edge capture | Backend implemented; standard WPILib interrupt wrapper integration remains unsupported |

Digital channels 0–21 use the same VMX channel indices. Analog channels 0–3
map to VMX channels 22–25. PWM uses matching channel indices where supported
by the hardware. No channel-map environment variables are required.

An API appearing in this reference does not establish VMX hardware support or
physical validation. Battery readings and IMU mounting behavior still need
hardware verification. HAL simulation APIs and internal integration classes
are also listed for reference; `wpi::studica::detail` contains internal helpers.

## Guides and releases

- [W4Studica documentation](/)
- [Beta release](https://github.com/W4Studica/allwpilib/releases/tag/v2027.0.0-alpha-7-w4.beta.7)
- [Studica integration source](https://github.com/W4Studica/allwpilib/tree/24807f4a6a3a9b29a4a1553ba6d111035ee14b6a/studica)
- [HAL simulation bridge source](https://github.com/W4Studica/allwpilib/tree/24807f4a6a3a9b29a4a1553ba6d111035ee14b6a/simulation/halsim_studica)

This reference is generated from the pinned beta source. The VMX HAL SDK is not
included. Robot programs are C++ only.
