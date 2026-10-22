---
title: WPILib 및 VMX2026 설치
---

## WPILib 2026 설치

개발 컴퓨터의 운영체제와 CPU에 맞는 공식 **WPILib 2026.2.2** 설치 파일을 내려받아 설치하세요.

[WPILib 2026.2.2 릴리스 및 설치 파일](https://github.com/wpilibsuite/allwpilib/releases/tag/v2026.2.2)

로봇 프로젝트를 만들고 배포할 때는 설치 프로그램이 만든 WPILib VS Code를 사용하세요. 이 절차에서는 2027 W4Studica 프로젝트나 확장 프로그램을 사용하지 않습니다.

## VMX2026 확장 프로그램 설치

VMX2026 확장 프로그램 릴리스 페이지에서 최신 `.vsix` 파일을 내려받으세요. 현재 릴리스는 **2.0.3**입니다.

[VMX2026 확장 프로그램 릴리스](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases)

WPILib VS Code에서 **Extensions**를 열고 `…` 메뉴에서 **Install from VSIX…**를 선택한 뒤 내려받은 파일을 엽니다. VS Code가 다시 시작을 요청하면 재시작하세요.

## 로봇에 설치할 소프트웨어

VMX-pi에는 64비트 Ubuntu 24.04 또는 26.04, Studica `vmxpi-hal` 패키지, VMX Robot Manager 서비스가 필요합니다. Java 로봇 프로그램은 로봇에 Java 17도 설치해야 합니다.

```sh
sudo apt install openjdk-17-jre-headless
```

로봇 요구 사항은 [VMX-Pi 설정](vmx-pi-setup.md)을, 패키지 설치는 [Robot Manager 저장소](https://github.com/VMXONWPI/wpi-robot-manager)를 참고하세요.
