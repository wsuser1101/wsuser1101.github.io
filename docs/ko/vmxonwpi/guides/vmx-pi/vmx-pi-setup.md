---
title: VMX-Pi 설정
---

## 로봇 요구 사항

VMX on WPI는 Raspberry Pi 4에서 **64비트 Ubuntu 26.04.1 LTS**와 Studica `vmxpi-hal` 패키지를 사용해 시험했습니다. VMX HAL의 `libvmxpi_hal_cpp.so`와 헤더는 Studica에서 제공하며 WPILib이나 Robot Manager 패키지에 포함되지 않습니다.

VMX-pi용 64비트 Ubuntu 26.04 ARM64 시스템 이미지를 준비하세요. 미리 만들어진 이미지를 사용하는 경우 배포 전에 VMX-pi HAL이 포함되어 있는지 확인하세요. 실험실에서 사용한 이미지 다운로드 링크는 임시 링크이므로, 이미지를 기록하기 전에 관리자에게 최신 이미지와 체크섬을 문의하세요.

## 저장 장치에 이미지 기록하기

Raspberry Pi Imager로 호환되는 이미지를 로봇의 SD 카드 또는 저장 장치에 기록합니다.

1. 로봇에 맞는 Raspberry Pi 모델을 선택합니다.
2. 운영체제 목록에서 **Use custom**을 선택합니다.
3. Ubuntu 26.04 ARM64 VMX-pi 이미지를 선택합니다.
4. 로봇의 저장 장치를 선택하고 이름과 용량을 확인합니다.
5. 기록을 진행합니다. **선택한 장치의 데이터가 모두 삭제됩니다.**
6. 기록과 검증이 모두 끝난 뒤 카드를 분리합니다.

## 첫 부팅

유선 또는 Wi-Fi로 로봇에 연결하고 `ubuntu` 계정으로 로그인합니다. 공용 네트워크에 연결하기 전에 기본 비밀번호를 변경하세요. VMX Robot Manager 패키지를 설치합니다. 저장소에 `.deb` 패키지를 직접 빌드하는 안내가 있습니다.

[VMXONWPI/wpi-robot-manager](https://github.com/VMXONWPI/wpi-robot-manager)

이 패키지는 `robot_manager` 서비스, NetworkManager 연동, 유선 네트워크, CPU·Wi-Fi 성능 설정, `/home/lvuser` 런타임 디렉터리를 구성합니다. Studica `vmxpi-hal` 패키지도 필요합니다.

접속 주소와 네트워크 명령은 [VMX-Pi 네트워크](vmx-pi-network.md)를, 개발 컴퓨터의 WPILib 설정은 [WPILib 및 VMX2026 설치](software-install.md)를 참고하세요.
