---
title: VMX-Pi 설정
---

## VMX on WPI 이미지 다운로드

VMX on WPI는 VMX-pi용 부팅 이미지로 배포할 예정입니다. 로봇을 바로 배포할 수 있는 상태로 제공하는 것이 목표입니다. 이미지를 기록하고 VMX-pi 전원을 켠 뒤, 개발 컴퓨터를 로봇의 Wi-Fi 핫스팟에 연결해 로컬 네트워크로 WPILib 프로젝트를 배포하면 됩니다. 로봇과 개발 컴퓨터 사이의 배포 연결에는 인터넷이 필요하지 않습니다. 이미지에는 시험에 사용한 **64비트 Ubuntu 26.04.1 LTS** 기반과 로봇용 VMX HAL, Robot Manager, 핫스팟 설정을 포함해 패키지를 직접 설치하지 않도록 할 계획입니다.

첫 VMX on WPI 이미지가 공개되면 이곳에 다운로드 링크, 버전, 로그인 정보, 체크섬을 안내하겠습니다. 이미지별 정확한 포함 내용과 계정 정보는 릴리스 안내를 확인하세요. W4Studica 2027 이미지를 대신 사용하지 마세요.

## 저장 장치에 이미지 기록하기

이미지를 내려받은 뒤 Raspberry Pi Imager로 로봇의 SD 카드 또는 저장 장치에 기록합니다.

1. 로봇에 맞는 Raspberry Pi 모델을 선택합니다.
2. 운영체제 목록에서 **Use custom**을 선택합니다.
3. VMX on WPI 이미지 파일을 선택합니다.
4. 로봇의 저장 장치를 선택하고 이름과 용량을 확인합니다.
5. 기록을 진행합니다. **선택한 장치의 데이터가 모두 삭제됩니다.**
6. 기록과 검증이 모두 끝난 뒤 카드를 분리합니다.

## 첫 부팅

로봇 전원을 켜고 개발 컴퓨터에서 이미지 릴리스 안내의 VMX 핫스팟 이름과 비밀번호로 접속한 뒤, 핫스팟 주소를 대상으로 배포합니다. 이미지는 `robot_manager` 서비스를 시작하고 NetworkManager, Wi-Fi 핫스팟과 유선 네트워크, CPU·Wi-Fi 성능 설정, `/home/lvuser` 런타임 디렉터리를 구성합니다. 구현은 [VMXONWPI/wpi-robot-manager 저장소](https://github.com/VMXONWPI/wpi-robot-manager)에서 관리합니다.

접속 주소와 네트워크 명령은 [VMX-Pi 네트워크](vmx-pi-network.md)를, 개발 컴퓨터의 WPILib 설정은 [WPILib 및 VMX2026 설치](software-install.md)를 참고하세요.
