---
title: 로봇 코딩 시작하기
---

WPILib VS Code에서 일반 **WPILib 2026 C++ 또는 Java** 로봇 프로젝트를 만들고, [VMX2026 확장 프로그램](vscode-setup.md)으로 VMX-pi에 연결하세요. 로봇 동작 코드는 프로젝트에 작성하고, 확장 프로그램은 VMX-pi 대상의 빌드·배포 설정을 구성합니다.

## 빌드 및 배포

프로젝트 폴더에서 다음을 실행합니다.

```sh
./gradlew build
./gradlew deploy -PteamNumber=1234
```

`1234`를 FRC 팀 번호로 바꾸세요. GradleRIO가 유선 또는 팀 번호 기반 Wi-Fi 주소로 로봇에 연결하고 `robot_manager`를 중지한 뒤 프로그램과 런타임 라이브러리를 올리고 서비스를 다시 시작합니다. 서비스는 배포된 `robotCommand`를 실행하고 예기치 않게 종료되면 다시 실행합니다.

Java 프로젝트는 로봇에 Java 17이 필요합니다. C++ 프로젝트는 로봇 이미지에 Studica VMX HAL 공유 라이브러리가 있어야 합니다. [VMX-Pi 설정](vmx-pi-setup.md)을 참고하세요.

## WPILib API 사용

2026 프로젝트 템플릿의 표준 WPILib 클래스(`TimedRobot`, `DigitalInput`, `Encoder`, `AnalogInput`, `PWM`, `OnboardIMU` 등)를 사용하고 [하드웨어 지원 안내](hardware-support.md)를 확인하세요. VMX-pi HAL이 VMX 연결을 관리하므로 프로젝트에 다른 HAL을 설치하거나 복사하지 마세요.

WPILib API에서 제공하지 않는 기능이 필요하면 C++에서 Studica VMX SDK를 직접 사용할 수 있습니다. SDK는 로봇의 `vmxpi-hal` 패키지가 제공합니다. SDK 가져오기 작업과 CMake/Gradle 설정은 [GradleRIO VMX-pi 안내](https://github.com/VMXONWPI/GradleRIO/blob/main/VMX.md)를 참고하세요.

## 로봇 로그

로봇 매니저는 서비스 출력을 systemd와 `/home/lvuser/FRC_UserProgram.log`에 기록합니다.

```sh
sudo journalctl -u robot_manager -f
```

프로젝트 연결과 배포 세부 사항은 [프로젝트를 VMX-Pi에 연결](vmx2026-setup.md)을 참고하세요.
