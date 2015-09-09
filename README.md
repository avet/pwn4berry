pwn4berry
=========

AVET INS toolkit for pentesters using Raspberry Pi 2 and Raspbian.

# Introduction

pwn4berry is a set of tools to automatically create lightweight Linux distro based on Raspbian for pentesters.
Main objective for pwn4berry is evaluation of infrastructure security in data centers. 

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


Installer automatically installs all tools, components required for installation and missing libraries. When possible installers uses binary packages. For some cases source code is being downloaded. Source code files can be found in ./install-base directory.

# Linux, firmware and Quake sources
If you would like to quickly download Linux kernel, RPI firmware and Quake source code you can also use the pwn4berry installer module: pwn4berry-setup.py. Just run it with “firmware” option:

./pwn4berry-setup.py firmware

Pwn4berry-setup requires python 2.7. Python is being installed by the pwn4berry installer so either install Python first or just run main install script before running pwn4berry-setup.py with “firmware” option.
Sources are being downloaded using git to current directory. 

# Files
Despite base-install directory containing tools and exploit archive (check out master.zip) additional file containing pwn4berry version is now being created at /etc (pwn4berry). 
