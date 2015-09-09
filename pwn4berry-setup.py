#!/usr/bin/python
'''
AVET Information and Network Security Sp. z o.o.  pwn4berry

pwn4berry lite version for NON COMMERCIAL use only. 

For more details please visit us at: www.avet.com.pl
Latest version of this code can be downloaded at: https://github.com/avet/pwn4berry
'''

import os
import sys
import subprocess

def do_install_pkg(cmd, cmd_args):
	try:
		retcode = subprocess.call(cmd + ' ' + cmd_args, shell=True)
		if retcode < 0:
			print >>sys.stderr, 'Process has been terminated by signal'
			return False
		else:
			print 'Installing %s done' % cmd_args
			return True
	except OSError as e:
		print >>sys.stderr, 'Execution of %s failed:' % e
		print cmd, cmd_args
		return False

def do_install():
	pkgs = {'Basic build tools':['sudo apt-get -y install', 'zip', 'gcc', 'build-essential', 'libsdl1.2-dev'],
		'Basic admin tools':['sudo apt-get -y install', 'htop', 'mc'],
		'Basic network tools':['sudo apt-get -y install', 'wget', 'nmap', 'netcat-openbsd', 'wireshark', 'stunnel4', 'tightvncserver', 'ssvnc', 'scanssh', 'sslscan', 'hping3', 'fping', 'dnswalk', 'arping'],
		'Additional network tools':['sudo apt-get -y install', 'dsniff', 'tcpreplay', 'ettercap-common', 'ettercap-text-only', 'yersinia'],
		'More network sniffers':['sudo apt-get -y install', 'ngrep', 'p0f', 'tcpdump', 'tcpslice', 'ssldump'],
		'Python bindings for libpcap':['sudo apt-get -y install', 'python-ncap'],
		'Basic python bindings':['sudo apt-get -y install', 'python-rpi.gpio', 'python-ipaddr', 'python-impacket', 'python-paramiko', 'python-scapy'], 
		'Additional python tools':['sudo apt-get -y install', 'python-setuptools', 'python-virtualenv', 'virtualenvwrapper', 'ipython', 'snimpy'], 
		'Basic web app sec tools':['sudo apt-get -y install', 'nikto'],
		'Exploit development tools':['sudo apt-get -y install', 'bochs', 'qemu'],
		'Exploit database':['wget', '''https://github.com/offensive-security/exploit-database/archive/master.zip'''],
		'Ruby':['sudo apt-get -y install','ruby', 'rubygems'],
		'Source code audit':['sudo apt-get -y install', 'splint'],
		'sqlmap download':['git clone', '''https://github.com/sqlmapproject/sqlmap.git sqlmap-dev'''],
		'wfuzz download':['git clone', '''https://github.com/xmendez/wfuzz wfuzz-dev''']
		}
	
	if os.path.isfile('master.zip'):
		os.remove('master.zip')
	
	for pack in pkgs.keys():
		print ' + Installing: %s' % pack
		cmd = pkgs[pack][0]
		for arg in pkgs[pack][1:]:
			if do_install_pkg(cmd, arg) is False:
				print >>sys.stderr,'* ERROR: Instalation failed *'
				return 2
	print '*** Installation finished ***'
	return 0	 

def do_post_install():
	exit_code = 0

	#install wfuzz
	#do_install_pkg('python', '''./wfuzz-dev/setup.py install''')

	if exit_code == 0:
		print '*** Post installation finished ***'	
	return exit_code

def do_rpi_firmware():
	pkgs = {'Quake & rpi firmware':['git clone','''https://github.com/raspberrypi/linux''', '''https://github.com/raspberrypi/userland''', '''https://github.com/raspberrypi/quake3''']}

	for pack in pkgs.keys():
        	print ' + Installing: %s' % pack
                cmd = pkgs[pack][0]
                for arg in pkgs[pack][1:]:
                        if do_install_pkg(cmd, arg) is False:
                                print >>sys.stderr,'* ERROR: Instalation failed *'
                                return 2
	print '** Firmware and Quake sources download done **'
	return 0


def usage():
	print 'Usage: python pwn4berry-setup.py [command]'


def main():
	exit_code = 0
	if len(sys.argv) != 2:
		usage()
		exit_code = 1
	else:
		if sys.argv[1].lower() == 'install':
			exit_code = do_install()
			if exit_code == 0:
				exit_code = do_post_install()
		elif sys.argv[1].lower() == 'firmware':
			exit_code = do_rpi_firmware()

	sys.exit(exit_code)

if __name__ == '__main__':
	try:
		main()
	except IOError, e:
		print 'IO Error:', e
		sys.exit(1)

