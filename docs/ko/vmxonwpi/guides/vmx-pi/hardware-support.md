---
title: 하드웨어 지원
---

VMX on WPI는 VMX-pi용 WPILib 2026 HAL 백엔드를 사용합니다. 지원되는 `linuxarm64` 대상에서 WPILib 클래스를 사용할 수 있습니다. C++와 Java 로봇 프로그램을 지원하며 Java는 로봇에 Java 17이 필요합니다.

| 영역 | 지원 내용 |
|---|---|
| Driver Station | WPILib Driver Station 프로토콜을 사용합니다. Driver Station이 연결되어 활성화되기 전까지 로봇 출력은 비활성 상태입니다. |
| 디지털 입출력, 아날로그, 엔코더, PWM | Studica VMX 라이브러리를 사용해 VMX-pi HAL에서 구현합니다. 배선 전에 보드와 SDK의 채널 안내를 확인하세요. |
| I2C 및 수동 SPI | HAL 백엔드에서 지원합니다. 현재 VMX SDK는 자동 SPI 전송을 지원하지 않습니다. |
| 아날로그 트리거 | 원시 아날로그 트리거를 지원합니다. 평균 및 필터 아날로그 트리거는 현재 VMX SDK에서 지원하지 않습니다. |
| DMA, DutyCycle, 라디오 LED, 사용자 전원 레일 | VMX-pi HAL 백엔드에서 사용할 수 없습니다. 지원하지 않는 동작은 오류를 반환하거나 WPILib이 정의한 무동작으로 처리됩니다. |
| VMX 네이티브 라이브러리 | Studica의 `libvmxpi_hal_cpp.so`는 로봇 이미지/패키지에서 제공하며 VMX2026 릴리스 아카이브에는 포함하지 않습니다. |

HAL에는 호스트 회귀 테스트가 있지만 실제 VMX-pi, 센서, 모터 컨트롤러, Driver Station 시험을 대신하지 않습니다. 로봇에서 사용하기 전에 각 입출력과 안전 동작을 실제 하드웨어에서 확인하세요.

자세한 내용은 [VMX HAL 구현 안내](https://github.com/VMXONWPI/allwpilib/blob/main/vmx/README.md)와 [GradleRIO VMX-pi 배포 안내](https://github.com/VMXONWPI/GradleRIO/blob/main/VMX.md)를 참고하세요.

## Studica 장치 클래스

개발 소스의 wpilibc / wpilibj에는 TitanQuad, TitanQuadEncoder, Cobra, Servo,
ServoContinuous, 원래 Studica 360도 Lidar 구현이 추가되어 있습니다.
현재 확장 프로그램 릴리스에는 아직 포함되지 않았습니다.
지원 모델, 일치하는 라이브러리, C++·Java 예제와 하드웨어 검증 범위는
[Studica API 사용법](studica-api.md)을 참고하세요.
