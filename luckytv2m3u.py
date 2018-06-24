#!/bin/python

import urllib
import json
from pprint import pprint

# leemos el json
website = urllib.urlopen('http://luckytv.me') 
siteData = website.read()

# procesamos el json
data = json.loads(siteData)

print("#EXTM3U")
print("")

for groups in data["groups"]:
    #print(key["name"])
    for stations in groups["stations"]:
        print("#EXTINF:-1, " + stations["name"].encode('utf-8').strip())
        print(stations["url"].encode('utf-8').strip())
        print("")

