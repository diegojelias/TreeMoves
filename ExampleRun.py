
#!/usr/bin/env python
'''
To Do:
'''

-------------------------------------------------------
exit()



python


from __future__ import (division, print_function)
from readTree import Node
from readTree import Tree
import random
import numpy
import readTree
import dendropy
import re
from Bio import Phylo


############################## 
#Input tree options
############################## 
# From string
doo="(P:0.09,(Q:0.07,(X:0.02,((Y:0.03,Z:0.01):0.02,W:0.08):0.06):0.03):0.04)"
boo="(P:0.01,(Q:0.01,(X:0.01,((Y:0.01,Z:0.01):0.01,W:0.01):0.01):0.01):0.01)"
# Create readTree.tree object
in_tree_object = Tree(boo)

# From file
in_tree_object=readTree.read_nexus('oneTree.t',0)

# Create random starting tree
in_tree_object = readTree.rand_tree(tips=10,brl_avg=1,brl_std=None,verbose='T')

############################## 
#Look at tree and make moves
############################## 
# Print newick string
in_tree_object.newick(in_tree_object.root)

# Make NNI move 
new_tree = readTree.NNI(orig_tree=in_tree_object,node_choice='exponential')

# Print newick string
new_tree.newick(new_tree.root)

# Make multiple trees, each with one NNI move from starting tree. Output as nexus file.
readTree.mult_NNI(in_tree=in_tree_object,num_out_trees=10,out_file='outFile1.t',node_choice='random')



