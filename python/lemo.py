import re, requests, os

if os.path.exists("sample.txt"):
  os.remove("sample.txt")
    
if os.path.exists("lemoTV.m3u"):
  os.remove("lemoTV.m3u")
    
response = requests.get('http://line.lemotv.cc:25461/get.php?username=Ufq7Y2hUbX&password=tJNse4HJja&type=m3u_plus&output=mpegts', timeout=120)
with open("sample.txt", "w") as file:
    file.write(response.text)

fo = open("sample.txt", "r")

tvg_id_set={""}
lines = fo.readlines()
for i in range(0, len(lines)):
    line = lines[i]
    #print (line)
    x = re.findall("tvg-id=\"(.*?)\"", line)
    if (len(x) > 0) :
        v = x[0]
        if (len(v) > 0) :
            #print(x[0])
            tvg_id_set.add(x[0])
print (tvg_id_set)

group_title_set={""}
fo = open("sample.txt", "r")
lines = fo.readlines()
for i in range(0, len(lines)):
    line = lines[i]
    #print (line)
    x = re.findall("group-title=\"(.*?)\"", line)
    if (len(x) > 0) :
        v = x[0]
        if (len(v) > 0) :
            #print(x[0])
            group_title_set.add(x[0])
print (group_title_set)



m3uOutputFile = open('lemoTV.m3u','w')
print("    ")
print("    ")
m3uOutputFile.write("#EXTM3U\n")
m3uOutputFile.write("#EXT-X-SESSION-DATA:DATA-ID=\"com.xui.1_5_5r2\"\n")

print ("#EXTM3U")
print ("#EXT-X-SESSION-DATA:DATA-ID=\"com.xui.1_5_5r2\"")

desired_group_title_set={'Sport Cricket', 'IN: Indian Marathi', 'IN: Indian South', 'IN: Indian Entertainment', 'ESPN Events 200 VIP channels', 'USA NFL - Sunday Ticket', 'Sport Cycling', 'USA Local - MISC', 'BR: Brazil Sports', 'USA Bally Sports', 'DE: Germany Sport', 'FR: France Sports', 'TR: Turkey Sport', 'USA NBA', 'Movies-HBO', 'CA: Canada Super Sports', 'Sport College Baseball', 'Sport Tennis', 'RO: Romania Sports', 'Movies - Tamil', 'CA: Canada Sports', 'Movies-Bollywood', 'Sport Rugby', 'USA Local - CBS', 'BIH: Bosnia Sport', 'HR: Croatia Sport', 'SE: Sweden Sport', 'Sport NCAA Women Basketball', 'Sport Softball', 'USA MLB', 'USA NBC Sports', 'Africa Super Sports', 'IN: Indian Tamil', 'USA NFL - Sunday Ticket', 'USA Local - ABC', 'IT: Sky Sports', 'MX: Mexico Sports', 'Movies-Netflix', 'DK: Denmark Sport', 'NetFlix Premium', 'USA Local - NBC', '24/7 Sports Replay', 'HU: Hungary Sport', 'USA Sports', 'AR: Arabic Sports', 'UK: Sport', 'USA NCAAF', 'PK: Pakistan Sport', 'PL: Poland Sports', 'CH: Switzerland Sport', 'Latino Sports', 'UK: EPL Games', 'USA NHL', 'CAR: Caribbean Sport', 'Sport Match Center', 'USA Bein Sports', 'Sport Golf', 'Movies-Classic', 'Tom & Jerry Collection', 'USA Local - FOX', 'AR: Arab BeIN sports VIP'}
fo = open("sample.txt", "r")
lines = fo.readlines()
for i in range(0, len(lines)):
    line = lines[i]
    #print (line)
    x = re.findall("group-title=\"(.*?)\"", line)
    if (len(x) > 0) :
        v = x[0]
        if (len(v) > 0) :
            v=(x[0])
            if (v in desired_group_title_set):
                currLine = lines[i]
                nextLine = lines[i+1]
                if ("mkv" in nextLine) or ("avi" in nextLine) :
                    print ("Did not write - %s", nextLine)
                else :
                    #print(currLine.strip())
                    #print(nextLine.strip())
                    m3uOutputFile.write(currLine)
                    m3uOutputFile.write(nextLine)
os.unlink("sample.txt")
