import re
import requests
import os


if os.path.exists("lemoTVSports.m3u"):
    os.remove("lemoTVSports.m3u")

if os.path.exists("lemoTVMaster.txt"):
    os.remove("lemoTVMaster.txt")

response = requests.get(
    'http://line.lemotv.cc:25461/get.php?username=Ufq7Y2hUbX&password=tJNse4HJja&type=m3u_plus&output=mpegts',
    timeout=120)
with open("lemoTVMaster.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

fo = open("lemoTVMaster.txt", "r", encoding="utf-8")

tvg_id_set = {""}
lines = fo.readlines()
for i in range(0, len(lines)):
    line = lines[i]
    # print (line)
    x = re.findall("tvg-id=\"(.*?)\"", line)
    if (len(x) > 0):
        v = x[0]
        if (len(v) > 0):
            # print(x[0])
            tvg_id_set.add(x[0])
print(tvg_id_set)

group_title_set = {""}
fo = open("lemoTVMaster.txt", "r", encoding="utf-8")
lines = fo.readlines()
for i in range(0, len(lines)):
    line = lines[i]
    # print (line)
    x = re.findall("group-title=\"(.*?)\"", line)
    if (len(x) > 0):
        v = x[0]
        if (len(v) > 0):
            # print(x[0])
            group_title_set.add(x[0])
print(group_title_set)

m3uOutputFile = open('lemoTVSports.m3u', 'w', encoding="utf-8")
print("    ")
print("    ")
m3uOutputFile.write("#EXTM3U\n")
m3uOutputFile.write("#EXT-X-SESSION-DATA:DATA-ID=\"com.xui.1_5_5r2\"\n")

print("#EXTM3U")
print("#EXT-X-SESSION-DATA:DATA-ID=\"com.xui.1_5_5r2\"")

desired_group_title_set = {'Sport Cricket', 'IN: Indian South', 'IN: Indian Entertainment',
                           'ESPN Events 200 VIP channels', 'USA NFL - Sunday Ticket', 'Sport Cycling',
                           'USA Local - MISC', 'BR: Brazil Sports', 'USA Bally Sports', 'DE: Germany Sport',
                           'FR: France Sports', 'USA NBA', 'CA: Canada Super Sports',
                           'Sport Tennis',
                           'CA: Canada Sports', 'USA Local - CBS',
                           'SE: Sweden Sport', 'Sport NCAA Women Basketball',
                           'USA MLB', 'USA NBC Sports', 'Africa Super Sports',
                           'USA NFL - Sunday Ticket', 'USA Local - ABC', 'IT: Sky Sports',
                           'DK: Denmark Sport', 'USA Local - NBC',
                           '24/7 Sports Replay', 'USA Sports', 'UK: Sport',
                           'USA NCAAF', 'PK: Pakistan Sport', 'CH: Switzerland Sport',
                           'Latino Sports', 'UK: EPL Games', 'USA NHL', 'CAR: Caribbean Sport',
                           'USA Bein Sports', 'Sport Golf',
                           'USA Local - FOX'}
fo = open("lemoTVMaster.txt", "r", encoding="utf-8")
lines = fo.readlines()
for i in range(0, len(lines)):
    line = lines[i]
    # print (line)
    x = re.findall("group-title=\"(.*?)\"", line)
    if (len(x) > 0):
        v = x[0]
        if (len(v) > 0):
            v = (x[0])
            if (v in desired_group_title_set):
                currLine = lines[i]
                nextLine = lines[i + 1]
                if ("mkv" in nextLine) or ("avi" in nextLine) or ("mp4" in nextLine):
                    print("Did not write - %s" % nextLine)
                else:
                    # print(currLine.strip())
                    # print(nextLine.strip())
                    m3uOutputFile.write('%s\n' % currLine)
                    m3uOutputFile.write('%s\n' % nextLine)
fo.close()
os.unlink("lemoTVMaster.txt")
