---
title: VMX-Pi Network
---

The VMX Robot Manager keeps the familiar W4Studica command names while configuring interfaces through NetworkManager. After installing the package, wired Ethernet is configured automatically. Configure the robot's access point once with `setupHotspot`.

## Wi-Fi access point

For team 1234, this creates the `VMX-1234` hotspot and assigns the robot `10.12.34.2`:

```sh
sudo setupHotspot VMX 1234 2.4 password
```

The last argument is the WPA2 password (8–63 characters). Change the example password before use. The command supports 2.4 GHz or 5 GHz; 2.4 GHz is the safer choice when the local 5 GHz channel plan is unknown. A channel can be selected when prompted or supplied with `--channel N`.

To reactivate the saved access point later:

```sh
sudo toggleNetMode ap
```

## Wired Ethernet

The robot uses `172.22.11.2/24` on its wired interface and runs DHCP for a directly connected computer. Set the computer's wired IPv4 configuration to automatic/DHCP. To configure the profile manually:

```sh
sudo setupEthernet
```

Connect to the robot with SSH:

```sh
ssh ubuntu@172.22.11.2
```

## Join a Wi-Fi router

To connect the VMX-pi and development computer to the same router, provide the router SSID and password:

```sh
sudo toggleNetMode wifi HomeRouter RouterPassword
```

To use a previously saved Wi-Fi profile, run `sudo toggleNetMode wifi` without credentials. The router assigns the robot's address; inspect the router's DHCP lease list to find it. Network changes may disconnect the current SSH session. Reconnect after the new profile becomes active.

The access point address uses the team number as `10.TE.AM.2` (for example, team 1234 is `10.12.34.2`). The wired address remains `172.22.11.2`.
