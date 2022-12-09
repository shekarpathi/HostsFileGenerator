import requests
import hashlib
import os

# initialize exception domains, these will be allowed
allowable_domains_set = ["fe80::1%lo0 localhost", ".godaddy.com", "sso.godaddy.com", ".etihad.com", "www.googleadservices.com", "ad.doubleclick.net", "go.redirectingat.com", "www.jdoqocy.com", "cj.dotomi.com", "go.redirectingat.com"]

block_url = True

url = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts'
r = requests.get(url, allow_redirects=True, verify=False)
open('hosts.txt', 'wb').write(r.content)

#url = 'https://hosts.ubuntu101.co.za/hosts'
#r = requests.get(url, allow_redirects=True, verify=False)
#open('hosts.txt', 'ab').write(r.content)

url = 'https://gitlab.com/The_Quantum_Alpha/the-quantum-ad-list/-/raw/master/Individual%20lists/The_Quantum_Youtube-Ads-List.txt'
r = requests.get(url, allow_redirects=True, verify=False)
open('hosts.txt', 'ab').write(r.content)

#url = 'https://gitlab.com/The_Quantum_Alpha/the-quantum-ad-list/-/raw/master/Individual%20lists/The_Quantum_Simply-ads-list.txt'
#r = requests.get(url, allow_redirects=True, verify=False)
#open('hosts.txt', 'ab').write(r.content)

url = 'https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds.txt'
r = requests.get(url, allow_redirects=True, verify=False)
open('hosts.txt', 'ab').write(r.content)

url = 'https://gist.githubusercontent.com/consti/8022703/raw/47e20864cae30c8f7024444de353b4f03ee7c93d/hosts'
r = requests.get(url, allow_redirects=True, verify=False)
open('hosts_adobe.txt', 'wb').write(r.content)

#1
fin = open("hosts_adobe.txt", "r")
#output file to write the result to
fout = open("hosts_adobe.add", "w")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('127.0.0.1', '0.0.0.0'))
#close input and output files
fin.close()
fout.close()

output_file_path = 'hosts.add'
#2
completed_lines_hash = set()

#3
output_file = open(output_file_path, 'w')

#4
for line in open('hosts.txt', 'r'):
  block_url = True
  # if (line.rstrip() == "fe80::1%lo0 localhost"):
  #   continue
  for x in allowable_domains_set:
   if (x in line.rstrip()):
     block_url = False
     break
      
  #5
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    if block_url == True:
      output_file.write(line)
      completed_lines_hash.add(hashValue)
#7
output_file.close()
if os.path.exists("hosts.txt"):
  os.remove("hosts.txt")
