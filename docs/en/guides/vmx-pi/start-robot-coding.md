---
title: Start Robot Coding
---

This page covers the C++ code that uses the VMX-Pi and Studica libraries. Set the project to the VMX target first, as described in [Adding W4Studica Libraries](adding-w4studica-libraries.md). To use WPILib classes such as `DigitalInput`, `Encoder`, `AnalogInput`, `PWM` or `OnboardIMU`, connect their channels to VMX channels first: see [Hardware Support](hardware-support.md).

## Include the Studica headers

The VMX project setup provides these headers. Include the ones used by your robot code:

```cpp
#include "titan.hpp"
#include "wpi/halsim/vmx/ControlLoopWatchdog.hpp"
#include "wpi/halsim/vmx/SharedVMX.hpp"
#include "wpi/halsim/vmx/StudicaTitan.hpp"
#include "wpi/halsim/vmx/TitanEnableGuard.hpp"
```

## Use the shared VMX connection

Pass `wpilibvmx::SharedVMX()` when constructing Studica driver objects. This gives robot code and the VMX HAL the same VMX connection.

For a Titan, use `wpilibvmx::StudicaTitan` with `wpilibvmx::TitanEnableGuard`. The guard follows the Driver Station enabled and E-stop state and disables the Titan when the robot is disabled or the program stops. It does not send motor speed commands; your robot code must continue sending those while enabled. Do not call `studica_driver::Titan::Enable()` directly for enable-state handling.

## Stop the Titan when the program or the Driver Station stalls

The guard reads the cached enabled state. If your main loop hangs or Driver Station updates stop arriving, that state can stay "enabled" and the guard keeps the Titan enabled. Add `wpilibvmx::ControlLoopWatchdog` to cover both cases:

```cpp
using namespace std::chrono_literals;
wpilibvmx::ControlLoopWatchdog watchdog{100ms, 150ms};  // control loop, Driver Station: tune for your robot
using Guard = wpilibvmx::TitanEnableGuard<wpilibvmx::StudicaTitan>;
Guard guard{switcher, [&] { return Guard::HalEnabled() && watchdog.IsFresh(); }};
guard.Start();

// After each completed control cycle:      watchdog.FeedControlLoop();
// After each new valid Driver Station packet: watchdog.FeedDriverStation();
```

The watchdog starts disabled until both have been fed once. Feed it only from the real events, never from a timer or from the guard. Create it before the guard so it outlives the guard. The deadlines above are examples; the stop time on a real robot has not been measured yet.

For classes and methods, see the [C++ API reference](https://wsuser1101.github.io/apidocs/).

See the [complete VMX C++ example](https://github.com/W4Studica/GradleRIO/tree/main/examples/vmx-cpp) for object initialization, periodic motor commands, and Driver Station handling.

For offline dependency setup, return to [Adding W4Studica Libraries](adding-w4studica-libraries.md).
