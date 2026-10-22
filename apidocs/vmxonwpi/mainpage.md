# VMX on WPI C++ API

**WPILib APIs with VMX implementations · 2026.2.2-vmx.2**

This reference covers both **standard WPILib hardware APIs implemented by the
VMX-pi port** and **VMX-specific interfaces added by the port**. An API does not
need a new name or declaration to be included: standard WPILib classes and HAL
functions with a VMX implementation belong here too.

Use **Classes**, **Namespaces**, **Files**, or search to find an interface.

## WPILib APIs with VMX implementations

These are the standard APIs used by robot programs. The VMX port supplies the
underlying HAL implementations in `hal/src/main/native/mau`.

| Area | Robot API | VMX HAL implementation |
| --- | --- | --- |
| Digital I/O | @ref frc::DigitalInput, @ref frc::DigitalOutput, @ref frc::DigitalGlitchFilter | `DIO.cpp` |
| Analog input and accumulation | @ref frc::AnalogInput, @ref frc::AnalogGyro | `AnalogInput.cpp`, `AnalogAccumulator.cpp`, `AnalogGyro.cpp` |
| Analog triggers | @ref frc::AnalogTrigger, @ref frc::AnalogTriggerOutput | `AnalogTrigger.cpp` |
| Counters and encoders | @ref frc::Counter, @ref frc::Encoder | `Counter.cpp`, `Encoder.cpp` |
| PWM and servo outputs | @ref frc::PWM, @ref frc::Servo, @ref frc::PWMMotorController | `PWM.cpp` |
| Relay and addressable LEDs | @ref frc::Relay, @ref frc::AddressableLED | `Relay.cpp`, `AddressableLED.cpp` |
| Onboard acceleration | @ref frc::BuiltInAccelerometer | `Accelerometer.cpp` |
| I2C, SPI and serial | @ref frc::I2C, @ref frc::SPI, @ref frc::SerialPort | `I2C.cpp`, `SPI.cpp`, `SerialPort.cpp` |
| Interrupts and timing | @ref frc::SynchronousInterrupt, @ref frc::AsynchronousInterrupt, @ref frc::Notifier, @ref frc::Timer | `Interrupts.cpp`, `Notifier.cpp`, `HAL.cpp` |
| Driver Station and operator input | @ref frc::DriverStation, @ref frc::GenericHID, @ref frc::Joystick | `DriverStation.cpp`, `DriveStation/` |
| Robot state and power | @ref frc::RobotState, @ref frc::RobotController | `HAL.cpp`, `Power.cpp` |
| CAN devices | @ref frc::CAN, @ref frc::PowerDistribution, @ref frc::Compressor, @ref frc::Solenoid, @ref frc::DoubleSolenoid | `CAN.cpp`, `CANAPI.cpp`, `PowerDistribution.cpp`, `CTREPCM.cpp`, `REVPH.cpp` |

The corresponding standard HAL declarations are also indexed under **Files**.
General WPILib math, NetworkTables and command APIs are outside this focused
reference because the VMX port does not add hardware implementations for them.

## Implementation limits

Including a class or HAL declaration does not mean every operation is supported.
These pages retain the standard WPILib API comments; apply the VMX limits below
and consult the [hardware support guide](/vmxonwpi/guides/vmx-pi/hardware-support/).

- Analog triggers support raw input; averaged and filtered triggers are unsupported.
- SPI supports manual transfers; automatic transfers are unsupported by the VMX SDK.
- Onboard acceleration has a fixed 2G range; changing the range has no effect.
- Analog output, DMA and DutyCycle HAL entries are compatibility stubs, not working hardware features.
- RoboRIO-specific user rails and radio LEDs do not provide equivalent VMX hardware behavior.
- Channel availability and capability follow the VMX channel map. CAN device operation and each I/O path require verification on the actual robot.

## VMX-specific backend interfaces

The following interfaces were added for the port's **internal HAL implementation**.
Robot programs normally use the public WPILib APIs above.

| Area | Interfaces |
| --- | --- |
| Channel mapping | @ref Mau_Channel, @ref Mau_ChannelGroup, @ref Mau_HandledGroup, @ref Mau_ChannelMap |
| Channel configuration | @ref Mau_FileHandler, @ref Mau_EnumConverter |
| Backend access and communication errors | @ref mau::GetChannelInfo, @ref mau::DefaultOnBoardCommError, @ref mau::RetryWriteOnBoardCommError, @ref mau::ClearBoardCommErrorStatus |
| Driver Station data and snapshots | @ref Mau_DriveData, @ref Mau_SharedJoystick |
| Driver Station communication | @ref mau::comms namespace — protocol threads, packet handling and robot status |
| Bounded packet reading | @ref mau::comms::PacketReader |
| TCP frame reassembly | @ref mau::comms::TcpPacketBuffer |
| VMX time | @ref mau::vmxGetTime; timing helpers in `MauClockInternal.h` |
| VMX AHRS bridge | `HAL_Mau_AHRS_*` functions in `navX/include/AHRS_Mau.h` |
| VMX-specific errors | `MAU_*` constants in `MauErrors.h` |

Bundled RapidJSON and CAN frame libraries and proprietary Studica SDK headers
are excluded. SDK types in signatures are external dependencies and do not
acquire their own API pages here.

## Guides and source

- [VMX on WPI guides](/vmxonwpi/)
- [한국어 안내](/ko/vmxonwpi/)
- [Hardware support](/vmxonwpi/guides/vmx-pi/hardware-support/)
- [VMX backend source](https://github.com/VMXONWPI/allwpilib/tree/7a10d27fe5bb3291e9a8fc62db0e3d400982d530/hal/src/main/native/mau)
- [VMX HAL implementation notes](https://github.com/VMXONWPI/allwpilib/blob/7a10d27fe5bb3291e9a8fc62db0e3d400982d530/vmx/README.md)
