#!/usr/bin/python26
#-*-coding:utf-8-*-

import os
import sys
import json

default_encoding="utf-8"

if sys.getdefaultencoding() != default_encoding:
  reload(sys)
  sys.setdefaultencoding(default_encoding)

#filepath = os.environ["map_input_file"]
for line in sys.stdin: 
  try:
    line = line.strip().strip("\n").strip()
    if line == "": 
      continue
    set = line.split("\t")
    dict = json.loads(line)
    if dict.has_key("name") == False:
      continue
    if dict.has_key("id") == False:
      continue
    id = dict["id"]
    if dict.has_key("loc") == False:
      continue
    xy = dict["loc"]
    if len(xy) != 2:
      continue
    x = xy[1]
    y = xy[0]
    if dict.has_key("city") == False:
      continue
    city = dict["city"]
    result = id + "\t" + city + "\t" + str(x) + "\t" + str(y)
    print result
  except Exception:
    print line
