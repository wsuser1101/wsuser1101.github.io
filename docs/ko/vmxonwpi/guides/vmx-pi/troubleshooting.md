---
title: 문제 해결
---

## Gradle 오프라인 모드에서 의존성을 캐시하지 않았다고 나옵니다

`--offline`은 프로젝트의 모든 의존성을 Gradle이 내려받은 뒤에만 작동합니다. 개발 컴퓨터를 인터넷에 연결하고 WPILib VS Code에서 **VMX2026: Save VMX2026 Offline**을 실행하세요. 오프라인으로 배포하기 전에 온라인 의존성 확인, 빌드, 오프라인 검증이 끝날 때까지 기다리세요. [VS Code 설정](vscode-setup.md)을 참고하세요.

## 배포 중 SFTP `No such file` 오류가 납니다

현재 [VMX2026 확장 프로그램 릴리스](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases)(2.0.3 이상)를 설치하세요. 이전 버전은 RoboRIO 경로인 `/home/lvuser/deploy`를 VMX 프로젝트에 남길 수 있었습니다. VMX 대상은 설정된 로그인 계정의 홈 디렉터리, 기본값 `/home/ubuntu/deploy`에 정적 파일을 배포해야 합니다.

## `robot_manager`가 실행 중이 아닙니다

로봇에서 서비스를 확인하고 다시 시작합니다.

```sh
sudo systemctl status robot_manager --no-pager
sudo systemctl restart robot_manager
sudo journalctl -u robot_manager -n 100 --no-pager
```

서비스 파일이 없다면 [wpi-robot-manager 저장소](https://github.com/VMXONWPI/wpi-robot-manager)에서 VMX Robot Manager 패키지를 설치하세요. 배포된 `/home/ubuntu/robotCommand` 파일이 있고 실행 가능한지도 확인하세요.

## SSH 또는 배포에서 로봇에 연결할 수 없습니다

개발 컴퓨터가 로봇 핫스팟이나 같은 공유기에 연결되었는지 확인하세요. 유선으로 직접 연결하면 PC의 유선 네트워크가 DHCP를 사용하는지 확인합니다. 로봇 유선 주소는 `172.22.11.2`, 핫스팟 주소는 `10.TE.AM.2`입니다. [VMX-Pi 네트워크](vmx-pi-network.md)를 참고하세요.

## Java 프로그램이 시작되지 않습니다

VMX-pi에 Java 17 런타임을 설치하세요.

```sh
sudo apt install openjdk-17-jre-headless
```

## C++ 코드에서 `VMXPi.h`를 찾을 수 없습니다

일반 WPILib 코드는 `VMXPi.h`를 직접 포함할 필요가 없습니다. C++ 코드에서 Studica SDK를 직접 사용하는 경우 로봇에 `vmxpi-hal` 패키지가 있어야 합니다. SDK 가져오기 방법은 [GradleRIO VMX-pi 안내](https://github.com/VMXONWPI/GradleRIO/blob/main/VMX.md)를 참고하세요.

## 프로그램 출력이나 로봇 로그를 볼 수 없습니다

```sh
sudo journalctl -u robot_manager -f
```

서비스는 `/home/lvuser/FRC_UserProgram.log`에도 기록합니다. 두 로그가 모두 갱신되지 않으면 먼저 `robot_manager` 상태를 확인하세요.
