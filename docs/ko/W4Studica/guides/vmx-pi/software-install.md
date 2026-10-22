---
title: 소프트웨어 설치
---

## WPILib 2027 Alpha 7 다운로드

[WPILib 2027.0.0-alpha-7 릴리스 페이지](https://github.com/wpilibsuite/allwpilib/releases/tag/v2027.0.0-alpha-7)를 여세요. 아래 사진처럼 **Downloads** 영역에서 컴퓨터에 맞는 항목을 클릭하면 됩니다. 프로세서에 따라 x64 또는 Arm64를 선택하고, Mac은 Apple silicon이면 **Mac (Arm)**, Intel Mac이면 **Mac (Intel)**을 선택하세요.

[![WPILib 릴리스의 Downloads 영역](/assets/w4studica/wpilib-downloads.png)](https://github.com/wpilibsuite/allwpilib/releases/tag/v2027.0.0-alpha-7)

이 설치 안내는 [WPILib 공식 설치 문서](https://docs.wpilib.org/en/latest/docs/zero-to-robot/step-2/wpilib-setup.html)를 참고해 작성했습니다. 이 버전은 정식 출시 전 프리릴리스이므로 설치 전에 문서에서 최신 요구 사항과 릴리스 정보를 확인하세요.

!!! warning "이 설치 파일은 컴퓨터용입니다"
    Windows `.iso`는 컴퓨터에 WPILib을 설치하기 위한 디스크 이미지입니다. Raspberry Pi Imager로 SD 카드에 기록하지 마세요. 로봇 저장 장치를 준비할 때는 [VMX-Pi 설정](vmx-pi-setup.md)에 있는 별도의 VMX-Pi 이미지를 사용하세요.

## Windows에 설치하기

1. 위 릴리스 페이지에서 프로세서에 맞는 Windows `.iso` 파일을 다운로드합니다.
2. 파일 탐색기에서 `.iso` 파일을 마우스 오른쪽 버튼으로 클릭하고 **Mount(탑재)**를 선택합니다. Mount가 보이지 않으면 7-Zip 같은 도구로 ISO를 압축 해제합니다.
3. 탑재된 드라이브 또는 압축 해제한 폴더를 열고 `WPILibInstaller.exe`를 실행합니다.
4. 설치 프로그램에서 **Start**를 누른 뒤, WPILib 도구·VS Code·확장 프로그램·Java·종속 항목을 모두 설치하려면 **Everything**을 선택합니다.
5. 특별히 모든 계정에 설치해야 하는 경우가 아니라면 **Install for this User**를 선택합니다.
6. VS Code 설치 단계에서 **Download for this computer only**를 선택하고 **Next**를 누른 뒤 설치가 끝날 때까지 기다립니다.
7. **Finish**를 누릅니다. 로봇 코드를 작성할 때는 별도로 설치된 **WPILib VS Code 2027**을 실행하세요.

Windows에서 “Windows protected your PC” 창이 나오면 **More info**를 누른 뒤 **Run anyway**를 선택해 공식 릴리스에서 받은 설치 프로그램을 실행합니다.

## macOS에 설치하기

1. Mac 프로세서에 맞는 `.dmg` 파일(Apple silicon 또는 Intel)을 다운로드합니다.
2. 다운로드한 디스크 이미지를 열고 `WPILibInstaller`를 실행합니다.
3. 설치 안내를 따릅니다. 설치가 끝나면 WPILib 설치 디스크 이미지를 꺼냅니다.

## Linux에 설치하기

1. 컴퓨터에 맞는 Linux `.tar.gz` 파일(x64 또는 Arm64)을 다운로드합니다.
2. 다운로드 파일이 있는 폴더에서 터미널을 열고 압축을 풉니다. x64 파일은 다음 명령을 사용합니다.

   ```bash
   tar -xf WPILib_Linux-x64-2027.0.0-alpha-7.tar.gz
   cd WPILib_Linux-2027.0.0-alpha-7
   ./WPILibInstaller
   ```

   Arm64는 `WPILib_Linux-Arm64-2027.0.0-alpha-7.tar.gz` 파일과 압축이 풀린 해당 폴더를 사용하세요.
3. 설치 안내를 따르고 VS Code를 묻는 단계에서는 **Download for this computer only**를 선택합니다.

## 로봇에 배포하기 전에

컴퓨터에 WPILib을 설치해도 VMX-Pi 운영체제 이미지는 설치되지 않습니다. [VMX-Pi 설정](vmx-pi-setup.md)에서 로봇 이미지를 별도로 준비한 뒤, [W4Studica 라이브러리 추가](adding-w4studica-libraries.md)의 안내를 따르세요.

WPILib Alpha 7은 호환성이 변경된 프리릴리스입니다. 공식 릴리스 안내에는 공식 Systemcore 환경의 요구 사항으로 Systemcore Image 14와 FIRST Driver Station Alpha 7이 명시되어 있습니다. VMX-Pi에 배포하기 전 W4Studica 안내에서 해당 로봇 이미지와 호환되는 절차를 확인하세요.
