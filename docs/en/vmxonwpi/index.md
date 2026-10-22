---
title: VMX on WPI
hide:
  - toc
---

# VMX on WPI · WPILib 2026

VMX on WPI brings the Studica VMX-pi into the WPILib 2026 development workflow. The project includes a VMX-pi HAL for 64-bit Linux, a GradleRIO `VmxPi` deploy target, the VMX2026 VS Code extension, and a NetworkManager-based robot manager.

Use these guides for the WPILib 2026 releases from [VMXONWPI](https://github.com/VMXONWPI). They are separate from the [W4Studica WPILib 2027 beta guides](https://wsuser1101.github.io/W4Studica/).

## Recommended order

1. [Prepare the VMX-pi](guides/vmx-pi/vmx-pi-setup.md) with 64-bit Ubuntu and the Studica VMX HAL.
2. [Install WPILib 2026 and VMX2026](guides/vmx-pi/software-install.md) on the development computer.
3. [Configure robot networking](guides/vmx-pi/vmx-pi-network.md).
4. [Connect a WPILib project to the VMX-pi](guides/vmx-pi/vmx2026-setup.md) and deploy.
5. Review [hardware support](guides/vmx-pi/hardware-support.md) before connecting robot hardware.

The WPILib version is 2026.2.2. The current VMX GradleRIO and HAL pair is 2026.2.2-vmx.2; the [VMX2026 extension releases](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases) list the latest VSIX.
