from math import floor
import random

def otgenrator():
    digits = "0123456789"
    otp = ""

    for i in range(4):
        otp += digits[floor(random.random()*10)]
    print(otp)
print("OTP IS : ",end = '')
otgenrator()