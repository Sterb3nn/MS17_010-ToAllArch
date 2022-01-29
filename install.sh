#!/bin/bash
apt-get install python2 nasm -y
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
python2 get-pip.py
pip2 install impacket
apt-get install metasploit-framework
