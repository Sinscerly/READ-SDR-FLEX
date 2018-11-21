*****************************************
*************** README ******************

This repo is for getting a certain P2000 message, this is made for fair use only.

RTL-SDR Receiver is used.

Frequency: 169,650 MHz
Speed 1600 bit/s (2FSK)
Protocol: Motorola FLEX


Could be handy to have installed:

	- git
	
	- cmake
	
	- build-essential
	
	- libusb-1.0.0
	
	- qt4-qmake
	
	- libpulse-dev
	
	- libx11-dev
	
	- qt4-default

I have tested it with python3.5

*****************************************
**** Install P2000 RECEIVER: RTL-SDR ****

Execute:

	mkdir -p ~/src/
	
	cd ~/src/
	
	git clone git://git.osmocom.org/rtl-sdr.git
	
	cd rtl-sdr
	
	mkdir build
	
	cd build
	
	cmake ../ -DINSTALL_UDEV_RULES=ON
	
	make
	
	sudo make install
	
	sudo ldconfig

**** Test it ****

Execute:

	rtl_test


If error comes out -> goto: /etc/modprobe.d/raspi-blacklist.conf and put in:

	blacklist dvb_usb_rtl28xxu
	
	blacklist rtl2832
	
	blacklist rtl2830

reboot and try again

*************************************************
**** Install P2000 FLEX DECODER: MULTIMON-NG ****

Execute:

	cd ~/src/
	
	git clone https://github.com/Zanoroy/multimon-ng.git
	
	cd multimon-ng
	
	mkdir build
	
	cd build
	
	qmake ../multimon-ng.pro
	
	make
	
	sudo make install

**** Test Receiving ****

Dutch example, execute:

	rtl_fm -f 169.65M -M fm -s 22050 -p 43 -g 49 | multimon-ng -a FLEX -t raw /dev/stdin


If it looks something like this:

FLEX: 2018-11-15 14:08:20 1600/2/K/A 02.020 [000000000] ALN test 446 fijne dienst

You made it :)
