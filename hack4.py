#!/usr/bin/python
from __future__ import unicode_literals

import subprocess
import json
import sys
import re
import os

def list1 (p) :
	y = 10
	result = y + p
	print(result)
	return result

print ("Please enter a number between 0 ands 999")
x = input()
if x >= 0 and x <= 999:
	list1 (x)
else :
	print ("Invalid number entered. Run program again")

