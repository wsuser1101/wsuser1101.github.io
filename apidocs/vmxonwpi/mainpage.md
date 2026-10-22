# VMX on WPI C++ API

**VMX HAL additions · 2026.2.2-vmx.2**

Reference for the VMX-specific interfaces added by the VMX on WPI port.
Use **Classes**, **Namespaces**, **Files**, or search to find an interface.

These are **internal HAL backend interfaces**, not an additional public robot
library. The port implements the existing WPILib API on VMX-pi without adding
new public WPILib headers. Robot programs continue to use the standard WPILib
API. The general WPILib class reference is excluded from this site.

## VMX additions

| Area | Interfaces |
| --- | --- |
| Channel mapping | @ref Mau_Channel, @ref Mau_ChannelGroup, @ref Mau_HandledGroup, @ref Mau_ChannelMap |
| Channel configuration | @ref Mau_FileHandler, @ref Mau_EnumConverter |
| Backend access and communication errors | @ref mau::GetChannelInfo, @ref mau::DefaultOnBoardCommError, @ref mau::RetryWriteOnBoardCommError, @ref mau::ClearBoardCommErrorStatus |
| Driver Station data and snapshots | @ref Mau_DriveData, @ref Mau_SharedJoystick |
| Driver Station communication | @ref mau::comms namespace — protocol threads, packet handling and robot status |
| Bounded packet reading | @ref mau::comms::PacketReader |
| TCP frame reassembly | @ref mau::comms::TcpPacketBuffer |
| VMX time | @ref mau::vmxGetTime; timing helpers in `MauClockInternal.h` |
| VMX AHRS bridge | `HAL_Mau_AHRS_*` functions in `navX/include/AHRS_Mau.h` |
| VMX-specific errors | `MAU_*` constants in `MauErrors.h` |

Only the selected VMX interface headers are inputs. Upstream WPILib classes,
standard HAL declarations, bundled RapidJSON and CAN frame libraries, and
proprietary Studica SDK headers are excluded. SDK types in signatures are
external dependencies and do not acquire their own API pages here.

## Guides and source

- [VMX on WPI guides](/vmxonwpi/)
- [한국어 안내](/ko/vmxonwpi/)
- [Hardware support](/vmxonwpi/guides/vmx-pi/hardware-support/)
- [VMX backend source](https://github.com/VMXONWPI/allwpilib/tree/7a10d27fe5bb3291e9a8fc62db0e3d400982d530/hal/src/main/native/mau)
- [VMX HAL implementation notes](https://github.com/VMXONWPI/allwpilib/blob/7a10d27fe5bb3291e9a8fc62db0e3d400982d530/vmx/README.md)
