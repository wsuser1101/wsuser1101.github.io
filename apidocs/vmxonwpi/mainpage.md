# VMX on WPI C++ API

**WPILib APIs with VMX implementations · Studica 1.1.8 compatibility**

The Studica classes below are included in **allwpilib 2026.2.2-vmx.3**.
Install **VMX2026 extension 2.0.4 or later** and run **Update VMX2026 Version**
to select matching wpilibc, wpilibj, HAL and HAL JNI with GradleRIO 2026.2.2-vmx.2.
Remove the old Titan vendor dependency. Native Studica artifacts target
linuxarm64; desktop C++ simulation with these classes needs a separate build.
See the [Studica API setup guide](/vmxonwpi/guides/vmx-pi/studica-api/)
for C++ / Java examples and hardware verification limits.

This reference covers both **standard WPILib hardware APIs implemented by the
VMX-pi port** and **VMX-specific interfaces added by the port**. An API does not
need a new name or declaration to be included: standard WPILib classes and HAL
functions with a VMX implementation belong here too.

Use **Classes**, **Namespaces**, **Files**, or search to find an interface.

## Studica device APIs

The original C++ `studica` namespace and `#include <studica/...>` paths are
retained. Java uses `com.studica.frc`; see the [Java API reference](/vmxonwpi/javadocs/)
and [Java usage guide](/vmxonwpi/guides/vmx-pi/studica-api/#java).

| Device | C++ reference | Notes |
| --- | --- | --- |
| Titan Quad motor | @ref studica::TitanQuad | CAN ID 1..63; motor channel 0..3; shares the existing HAL transport |
| Titan Quad encoder | @ref studica::TitanQuadEncoder | Signed counts, distance scaling, direction and shaft RPM |
| Cobra ADC | @ref studica::Cobra | Four ADS1015 channels on MXP I2C, address 0x48 |
| Positional servo | @ref studica::Servo | 0..300 degrees, 500..2500 microsecond PWM |
| Continuous servo | @ref studica::ServoContinuous | PWM motor interface with 1500 microsecond neutral |
| Original Studica 360-degree LiDAR | @ref studica::Lidar | Non-intensity triangle protocol; 360 rays; distance in mm |

Titan Set calls require an attached, enabled Driver Station without E-stop.
Refresh commands within 100 ms; disabled or expired commands are cleared.
C++ and Java use the same CAN protocol. Java's old TitanDriver JNI library is
not required. The legacy public Java method signatures have been checked against
the original 1.1.8 JAR. Hardware tests remain required; host tests do not validate
physical motor, sensor or USB adapter behavior.

C++ TitanQuadEncoder retains its double-valued period methods instead of the
2026 CounterBase's units-valued methods. Java still implements CounterBase.
The old SendableBuilder package/header and Titan SpeedController interface
have source adapters. These are source-compatible APIs; recompile instead of
loading the old 2020 binaries alongside the new classes.

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
- [VMX backend source](https://github.com/VMXONWPI/allwpilib/tree/df7e6760001e16edba5d2dc44a06329f0961c5f2/hal/src/main/native/mau)
- [VMX HAL implementation notes](https://github.com/VMXONWPI/allwpilib/blob/df7e6760001e16edba5d2dc44a06329f0961c5f2/vmx/README.md)
