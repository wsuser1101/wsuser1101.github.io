---
title: VMX on WPI
hide:
  - toc
---

# VMX on WPI · WPILib 2026

VMX on WPI는 Studica VMX-pi를 WPILib 2026 개발 흐름에서 사용할 수 있게 합니다. 64비트 Linux용 VMX-pi HAL, GradleRIO `VmxPi` 배포 대상, VMX2026 VS Code 확장 프로그램, NetworkManager 기반 Robot Manager를 제공합니다.

[VMXONWPI](https://github.com/VMXONWPI)의 WPILib 2026 릴리스에 이 안내를 적용하세요. 이 문서는 별도의 [W4Studica WPILib 2027 베타 안내](https://wsuser1101.github.io/W4Studica/)와 다른 프로젝트를 다룹니다.

## 권장 순서

1. 64비트 Ubuntu와 Studica VMX HAL로 [VMX-pi를 준비](guides/vmx-pi/vmx-pi-setup.md)합니다.
2. 개발 컴퓨터에 [WPILib 2026 및 VMX2026을 설치](guides/vmx-pi/software-install.md)합니다.
3. [로봇 네트워크를 설정](guides/vmx-pi/vmx-pi-network.md)합니다.
4. [WPILib 프로젝트를 VMX-pi에 연결](guides/vmx-pi/vmx2026-setup.md)하고 배포합니다.
5. 로봇 하드웨어를 연결하기 전에 [하드웨어 지원 범위](guides/vmx-pi/hardware-support.md)를 확인합니다.

WPILib 버전은 2026.2.2입니다. 현재 VMX GradleRIO와 HAL 릴리스 쌍은 2026.2.2-vmx.2입니다. 최신 VSIX는 [VMX2026 확장 프로그램 릴리스](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases)에서 확인하세요.
