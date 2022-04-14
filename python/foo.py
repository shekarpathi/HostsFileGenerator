import requests
import hashlib

url = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts'
r = requests.get(url, allow_redirects=True)
open('hosts.txt', 'wb').write(r.content)

url = 'https://hosts.ubuntu101.co.za/hosts'
r = requests.get(url, allow_redirects=True)
open('hosts.txt', 'ab').write(r.content)

output_file_path = 'hosts.add'
#2
completed_lines_hash = set()

#3
output_file = open(output_file_path, 'w')

#4
for line in open('hosts.txt', 'r'):
  #5
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file.close()