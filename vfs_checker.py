
import time
import requests
import os

def check_vfs():
    url = "https://visa.vfsglobal.com/eg/en/prt/login"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("الموقع شغال")
        else:
            print("الموقع مش متاح حالياً. راجع لاحقاً")
    except:
        print("فشل في الاتصال بالموقع")

while True:
    check_vfs()
    time.sleep(60 * 5)  # كل 5 دقايق
