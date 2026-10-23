---
title: Studica APIs
---

The Studica compatibility implementation retains the C++ `studica` namespace,
Java `com.studica.frc` package, class names and methods. Standard WPILib APIs
continue to use `frc` / `frc2` or `edu.wpi.first.wpilibj`.

!!! info "Development-source additions"
    These Studica classes are not yet included in the published `2026.2.2-vmx.2`
    release or the current VMX2026 extension. Build matching custom wpilibc,
    wpilibj, HAL and HAL JNI libraries from the development source. Installing
    the existing extension alone does not add these classes.

[Pinned implementation source](https://github.com/VMXONWPI/allwpilib/tree/45be4e5c8ef3e6a97a8df2377e2b42c967de7201/vmx/studica)
· [Custom build and project version setup](https://github.com/VMXONWPI/allwpilib/blob/45be4e5c8ef3e6a97a8df2377e2b42c967de7201/vmx/studica/README.md#build-and-distribution)

## Available classes

| Class | Function | C++ API |
|---|---|---|
| `TitanQuad` | CAN ID 1..63, motor channel 0..3, speed, inversion, limit switches and status | [TitanQuad](/vmxonwpi/apidocs/classstudica_1_1TitanQuad.html) |
| `TitanQuadEncoder` | Signed counts, reset, distance, direction and RPM | [TitanQuadEncoder](/vmxonwpi/apidocs/classstudica_1_1TitanQuadEncoder.html) |
| `Cobra` | ADS1015 at MXP I2C address `0x48`, channels 0..3 | [Cobra](/vmxonwpi/apidocs/classstudica_1_1Cobra.html) |
| `Servo` | 0..300 degrees, 500..2500 microsecond PWM | [Servo](/vmxonwpi/apidocs/classstudica_1_1Servo.html) |
| `ServoContinuous` | Continuous-rotation servo, 1500 microsecond neutral | [ServoContinuous](/vmxonwpi/apidocs/classstudica_1_1ServoContinuous.html) |
| `Lidar` | Original Studica 360-degree model, 360 angle/distance entries | [Lidar](/vmxonwpi/apidocs/classstudica_1_1Lidar.html) |

## Prepare the project

1. Install [WPILib 2026 and VMX2026](software-install.md) and [select the VMX-pi deploy target](vmx2026-setup.md).
2. Follow the implementation's build guide to prepare matching custom wpilibc, wpilibj, HAL and HAL JNI libraries and select their versions in the project. Robot native code targets `linuxarm64`.
3. Remove the old Titan 1.1.8 vendor dependency and rebuild. Do not add the old JAR or native library alongside the new classes.

The classes are part of this fork's wpilibc and wpilibj. They do not load the
old TitanDriver JNI library. The new Java SerialPort DTR method requires the
matching HAL JNI; do not combine it with an older HAL JNI.

## C++

Keep the original include paths and capitalized methods. This example refreshes
motor output during enabled Teleop periods.

```cpp
#include <frc/TimedRobot.h>
#include <studica/TitanQuad.h>
#include <studica/TitanQuadEncoder.h>

class Robot : public frc::TimedRobot {
 public:
  void TeleopPeriodic() override {
    m_motor.Set(0.25);
  }

  void DisabledInit() override {
    m_motor.StopMotor();
  }

 private:
  studica::TitanQuad m_motor{42, 15600, 0};
  studica::TitanQuadEncoder m_encoder{m_motor, 0, 0.001};
};
```

`42` is the Titan CAN ID, `15600` is the motor PWM frequency in Hz, and `0` is
the motor channel. `0.001` is distance per encoder tick and determines the units
returned by `GetEncoderDistance()`.

## Java

Keep the original package and lower-camel-case methods.

```java
import com.studica.frc.TitanQuad;
import com.studica.frc.TitanQuadEncoder;
import edu.wpi.first.wpilibj.TimedRobot;

public class Robot extends TimedRobot {
  private final TitanQuad motor = new TitanQuad(42, 15600, 0);
  private final TitanQuadEncoder encoder =
      new TitanQuadEncoder(motor, 0, 0.001);

  @Override
  public void teleopPeriodic() {
    motor.set(0.25);
  }

  @Override
  public void disabledInit() {
    motor.stopMotor();
  }

  @Override
  public void close() {
    try {
      motor.close();
    } finally {
      super.close();
    }
  }
}
```

The public method signatures of all six Java classes were checked against the
original 1.1.8 JAR. This is source API compatibility; recompile instead of loading
the original 2020 binaries or relying on their `com.studica.frc.jni` internals.

## Titan and encoder behavior

- All four motors on one CAN ID share a device and the existing HAL transport. A motor channel cannot be allocated twice.
- Motor commands require a Driver Station that is attached, enabled and not E-stopped. Refresh `Set()` / `set()` within 100 ms.
- Disable, disconnect, E-stop and command expiry clear old commands. Re-enabling cannot replay an old nonzero output.
- Encoder distance is signed count × distance per tick. `GetSpeed()` / `getSpeed()` report shaft RPM, not linear distance per second.
- Encoder period is inferred from observed count changes, not hardware-captured edge timestamps. C++ retains its legacy `double GetPeriod()`; Java implements `CounterBase`.
- Missing or truncated telemetry throws instead of reporting valid zero. A latched CAN write fault requires recreating the device objects.

## LiDAR model and data

The implementation targets the **original non-intensity triangulation Studica
360-degree model** at 128000 baud. Newer T-Mini, ToF and intensity packet formats
are not interchangeable. A second constructor argument changes the baud rate
for the same packet format.

C++ opens `Lidar::kUSB1` / `kUSB2` and fills the public `angle[360]` and
`distance[360]` arrays on `GetData()`. Java opens `Lidar.Port.kUSB1` / `kUSB2`
and fills two separate arrays of at least 360 floats with `getData(float[], float[])`.
The upper USB2 port is `kUSB1`; the lower USB2 port is `kUSB2`.

Distance is in millimeters and angle is in degrees. Missing distances are `NaN`.
The reader checks packet boundaries and checksums and throws if a scan is not
received within one second.

## Verification scope

ARM64 C++ shared-library and HAL JNI linking, Java JAR creation, original Java
API comparison, host regression tests and C++ ASan/UBSan checks have passed.
Physical motor stopping, sensor values, firmware differences, USB DTR polarity
and LiDAR model settings have not yet been verified on a VMX-pi.
Also review [hardware support](hardware-support.md).
