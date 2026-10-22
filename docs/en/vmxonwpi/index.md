---
title: VMX-Pi on WPILib
hide:
  - toc
---

# VMX-Pi on WPILib

**WPILib 2026 · C++ and Java**

[C++ API](/vmxonwpi/apidocs/){ .md-button }

VMX-Pi on WPILib brings the Studica VMX-pi into the WPILib 2026 development workflow. The project includes a VMX-pi HAL for 64-bit Linux, a GradleRIO `VmxPi` deploy target, the VMX2026 VS Code extension, and a NetworkManager-based robot manager.

Use these guides for the WPILib 2026 releases from [VMXONWPI](https://github.com/VMXONWPI).

## Recommended order

1. [Prepare the VMX-Pi image](guides/vmx-pi/vmx-pi-setup.md).
2. [Configure robot networking](guides/vmx-pi/vmx-pi-network.md).
3. [Install WPILib 2026 and VMX2026](guides/vmx-pi/software-install.md) on the development computer.
4. [Connect a WPILib project to the VMX-pi](guides/vmx-pi/vmx2026-setup.md) and deploy.
5. Review [hardware support](guides/vmx-pi/hardware-support.md) before connecting robot hardware.

The WPILib version is 2026.2.2. The current VMX GradleRIO and HAL pair is 2026.2.2-vmx.2; the [VMX2026 extension releases](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases) list the latest VSIX.

## Project links

- [VMX on WPI C++ API reference](/vmxonwpi/apidocs/) — searchable WPILib 2026 classes, namespaces and public HAL headers. API listings do not establish VMX-pi hardware support; check [hardware support](guides/vmx-pi/hardware-support.md).
- [VMX2026 extension releases](https://github.com/VMXONWPI/VMX2026VSCodeExtension/releases)
- [VMXONWPI on GitHub](https://github.com/VMXONWPI)
- [WPILib 2026 documentation](https://docs.wpilib.org/en/2026/)
