#!/bin/bash

# This will iterate through all files with designated suffix. 
# Output will be a text file with all the commands needed to convert nexus files into a format readable by treescaper. 
# You will have to manually copy and paste the contents of 'paup_to_nexus_list.txt' into the terminal. 
# Edit directory for Paup* as needed. 

for f in *.tree
do
base=`basename $f .tree`
out_nexus=$base".nex"
echo "/Applications/paup4a152_osx $f
Y
1000000
2
savetrees file=$out_nexus
quit
" >> paup_to_nexus_list.txt
done

