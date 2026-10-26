---
title: VMX-Pi Network
---

The VMX-pi can communicate with a PC over its Wi-Fi hotspot, a Wi-Fi router, or Ethernet.

## Default connection

The default setup creates a `WorldSkills-1234` hotspot with password `password` on 2.4 GHz channel 6. The robot's address depends on the team number. For example, team 1234 uses `10.12.34.2`.

| Connection | VMX-pi address | PC setup |
|---|---|---|
| Wi-Fi hotspot | `10.12.34.2` for team 1234 | Join `WorldSkills-1234` |
| Ethernet | `172.22.11.2` | Set the PC's wired IPv4 to DHCP/automatic |
| Wi-Fi router | Address assigned by the router | Connect the VMX-pi and PC to the same router |

After joining the hotspot or connecting a cable, connect over SSH. The VMX-pi username is `ubuntu`.

```sh
ssh ubuntu@10.12.34.2
ssh ubuntu@172.22.11.2
```

## Change the hotspot name or password

`setupHotspot` adds the team number to the Wi-Fi name. This example creates a `W4-1234` hotspot and sets the robot address to `10.12.34.2`.

```sh
sudo setupHotspot W4 1234 2.4 RobotWifi2027
```

The last argument is the Wi-Fi password. WPA2 passwords must be 8–63 characters. Replace the example password with one of your own. If you omit the password, the default `password` is used.

Choose `2.4` or `5` for the Wi-Fi band. If you do not specify a channel, the command selects an available default. Use 2.4 GHz if a usable 5 GHz channel is not available in your regulatory settings.

## Switch to a Wi-Fi router

Connecting to a router turns off the hotspot. Provide the router SSID and password:

```sh
sudo toggleNetMode wifi HomeRouter RouterPassword2027
```

To turn the VMX-pi hotspot back on, run:

```sh
sudo toggleNetMode ap
```

Unless separately changed, the wired connection remains available at `172.22.11.2`. Changing network modes may end the current SSH connection; reconnect after the switch finishes.
