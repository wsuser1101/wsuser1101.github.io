---
title: 로봇 코딩 시작하기
---

이 페이지에서는 VMX-Pi 및 Studica 라이브러리를 사용하는 C++ 코드를 설명합니다. 먼저 [W4Studica 라이브러리 추가](adding-w4studica-libraries.md)의 안내대로 프로젝트 배포 대상을 VMX로 설정하세요. `DigitalInput`, `Encoder`, `AnalogInput`, `PWM`, `OnboardIMU` 같은 WPILib 클래스를 쓰려면 먼저 채널을 VMX 채널에 연결해야 합니다. [하드웨어 지원](hardware-support.md)을 참고하세요.

## Studica 헤더 포함하기

VMX 프로젝트 구성에서 다음 헤더를 사용할 수 있습니다. 로봇 코드에서 사용하는 헤더를 포함하세요.

```cpp
#include "titan.hpp"
#include "wpi/halsim/vmx/ControlLoopWatchdog.hpp"
#include "wpi/halsim/vmx/SharedVMX.hpp"
#include "wpi/halsim/vmx/StudicaTitan.hpp"
#include "wpi/halsim/vmx/TitanEnableGuard.hpp"
```

## VMX 연결 공유하기

Studica 드라이버 객체를 만들 때 `wpilibvmx::SharedVMX()`를 전달하세요. 로봇 코드와 VMX HAL이 같은 VMX 연결을 사용합니다.

Titan에는 `wpilibvmx::StudicaTitan`과 `wpilibvmx::TitanEnableGuard`를 사용하세요. Guard는 Driver Station의 활성 및 E-stop 상태를 따르며 로봇이 비활성화되거나 프로그램이 종료될 때 Titan을 비활성화합니다. 모터 속도 명령은 보내지 않으므로 활성 상태에서 로봇 코드가 계속 명령해야 합니다. 활성 상태 처리를 위해 `studica_driver::Titan::Enable()`을 직접 호출하지 마세요.

## 프로그램이나 Driver Station이 멈췄을 때 Titan 멈추기

Guard는 캐시된 활성 상태만 읽습니다. 메인 루프가 멈추거나 Driver Station 갱신이 끊겨도 그 상태가 "활성"으로 남을 수 있고, 그러면 Guard가 Titan을 계속 활성 상태로 유지합니다. 두 경우를 모두 막으려면 `wpilibvmx::ControlLoopWatchdog`를 추가하세요.

```cpp
using namespace std::chrono_literals;
wpilibvmx::ControlLoopWatchdog watchdog{100ms, 150ms};  // 제어 루프, Driver Station: 로봇에 맞게 조정
using Guard = wpilibvmx::TitanEnableGuard<wpilibvmx::StudicaTitan>;
Guard guard{switcher, [&] { return Guard::HalEnabled() && watchdog.IsFresh(); }};
guard.Start();

// 제어 주기를 끝까지 마칠 때마다:            watchdog.FeedControlLoop();
// 유효한 Driver Station 패킷을 새로 받을 때마다: watchdog.FeedDriverStation();
```

두 신호가 한 번씩 들어오기 전까지 워치독은 비활성 상태입니다. 타이머나 Guard가 아니라 실제 이벤트에서만 호출하세요. Guard보다 먼저 만들어 Guard보다 오래 살아 있게 하세요. 위 시간은 예시이며, 실제 로봇에서 정지까지 걸리는 시간은 아직 측정하지 않았습니다.

클래스와 메서드는 [C++ API 문서](https://wsuser1101.github.io/apidocs/)를 참고하세요.

객체 초기화, 주기적인 모터 명령, Driver Station 처리는 [VMX C++ 전체 예제](https://github.com/W4Studica/GradleRIO/tree/main/examples/vmx-cpp)를 참고하세요.

오프라인 의존성 설정은 [W4Studica 라이브러리 추가](adding-w4studica-libraries.md) 안내를 참고하세요.
