---
title: VMX-Pi Setup
---

## Download the VMX-Pi image

Download the VMX-Pi image from the link below. The link is temporary and may change.

[Download the VMX-Pi image](https://naver.me/GuCcHhMS)

## Write the image to a storage device

Use Raspberry Pi Imager to write the downloaded image to an SD card or other intended storage device. The screenshots below show one setup using a Raspberry Pi 4 and a 14.8 GB device; your device name, capacity, and image filename may be different.

1. Select the Raspberry Pi model that matches your hardware. This example uses Raspberry Pi 4.

   ![Raspberry Pi Imager device selection screen with Raspberry Pi 4 highlighted](../../../assets/vmx-pi-setup/01-select-device.png)

2. Open the operating system list and choose **Use custom**.

   ![Raspberry Pi Imager operating system list with Use custom highlighted](../../../assets/vmx-pi-setup/02-select-os.png)

3. Select the VMX-Pi image file you downloaded from the link above. Do not select `WPILib 2027.iso`: that is the WPILib installer for your computer, not a VMX-Pi image. See [Software Install](software-install.md) to install it on your computer.

4. Choose the SD card or storage device you intend to write to. Check its name and capacity before continuing.

   ![Raspberry Pi Imager storage selection screen](../../../assets/vmx-pi-setup/04-select-storage.png)

5. Review the selected device and confirm the write. **Writing the image erases all data on the selected device and cannot be undone.** Make sure the correct device is selected before confirming.

   ![Raspberry Pi Imager erase and write confirmation dialog](../../../assets/vmx-pi-setup/05-erase-confirmation.png)

6. Wait while Raspberry Pi Imager writes the image. Keep the storage device connected during the operation.

   ![Raspberry Pi Imager writing the image](../../../assets/vmx-pi-setup/06-writing.png)

7. Let verification finish as well. Do not remove the device while writing or verification is in progress.

   ![Raspberry Pi Imager verifying the written image](../../../assets/vmx-pi-setup/07-verifying.png)

8. When Imager reports **Write complete**, the storage device is ready. If it is ejected automatically, you can remove it safely.

## Login credentials

These are the fixed VMX-Pi login credentials. Use them whenever you log in to the VMX-Pi system:

| Username | Password |
|---|---|
| `ubuntu` | `password` |
