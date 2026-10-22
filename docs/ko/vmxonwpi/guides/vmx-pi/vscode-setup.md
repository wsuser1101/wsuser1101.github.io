---
title: VS Code 설정
---

WPILib 설치 프로그램이 설치한 **WPILib 2026 VS Code**를 사용하세요. VMX2026 `.vsix` 설치 방법은 [WPILib 및 VMX2026 설치](software-install.md)를 참고하세요.

1. WPILib 2026 로봇 프로젝트를 열거나 C++ 또는 Java 프로젝트를 새로 만듭니다.
2. **Ctrl+Shift+P**로 명령 팔레트를 엽니다.
3. **VMX2026: Change the deploy target to VMX-Pi (from RoboRIO)**를 실행합니다.
4. **VMX2026: Update VMX2026 Version**을 실행해 호환되는 GradleRIO와 VMX HAL 릴리스 쌍을 연결합니다.
5. 프로젝트의 Gradle wrapper로 빌드하고 배포합니다.

   ```sh
   ./gradlew build
   ./gradlew deploy -PteamNumber=1234
   ```

   `1234`를 팀 번호로 바꾸세요. 배포 대상은 기본적으로 `ubuntu` 계정을 사용합니다. 로봇 계정 정보가 다르면 `VMX_USER` 또는 `VMX_PASSWORD`를 설정하세요.

확장 프로그램은 배포 대상이 하나인 WPILib 2026 Groovy `build.gradle` 프로젝트를 지원합니다. Kotlin DSL, WPILib 2020 프로젝트, 배포 대상이 여러 개인 프로젝트는 지원하지 않습니다.

## 오프라인 빌드 준비

개발 컴퓨터가 인터넷에 연결된 동안 **VMX2026: Save VMX2026 Offline**을 실행하세요. 의존성을 내려받고 해석한 뒤 온라인 빌드와 강제 오프라인 빌드를 확인합니다. 성공하면 Gradle `--offline` 옵션으로 빌드할 수 있습니다. 의존성·벤더 라이브러리·배포 대상을 변경한 뒤에는 다시 실행하세요.

오프라인 빌드에서 의존성이 캐시에 없다는 오류가 나오면 인터넷에 연결한 뒤 **Save VMX2026 Offline**을 먼저 실행하세요.
