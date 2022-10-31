#!/usr/bin/env python3

import requests

url = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLSf9WQu4b2ZbgLPFHusSGuI-2W3LE3FfSPHqxxMdqqYXTg3r8w/formResponse'

form_data = {'entry.839337160':'This is a test'}

r=requests.post(url, data=form_data)
