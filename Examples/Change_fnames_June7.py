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
	repName = t.split(".")[0]
	listName = repName.split("_")
	# Adding in RF distance between clouds
	newName = listName[0]+"_"+listName[1]+"_0.043_"+"1.0start_"+listName[2]+"_"+listName[3] 
	newt = newName+".nex"
	os.system("mv %s %s" % (t,mainDir+"/"+newt))
	

for t in glob.glob('*.log'):
	# Split off name, dependant on what your iterating handle files are
	repName = t.split(".")[0]
	listName = repName.split("_")
	# Adding in RF distance between clouds
	newName = listName[0]+"_"+listName[1]+"_0.043_"+"1.0start_"+listName[2] 
	newt = newName+".log"
	os.system("mv %s %s" % (t,mainDir+"/"+newt))
	
for t in glob.glob('*starting_tree*'):
	# Split off name, dependant on what your iterating handle files are
	repName = t.split(".")[0]
	listName = repName.split("_")
	# Adding in RF distance between clouds
	newName = listName[0]+"_"+listName[1]+"_0.043_"+"1.0start_"+listName[2]+"_"+listName[3]+"_"+listName[4]+"_"+listName[5]
	newt = newName+".nex"
	os.system("mv %s %s" % (t,mainDir+"/"+newt))

for t in glob.glob('200tip*'):
	repName = t.split(".")[0]
	listName = repName.split("_")
	# Adding in RF distance between clouds
	newName = listName[0]+"_"+listName[1]+"_0.043_"+"1.0start_"+listName[2]+"_"+listName[3]+"_"+listName[4]+"_"+listName[5]
	newt = newName+".nex"
	os.system("mv %s %s" % (t,mainDir+"/"+newt))
