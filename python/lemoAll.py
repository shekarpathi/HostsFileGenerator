import re
import requests
import os


if os.path.exists("lemoAll.m3u"):
    os.remove("lemoAll.m3u")

response = requests.get(
    'http://ky-iptv.com:25461/get.php?username=nameproratererun&password=5715623659&type=m3u_plus&output=mpegts',
    timeout=120)
with open("lemoAll.m3u", "w", encoding="utf-8") as file:
    file.write(response.text)
