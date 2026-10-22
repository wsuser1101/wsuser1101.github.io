---
title: 프로젝트를 VMX-Pi에 연결
---

VMX2026 확장 프로그램은 GradleRIO 배포 대상을 바꾸고 호환되는 VMX HAL을 선택합니다. HAL 파일을 직접 복사하거나 `build.gradle`에 W4Studica 라이브러리를 수동으로 추가할 필요가 없습니다.

## 프로젝트 연결

WPILib VS Code에서 WPILib 2026 Groovy 프로젝트를 열고 다음 순서로 진행하세요.

1. **VMX2026: Change the deploy target to VMX-Pi (from RoboRIO)**를 실행합니다.
2. **VMX2026: Update VMX2026 Version**을 실행합니다. 확장 프로그램이 GradleRIO와 VMX HAL의 호환 릴리스 쌍을 내려받고 검증합니다.
3. `build.gradle`에서 배포 대상이 `VmxPi`, 플랫폼이 `linuxarm64`인지 확인합니다.
4. WPILib 설정에서 팀 번호를 지정하거나 Gradle에 `-PteamNumber=1234`를 전달합니다.
5. `./gradlew build`로 빌드하고 `./gradlew deploy -PteamNumber=1234`로 배포합니다.

배포는 SSH/SFTP로 로봇에 접속합니다. 기본 계정과 비밀번호는 `ubuntu`와 `password`입니다. 로봇의 비밀번호를 변경하고 사용할 네트워크에 맞게 계정을 설정하세요.

## C++와 Java

VMX-pi 배포 대상은 C++와 Java 프로젝트를 지원합니다. C++ 프로그램은 `linuxarm64`용 VMX HAL을 사용하므로 로봇 이미지에 Studica `vmxpi-hal` 공유 라이브러리가 있어야 합니다. Java 프로젝트는 로봇에 Java 17 런타임도 필요합니다.

```sh
sudo apt install openjdk-17-jre-headless
```

예제는 [GradleRIO C++ 프로젝트](https://github.com/VMXONWPI/GradleRIO/tree/main/examples/vmx-cpp)와 [Java 프로젝트](https://github.com/VMXONWPI/GradleRIO/tree/main/examples/vmx-java)를 참고하세요.

## 오프라인 의존성

Gradle `--offline`을 사용하기 전에 인터넷에 연결된 상태에서 **VMX2026: Save VMX2026 Offline**을 실행하세요. 프로젝트 의존성과 오프라인 빌드를 확인합니다. 의존성을 바꾸거나 배포 대상을 전환한 뒤에는 다시 오프라인 준비를 하세요.
