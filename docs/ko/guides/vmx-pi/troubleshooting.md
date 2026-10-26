---
title: 문제 해결
---

## 빌드가 `VMXPi.h: No such file or directory`로 실패합니다

VMX HAL 헤더와 라이브러리는 Studica 소유라서 W4Studica 다운로드에 들어 있지 않습니다. 새 프로젝트는 로봇에서 한 번 가져옵니다. VMX-Pi를 연결하고 배포를 한 번 실행하거나, 직접 가져오세요.

```sh
./gradlew fetchVmxSdksystemcore
```

마지막 단어는 `build.gradle`에 있는 배포 대상 이름입니다(W4Studica 확장으로 만든 프로젝트에서는 `systemcore`). 한 번 가져온 뒤에는 `clean` 후에도 로봇 없이 빌드할 수 있습니다.

## 배포 시 로봇을 찾지 못하거나 첫 연결이 느립니다

컴퓨터의 Wi-Fi 절전 기능 때문에 VMX-Pi의 첫 응답이 몇 초 늦어질 수 있습니다. Wi-Fi 어댑터의 절전을 끄세요. NetworkManager를 쓰는 Linux에서는 다음과 같습니다.

```sh
nmcli connection modify <연결 이름> 802-11-wireless.powersave 2
```

컴퓨터가 VMX-Pi 핫스팟에 연결되었는지, 유선이라면 자동(DHCP) 주소를 쓰는지도 확인하세요. [VMX-Pi 네트워크](vmx-pi-network.md)를 참고하세요.

## 다음 실행이 `initMboxBlock: init mbox zaps failed`로 실패합니다

이전 프로그램이 정리되기 전에 강제로 종료되었습니다. VMX-Pi를 재부팅하세요. 정상적인 종료는 1초 정도 걸립니다.

## 모터가 돌지 않습니다

Titan은 활성화되기 전에는 명령을 무시합니다. `wpilibvmx::StudicaTitan`과 `wpilibvmx::TitanEnableGuard`를 사용하고, 속도 명령을 150 ms 이내마다 보내고, `studica_driver::Titan::Enable()`은 호출하지 마세요. [로봇 코딩 시작하기](start-robot-coding.md)를 참고하세요.

## 서보나 PWM 출력이 반응하지 않습니다

VMX-Pi에서 프로그램 출력을 확인하세요.

```sh
journalctl -u robot_manager -f
```

PWM 채널이 정상이면 `HALSim VMX: PWM <n> -> VMX channel <m>`이 출력됩니다. 이 줄이 없으면 `HALSIMVMX_PWM_MAP`이 설정되지 않았거나 그 채널이 목록에 없는 것입니다. [하드웨어 지원](hardware-support.md)을 참고하세요. PWM 출력은 Beta 6에서 새로 추가되었고 아직 로봇에서 시험하지 않았으니, 확인한 결과를 알려 주세요.

## WPILib 입력이나 출력이 동작하지 않습니다

프로그램 로그에 어떤 연결 설정이 없는지 나옵니다. 예를 들면 `HALSIMVMX_DIO_MAP is not set; no DIO channels mapped`입니다. [하드웨어 지원](hardware-support.md)에 설명된 대로 채널을 연결하세요.

## 로그에 `[GetSingle] Failed to write config!`가 계속 나옵니다

Cobra 센서가 I2C 버스에서 응답하지 않습니다. 연결되지 않았거나 배선이 잘못된 경우입니다. 프로그램은 계속 실행되고 Cobra 값은 -1로 읽힙니다.
