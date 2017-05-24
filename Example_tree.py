
#!/usr/bin/env python
############################## 
# Need to change lots of details below. Then whole script can be run, or pieces can be run in python interactively.
# This script calls makeNexus.sh, which requires user to input a custom path to Paup* 
# This script is all based on unweighted RF distances, will need to edit normalized RF calculations for weighted RF I think. 

############################## 

from __future__ import (division, print_function)
from readTree import Node
from readTree import Tree
import readTree
import dendropy
import subprocess
from cStringIO import StringIO
from Bio import Phylo

############################################################  
#Choose starting tree
############################################################

# Make one random starting tree. 
# Number of tips = 10
tips = 100
# Create random tree. Average branch length of 1. No variation in branch length. Don't print out tree structure
t1 = readTree.rand_tree(tips=tips,brl_avg=1,brl_std=None,verbose='F')

# Calculate number of NNI moves based on desired normalized RF distance.
# Used for creating another starting tree or creating a cluster
# Desired normalized RF distance
RF_norm = 1
# Calculate maximum RF distance and NNI moves
RF_max = 2*(tips-2)
NNI_moves = int((RF_max * RF_norm)/2)

# Confirm calculations
print("RF_norm: "+str(RF_norm)+", NNI_moves: "+str(NNI_moves))

# Create second starting tree
t2 = readTree.NNI_mult_moves(in_tree=t1,num_moves=NNI_moves,node_choice='random',no_dup_start_tree='F')

# Write out tree files
readTree.write_single_tree(t1,'100tip_starting_tree_1.tree')
readTree.write_single_tree(t2,'100tip_starting_tree_2.tree')

# Make cluster of trees around each starting tree
# Calculate number of NNI moves based on desired normalized RF distance.
RF_norm = 0.125
RF_max = 2*(tips-2)
NNI_moves = int((RF_max * RF_norm)/2)

# Make a cluster of 100 trees total in each cluster. 
cluster1 = readTree.NNI_mult_trees(in_tree=t1,num_out_trees=99,num_nni_moves=NNI_moves,out='list')
cluster2 = readTree.NNI_mult_trees(in_tree=t2,num_out_trees=99,num_nni_moves=NNI_moves,out='list')

# Make a nexus file with starting trees and cluster trees
readTree.list_to_out(cluster1, cluster2,'100tip_100tree.tree')

# Turn script into Nexus that is readable by TreeScaper
# This script turns all *.tree files into *.nex files 
subprocess.call(['./makeNexus.sh'])


