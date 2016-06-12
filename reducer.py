#!/usr/bin/python26
#-*-coding:utf-8-*-

import os
import sys
import json

default_encoding="utf-8"

if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
def is_in_business_bound(x,y,bounds):
  minX = bounds[0][0]
  maxX = bounds[0][0]
  minY = bounds[0][1]
  maxY = bounds[0][1]
  length = len(bounds)
  if length <= 2:
    return -1
  for k in range(0, length):
    if bounds[k][0] < minX:
      minX = bounds[k][0]
    if bounds[k][0] > maxX:
      maxX = bounds[k][0]
    if bounds[k][1] < minY:
      minY = bounds[k][1]
    if bounds[k][1] > maxY:
      maxY = bounds[k][1]
  if (x < minX or x > maxX or y < minY or y > maxY):
    return -1
  i = 0
  j = length - 2
result = -1
  while (i < length - 1):
    if ((bounds[i][1] != bounds[j][1]) and ((bounds[i][1] > y) != (bounds[j][1] > y)) and (x < ((bounds[j][0] - bounds[i][0]) * (y - bounds[i][1]) / (bounds[j][1] - bounds[i][1]) + bounds[i][0]))):
      result = -1 * result
    j = i
    i = i + 1
  return result

def find_business(city, x, y, bounds_dict):
  city = city.strip()
  x = x.strip()
  y = y.strip()
  if city.find("市") == -1:
    city = city + "市"
  if not bounds_dict.has_key(city):
    return ""
  bounds = bounds_dict[city]
  for i in range(0, len(bounds)):
    city_bound = bounds[i].split("\t")
    if len(city_bound) != 3:
      continue
    bound = city_bound[2]
    bound = bound.strip().strip("\n")
    bound_set = bound.split(";")
    if len(bound_set) <= 2:
      continue
    xys = []
    for j in range(0, len(bound_set)):
      xy_set = bound_set[j].split(',')
      if len(xy_set) != 2:
        continue
x_tmp = float(xy_set[0])
      y_tmp = float(xy_set[1])
      xys.append([x_tmp,y_tmp])
    if is_in_business_bound(float(x), float(y), xys) == 1:
      result = city_bound[1].split(" ")
      if len(result) == 2:
        return result[0] + "_" + result[1]
  return ""


bounds_dict = {}
file = open("business_bound.dict", "r")
for l in file:
  l = l.strip().strip("\n")
  l_set = l.split("\t")
  if len(l_set) != 2:
    continue
  city_bus = l_set[0].split(" ")
  if len(city_bus) != 2:
    continue
  city = city_bus[0]
  if bounds_dict.has_key(city):
    l = "1" + "\t" + l
    bounds_dict[city].append(l)
  else:
    l = "1" + "\t" + l
    list_tmp = [l]
    bounds_dict[city] = list_tmp
file.close()

for line in sys.stdin:
  line = line.strip().strip("\n")
  if line == "":
    continue
  source_set = line.split("\t")
  if len(source_set) < 3:
    continue
  if len(source_set) == 4:
    result = find_business(source_set[1], source_set[2], source_set[3], bounds_dict)
    if result != "":
      result_json = {}
      result_json["id"] = source_set[0]
      result_json["business_area"] = result
      result_str = json.dumps(result_json)
      print result_str
