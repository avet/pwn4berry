#!/bin/bash
# AVET Information and Network Security Sp. z o.o.  pwn4berry
#
# pwn4berry lite version for NON COMMERCIAL use only.
#
# For more details please visit us at: www.avet.com.pl
# Latest version of this code can be downloaded at: https://github.com/avet/pwn4berry

user_name =$(whoami)
pwn_verfile = /etc/pwn4berry
pwn_ver = "0.2b"
pwn_installbase = ./install-base

echo "pwn4berry version 0.2b (c) 2014 - 2015 AVET Information and Network Security Sp. z o.o. 2014"
echo "AVET INS toolkit for pentesters using Raspberry Pi Raspbian"
echo "Lite version for non commercial use only. WiFi support has been removed"
echo
if [ -f /etc/debian_version ] || [ $user_name -ne "pi" ]; then
	if [ -f $pwn_verfile ]; then
		echo "This installation will update current pwn4berry version if  possible."
	else
		sudo cat $pwn_ver > $pwn_verfile
	fi

	if [ -f $pwn_installbase ]; then
		echo " - Deleting old installation base directory"
		rm -rf $pwn_installbase
	fi

	echo " + Installing basic components"
	sudo apt-get update
	if [ $? -ne 0 ]; then
		echo "Raspbian update failed."
		echo "Please connect your Raspberry Pi to internet."
		exit
	fi
	sudo apt-get -y upgrade
	if [ $? -ne 0 ]; then
		echo "Raspbian update failed."
		exit
	fi
	sudo apt-get -y dist-upgrade
	if [ $? -ne 0 ]; then
		echo "Raspbian distribution update failed."
		exit
	fi
	sudo apt-get -y install wget git python 
	if [ $? -ne 0 ]; then
		echo "Installing git and python failed."
		exit
	fi
	echo " + Downloading pwn4berry base"
	git clone https://github.com/avet/pwn4berry ./install-base
	if [ $? -ne 0 ]; then
		echo "Failed to download pwn4berry components from github"
		exit
	fi
	echo " + Installing additional components"
	python ./install-base/pwn4berry-setup.py install
	if [ $? -ne 0 ]; then
		echo "Failed to run pwn4berry main installer."
		exit
	fi
	echo " + Removing deb packages from cache"
	sudo apt-get clean
else
	echo "Error: pwn4berry can be installed only on Raspbian system using default pi account"
fi
