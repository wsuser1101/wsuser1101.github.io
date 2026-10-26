---
title: 하드웨어 지원
---

이 페이지는 로봇 코드가 WPILib 클래스로 사용할 수 있는 VMX-pi 하드웨어, WPILib 채널 번호를 VMX 채널에 연결하는 방법, 실제 로봇에서 확인한 범위를 정리합니다.

## WPILib 클래스로 사용할 수 있는 것

| WPILib 클래스 | VMX 하드웨어 | 설정 | 상태 |
|---|---|---|---|
| `DigitalInput`, `DigitalOutput` | FlexDIO, HiCurrDIO(출력만), CommDIO | `HALSIMVMX_DIO_MAP` | VMX-pi에서 확인 |
| `AnalogInput` | AnalogIn | `HALSIMVMX_ANALOG_MAP` | VMX-pi에서 확인 |
| `Encoder` | FlexDIO 쌍 | `HALSIMVMX_DIO_MAP`(두 채널 모두) | VMX-pi에서 확인 |
| `OnboardIMU`(`FLAT`으로 사용) | navX: yaw, roll, pitch, 각속도, 가속도 | `HALSIMVMX_IMU` | yaw와 Z축 가속도는 확인. roll, pitch, Z축 각속도의 방향은 아직 확인하지 않음 |
| `PWM`, `Servo`, PWM 모터 컨트롤러 | FlexDIO, HiCurrDIO, CommDIO 26·27 | `HALSIMVMX_PWM_MAP` | Beta 6에 포함, **아직 로봇에서 시험하지 않음** |
| `RobotController` 배터리 전압 | VMX 시스템 전압 | 없음 | Beta 6에 포함, **아직 로봇에서 시험하지 않음** |

WPILib 클래스로는 사용할 수 없는 것:

- **I2C**, **DutyCycle**, **DutyCycleEncoder**. 대신 Studica 클래스를 사용하세요. 예를 들어 I2C 장치인 `Cobra`가 있습니다.
- **인터럽트.** WPILib 2027 alpha 7 HAL에는 인터럽트 API가 없습니다.
- **IMU 쿼터니언.** `OnboardIMU::GetQuaternion()`과 `GetRotation3d()`는 0을 돌려줍니다. 각도로 회전을 직접 만드세요: `wpi::math::Rotation3d{imu.GetAngleX(), imu.GetAngleY(), imu.GetYaw()}`. IMU는 `OnboardIMU::FLAT`으로 만드세요. 다른 장착 방향은 처리하지 않습니다.
- **Java.** 로봇 프로그램은 C++만 지원합니다.

WPILib에 대응하는 클래스가 없는 Studica 장치(`Titan`, `Ultrasonic`, `Sharp`, `Cobra`, `Colore`, `Parsec`, `LightTower`)는 Studica 클래스로 사용합니다. [로봇 코딩 시작하기](start-robot-coding.md)에 설명된 대로 항상 `wpilibvmx::SharedVMX()`를 전달하세요.

## WPILib 채널을 VMX 채널에 연결하기

WPILib 채널 번호는 VMX 채널 번호가 아니므로, 사용하는 채널마다 연결(map)해야 합니다. 프로젝트 `build.gradle`의 `wpilibCpp` 아티팩트에 설정을 추가하세요. VMX-pi에서 프로그램이 실행될 때 환경 변수로 전달됩니다.

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

이 예시는 WPILib DIO 0, 1을 VMX 채널 0, 1에(0, 1에 연결한 `Encoder`도 같습니다), `AnalogInput` 0을 AnalogIn 22에, `PWM` 0을 HiCurrDIO 12에 연결하고, navX를 `OnboardIMU`로 켭니다.

각 항목은 `<WPILib 채널>:<VMX 채널>` 형식이고, 항목은 공백 없이 쉼표로 구분합니다. 연결하지 않은 채널은 무시됩니다. 연결 설정이 없거나, 형식이 잘못되었거나, WPILib 채널 두 개가 VMX 채널 하나에 연결되면 로봇 로그에 알려 줍니다.

`Encoder`는 DIO 채널 두 개를 쓰므로 둘 다 연결하세요. VMX 채널 하나는 한 번에 한 가지 기능만 맡습니다.

### VMX 채널

| 종류 | 채널 | 기능 |
|---|---|---|
| FlexDIO | 0~11 | 디지털 입출력, PWM, 엔코더. 엔코더 쌍은 (0,1) (2,3) (4,5) (6,7) (8,9)이고 A는 짝수, B는 홀수 채널 |
| HiCurrDIO | 12~21 | 디지털 출력과 PWM만 가능 |
| AnalogIn | 22~25 | 아날로그 입력 |
| CommDIO | 26~33 | 26, 27: 디지털 입출력, PWM, I2C. 28~33: UART, SPI |

위 번호는 VMX 채널 인덱스입니다. 보드에 인쇄된 번호와 같은지는 아직 확인하지 않았습니다. 프로그램이 I2C, UART, SPI를 쓰는 동안에는 CommDIO 26~33을 다른 용도로 쓰지 마세요.

전체 설계는 [`DESIGN.md`](https://github.com/W4Studica/allwpilib/blob/main/simulation/halsim_vmx/DESIGN.md), 측정 결과는 [`HARDWARE_CHECKLIST.md`](https://github.com/W4Studica/allwpilib/blob/main/simulation/halsim_vmx/HARDWARE_CHECKLIST.md)에 있습니다.
