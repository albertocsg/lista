#!/bin/python

import urllib
import json
from pprint import pprint

# leemos el json
website = urllib.urlopen('http://luckytv.me')
siteData = website.read()

# Quitamos los caracteres extranos del principio
while (siteData[0:1] != "{"):
    siteData = siteData[1:]

# procesamos el json
data = json.loads(siteData)

print("#EXTM3U")
print("")

for groups in data["groups"]:
    if groups["name"] == "Adultos" or groups["name"] == "Play Store de Listas":
        continue

    for stations in groups["stations"]:
        print("#EXTINF:-1, " + stations["name"].encode('utf-8').strip())
        print(stations["url"].encode('utf-8').strip())
        print("")

