import math

import requests
from flask import Flask

print("Hello World")
r = requests.get("https://coreyms.com")
print(r.status_code)
# name = input("Enter Name: ")
# print("Hello,", name)
