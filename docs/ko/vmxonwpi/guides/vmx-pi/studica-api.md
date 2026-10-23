---
title: Studica API 사용법
---

VMX on WPI의 Studica 호환 구현은 기존 C++ `studica` 네임스페이스와 Java
`com.studica.frc` 패키지의 클래스명·메서드를 유지합니다. 일반 WPILib API는
계속 `frc` / `frc2` 또는 `edu.wpi.first.wpilibj`를 사용합니다.

!!! info "allwpilib 2026.2.2-vmx.6부터 제공"
    VMX2026 확장 프로그램 **2.0.7 이상**을 설치하고 **Update VMX2026 Version**을 실행하세요.
    VMX 대상에 일치하는 wpilibc, wpilibj, HAL, HAL JNI를 자동으로 선택합니다.
    GradleRIO는 **2026.2.2-vmx.2**를 사용합니다. 이전 Titan 벤더 의존성은 제거하세요.
    커스텀 네이티브 라이브러리는 linuxarm64용이며, 새 클래스를 사용하는 데스크톱
    C++ 시뮬레이션에는 별도 플랫폼 빌드가 필요합니다.

[고정된 구현 소스](https://github.com/VMXONWPI/allwpilib/tree/df7e6760001e16edba5d2dc44a06329f0961c5f2/vmx/studica)
· [커스텀 빌드 및 프로젝트 버전 설정](https://github.com/VMXONWPI/allwpilib/blob/df7e6760001e16edba5d2dc44a06329f0961c5f2/vmx/studica/README.md#build-and-distribution)

## 제공하는 클래스

| 클래스 | 기능 | C++ API | Java API |
|---|---|---|---|
| `TitanQuad` | CAN ID 1~63, 모터 채널 0~3, 속도·반전·리미트 스위치·상태 조회 | [TitanQuad](/vmxonwpi/apidocs/classstudica_1_1TitanQuad.html) | [TitanQuad](/vmxonwpi/javadocs/com/studica/frc/TitanQuad.html) |
| `TitanQuadEncoder` | 엔코더 카운트·초기화·거리·방향·RPM 조회 | [TitanQuadEncoder](/vmxonwpi/apidocs/classstudica_1_1TitanQuadEncoder.html) | [TitanQuadEncoder](/vmxonwpi/javadocs/com/studica/frc/TitanQuadEncoder.html) |
| `Cobra` | MXP I2C `0x48`의 ADS1015, 아날로그 채널 0~3 | [Cobra](/vmxonwpi/apidocs/classstudica_1_1Cobra.html) | [Cobra](/vmxonwpi/javadocs/com/studica/frc/Cobra.html) |
| `Servo` | 0~300도 위치 제어, 500~2500 μs PWM | [Servo](/vmxonwpi/apidocs/classstudica_1_1Servo.html) | [Servo](/vmxonwpi/javadocs/com/studica/frc/Servo.html) |
| `ServoContinuous` | 연속 회전 서보, 1500 μs 중립 | [ServoContinuous](/vmxonwpi/apidocs/classstudica_1_1ServoContinuous.html) | [ServoContinuous](/vmxonwpi/javadocs/com/studica/frc/ServoContinuous.html) |
| `Lidar` | 원래 Studica 360도 모델, 각도·거리 360개 | [Lidar](/vmxonwpi/apidocs/classstudica_1_1Lidar.html) | [Lidar](/vmxonwpi/javadocs/com/studica/frc/Lidar.html) |

## 프로젝트 준비

1. 개발 컴퓨터에 [WPILib 2026과 VMX2026](software-install.md)을 준비하고 프로젝트의 배포 대상을 [VMX-pi로 설정](vmx2026-setup.md)합니다.
2. VMX2026 **2.0.7 이상**에서 **Update VMX2026 Version**을 실행해 allwpilib **2026.2.2-vmx.6**을 선택합니다. 로봇용 네이티브 대상은 `linuxarm64`입니다.
3. 이전 Titan 1.1.8 벤더 의존성은 제거하고 프로젝트를 다시 빌드합니다. 이전 JAR·네이티브 라이브러리와 새 클래스를 함께 추가하지 마세요.

클래스는 이 포크의 wpilibc와 wpilibj에 포함됩니다. 별도의 기존 `TitanDriver`
JNI 라이브러리를 로드하지 않습니다. Java SerialPort의 새 DTR 기능에는 같은
빌드의 HAL JNI가 필요하므로 이전 HAL JNI를 혼용하지 마세요.

## C++

기존 헤더 경로와 대문자로 시작하는 메서드를 사용합니다. 다음은 활성화된
Teleop 주기에서 모터 출력을 갱신하는 예입니다.

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

`42`는 Titan CAN ID, `15600`은 모터 PWM 주파수(Hz), `0`은 모터 채널입니다.
`0.001`은 엔코더 한 틱당 거리이며 `GetEncoderDistance()`의 단위를 결정합니다.

## Java

기존 패키지와 소문자로 시작하는 메서드를 사용합니다.

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

Java의 원본 1.1.8 JAR와 여섯 클래스의 공개 메서드 시그니처를 대조했습니다.
이는 소스 API 호환이며, 이전 2020 바이너리나 `com.studica.frc.jni` 구현
클래스를 그대로 교체해 로드하는 방식은 아닙니다.

## Titan과 엔코더 동작

- 같은 CAN ID의 네 모터는 하나의 장치와 HAL 통신을 공유합니다. 같은 모터 채널을 중복 할당할 수 없습니다.
- Driver Station이 연결되어 활성화되고 E-stop이 아닐 때만 새 모터 명령을 받습니다. `Set()` / `set()`은 100 ms 이내에 갱신하세요.
- 비활성화·연결 해제·E-stop·명령 시간 초과 시 명령을 지웁니다. 다시 활성화해도 이전의 0이 아닌 출력이 재생되지 않습니다.
- 엔코더 거리는 부호 있는 카운트 × 한 틱당 거리입니다. `GetSpeed()` / `getSpeed()`의 단위는 거리/초가 아닌 축 RPM입니다.
- 엔코더 주기는 관측한 카운트 변화에서 계산하며 하드웨어에서 직접 캡처한 에지 시각은 아닙니다. C++의 기존 `double GetPeriod()`를 유지하고 Java는 `CounterBase`를 구현합니다.
- 누락·잘린 응답은 유효한 0으로 처리하지 않고 예외를 발생시킵니다. CAN 전송 오류로 잠긴 장치는 객체를 다시 만들어야 합니다.

## Lidar 모델과 데이터

원래 Studica 360도 **비강도 삼각측량 모델**을 대상으로 합니다. 기본 속도는
128000 baud이며 새로운 T-Mini·ToF·강도 데이터 형식과는 호환되지 않습니다.
동일한 패킷 형식에서 전송 속도만 바꾸려면 두 번째 생성자 인수를 사용합니다.

C++는 `Lidar::kUSB1` / `kUSB2`로 열고 `GetData()` 호출 후 공개 배열
`angle[360]`, `distance[360]`에서 읽습니다. Java는 `Lidar.Port.kUSB1` /
`kUSB2`로 열고 `getData(float[], float[])`로 각각 길이 360 이상인 별도 배열을
채웁니다. 위 USB2 포트가 `kUSB1`, 아래 USB2 포트가 `kUSB2`입니다.

거리는 mm, 각도는 도 단위이며 측정되지 않은 방향의 거리는 `NaN`입니다.
체크섬과 패킷 경계를 확인하고 한 스캔을 1초 안에 받지 못하면 예외를 발생시킵니다.

## 검증 범위

ARM64 C++ 공유 라이브러리·HAL JNI 링크, Java JAR 생성, 원본 Java API 대조,
호스트 회귀 테스트와 C++ ASan/UBSan 검사를 수행했습니다. 실제 VMX-pi에서의
모터 정지·센서 값·펌웨어 차이·USB 어댑터의 DTR 극성과 Lidar 모델 설정은
아직 검증하지 않았습니다. [하드웨어 지원](hardware-support.md)도 확인하세요.
