#!/bin/bash

# This will iterate through all files with designated suffix. 
# Output will be a text file with all the commands needed to convert nexus files into a format readable by treescaper. 
# You will have to manually copy and paste the contents of 'paup_to_nexus_list.txt' into the terminal. 
# Edit directory for Paup* as needed. 

for f in *.tree
do
base=`basename $f .tree`
out_nexus=$base".nex"
echo "begin paup;
	set nowarnreset autoclose maxtrees = 200000;
	execute $f;
	savetrees file=$out_nexus;
	quit;

" >> paup_to_nexus_list.txt
done

/Applications/paup4a152_osx paup_to_nexus_list.txt