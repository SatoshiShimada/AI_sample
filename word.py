# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 2:
	print "usage: python word.py [file]"
	sys.exit(1)

word_file = "database.txt"

fp = open(word_file, "r")

lines = fp.readlines()

word = []
for line in lines:
	word.append(line)

fin = open(sys.argv[1], "r")

w = ""
for ch in fin.read():
	w += ch
	if w in word:
		print w
		w = ""
