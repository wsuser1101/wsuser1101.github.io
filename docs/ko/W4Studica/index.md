---
title: 프로젝트 소개
hide:
  - toc
---

<div class="hero" markdown>

# W4Studica

**Studica VMX-pi에서 2027 WPILib을.** 현재 베타 버전을 개발하는 커뮤니티 프로젝트입니다.

[시작하기](guides/vmx-pi/vmx-pi-setup.md){ .md-button .md-button--primary }
[C++ API](/W4Studica/apidocs/){ .md-button }
[GitHub](https://github.com/W4Studica){ .md-button }

</div>

<div class="grid cards" markdown>

- :material-language-cpp: **PC에서 C++로 작성**

    GradleRIO로 빌드하고 `./gradlew deploy`로 네트워크를 통해 VMX-pi에 배포합니다.

- :material-chip: **VMX 하드웨어에서 WPILib 클래스**

    디지털 입출력, 아날로그 입력, 엔코더, PWM, IMU는 WPILib 클래스로 사용합니다. Titan 같은 Studica 장치는 Studica API와 W4Studica 도우미 클래스로 사용합니다.

- :material-shield-check: **Titan 안전 장치**

    로봇이 비활성화되거나 E-stop이 걸리거나 프로그램이 종료되면 Guard가 Titan을 끕니다.

- :material-lan-connect: **유선 또는 Wi-Fi**

    케이블이나 VMX-pi 자체 Wi-Fi 핫스팟으로 연결합니다. 대회 현장과 같은 방식입니다.

</div>

## 왜 만들었나요?

Studica의 WPILib 2020 지원이 끝나면서, VMX-pi에서 예전 환경에 계속 머무르지 않고 새 WPILib을 사용할 방법이 필요했습니다.

하드웨어 드라이버를 전부 새로 만드는 대신, Studica가 ROS 2에서 사용하는 드라이버 코드를 바탕으로 VMX-pi의 장치를 연결합니다.
같은 드라이버 코드를 활용하면 비슷한 기능을 따로따로 만들 필요가 줄고, Studica 장치 지원도 한곳을 중심으로 관리하기 쉽습니다.
W4Studica는 이 드라이버와 WPILib을 연결해 VMX-pi에서도 익숙한 로봇 개발 흐름을 이어가도록 만들고 있습니다.

## 어떻게 사용하나요?

PC에서 C++ 로봇 코드를 작성하고 빌드한 뒤, GradleRIO로 VMX-pi에 배포합니다.
VMX-pi에서는 WPILib과 하드웨어 드라이버를 이어주는 W4Studica 확장을 사용해 프로그램을 실행합니다.

## 현재 진행 상황

!!! info "베타, 2027.0.0-alpha-7 기반"

    C++ 로봇 프로그램의 빌드와 배포, 디지털 입출력·아날로그 입력·엔코더·IMU yaw·Titan 제어를 실제 VMX-pi에서 확인했습니다.

!!! warning "아직 시험하지 않았거나 제공하지 않는 것"

    PWM·서보 출력과 배터리 전압은 이번 베타에 들어 있지만 아직 로봇에서 시험하지 않았습니다. IMU roll, pitch, Z축 각속도의 방향은 더 확인해야 합니다. WPILib의 I2C, DutyCycle, IMU 쿼터니언 출력은 아직 없고, Java 로봇 프로그램은 지원하지 않습니다. 자세한 내용은 [하드웨어 지원](guides/vmx-pi/hardware-support.md)을 참고하세요.

지원 범위를 넓히면서 기능별 확인 결과와 사용 방법을 문서에 정리하고 있습니다. W4Studica는 Studica 또는 WPILib의 공식 배포판이 아닌 커뮤니티 프로젝트입니다.
