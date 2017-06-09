#! /usr/bin/env python

import os
import glob
import shutil 
import itertools
import re 


# Make sure you are in directory that you are calling script from 
mainDir = os.getcwd()

for t in glob.glob('*cloud.nex'):
	# Split off name, dependant on what your iterating handle files are
	listName = t.split("_")
	print(listName)
	# Adding in RF distance between clouds
	newName = listName[0]+"_"+listName[1]+"_"+listName[2]+"_1.0start_"+listName[3]+"_"+listName[4]
	print(newName)
	os.system("mv %s %s" % (t,mainDir+"/"+newName))

for t in glob.glob('*.log'):
	# Split off name, dependant on what your iterating handle files are
	listName = t.split("_")
	# Adding in RF distance between clouds
	newName = listName[0]+"_"+listName[1]+"_"+listName[2]+"_1.0start_"+listName[3]
	os.system("mv %s %s" % (t,mainDir+"/"+newName))
	
for t in glob.glob('*starting_tree*'):
	# Split off name, dependant on what your iterating handle files are
	listName = t.split("_")
	# Adding in RF distance between clouds
	newName = listName[0]+"_"+listName[1]+"_"+listName[2]+"_1.0start_"+listName[3]+"_"+listName[4]+"_"+listName[5]+"_"+listName[6]
	os.system("mv %s %s" % (t,mainDir+"/"+newName))

