#!/usr/local/bin/python3.9

import random
import json

dinners = open('dinners.json')
dinjson = json.load(dinners)

for dinner in random.choices(dinjson):
	print(json.dumps(dinner, indent=2))