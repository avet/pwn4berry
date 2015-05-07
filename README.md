pwn4berry
=========

AVET INS toolkit for pentesters using Raspberry Pi 2 Raspbian

This is lite version of pwn4berry for non-commercial use only. Lite version is missing some tools and has no WiFi/BT support. 

# Requirements
 * Raspberry Pi 2 (Model A will not work - sorry)
 * MicroSD Card (min 16gb)

# Installation

1.	Download latest Raspbian distro from http://downloads.raspberrypi.org/raspbian_latest 
2.	Copy it to micro SD card as described on raspberrypi.org site
3.	Insert card and turn on your Raspberry Pi 2
4.	Select expand fs from raspi-config menu during first boot
5.	Reboot
6.	Log in using pi account
7.	Download (or upload through SSH/SCP)  pwn4berry installation script: install-pwn4berry.sh
8.	Run installation script from shell prompt. You must run the script from pi account.

Installer automatically installs all tools, components required for installation and missing libraries. 


