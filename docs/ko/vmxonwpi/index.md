---
title: VMX-Pi on WPILib
hide:
  - toc
---

# VMX-Pi on WPILib

**WPILib 2026 · C++ 및 Java**

[C++ API](/vmxonwpi/apidocs/){ .md-button }

VMX-Pi on WPILib은 Studica VMX-pi를 WPILib 2026 개발 흐름에서 사용할 수 있게 합니다. 64비트 Linux용 VMX-pi HAL, GradleRIO `VmxPi` 배포 대상, VMX2026 VS Code 확장 프로그램, NetworkManager 기반 Robot Manager를 제공합니다.

[VMXONWPI](https://github.com/VMXONWPI)의 WPILib 2026 릴리스에 이 안내를 적용하세요.

## 권장 순서

1. [VMX-Pi 이미지를 준비](guides/vmx-pi/vmx-pi-setup.md)합니다.
2. [로봇 네트워크를 설정](guides/vmx-pi/vmx-pi-network.md)합니다.
3. 개발 컴퓨터에 [WPILib 2026 및 VMX2026을 설치](guides/vmx-pi/software-install.md)합니다.
4. [WPILib 프로젝트를 VMX-pi에 연결](guides/vmx-pi/vmx2026-setup.md)하고 배포합니다.
5. 로봇 하드웨어를 연결하기 전에 [하드웨어 지원 범위](guides/vmx-pi/hardware-support.md)를 확인합니다.

WPILib 버전은 2026.2.2입니다. 현재 VMX GradleRIO와 HAL 릴리스 쌍은 2026.2.2-vmx.2입니다. 최신 VSIX는 [VMX2026 확장 프로그램 릴리스](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases)에서 확인하세요.

## Studica 장치 API

개발 소스에 TitanQuad, TitanQuadEncoder, Cobra, Servo, ServoContinuous,
Lidar의 C++·Java 구현이 추가되었습니다. 기존 `studica` / `com.studica.frc`
API를 유지합니다. 아직 현재 확장 프로그램 릴리스에 포함되지 않았으므로
일치하는 커스텀 라이브러리가 필요합니다.

[Studica API 설정 및 사용 예제](guides/vmx-pi/studica-api.md)

## 프로젝트 링크

- [VMX on WPI C++ API 문서](/vmxonwpi/apidocs/) — VMX용 구현을 추가한 WPILib 하드웨어 API와 채널 매핑·Driver Station 통신 등 VMX 전용 인터페이스를 제공합니다. 공개 API와 백엔드 내부 인터페이스, 구현 제한 사항을 구분해 안내합니다. 로봇 입출력 지원 범위는 [하드웨어 지원](guides/vmx-pi/hardware-support.md)을 확인하세요.
- [VMX2026 확장 프로그램 릴리스](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases)
- [VMXONWPI GitHub](https://github.com/VMXONWPI)
- [WPILib 2026 공식 문서](https://docs.wpilib.org/en/2026/)
