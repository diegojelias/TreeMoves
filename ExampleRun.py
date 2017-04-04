
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
doo="(P:0.09,(Q:0.07,(X:0.02,((Y:0.03,Z:0.01):0.02,W:0.08):0.06):0.03):0.04)"
boo="(P:0.01,(Q:0.01,(X:0.01,((Y:0.01,Z:0.01):0.01,W:0.01):0.01):0.01):0.01)"
Zim = Tree(boo)
Zim.newick(Zim.root)
Jim = readTree.NNI(Zim,'exponential')
Jim.newick(Jim.root)



for key, value in n_dict.items():
		if value == start_brl:
				start_node = key




############################## 
'''
Wrap in function later - user
Reads in tree from nexus file and turn into readTree.Tree object
'''
############################## 

# Read in tree from nexus file and transform to newick string
t = dendropy.Tree.get(path="oneTree.t",schema="nexus",tree_offset=0)
# Convert tree to newick string and strip whitespace characters.
n = t.as_string(schema='newick').strip()
# Convert to readTree Tree object
treeOG = Tree(n)
# print newick string
treeOG.newick(treeOG.root)
return treeOG

############################## 
'''
Make random tree. 
Input total number of tips, average brl and std for branch length
'''
############################## 
tips=5
brl_avg=1
brl_std=None
# Create random tree
rand_tree = Phylo.BaseTree.Tree.randomized(taxa=tips,branch_length=brl_avg,branch_stdev=brl_std)
# View tree
Phylo.draw_ascii(rand_tree)
# Convert to newick string, strip trailing whitespace
rand_newick = rand_tree.format('newick').strip()
# Remove root branch length of 0
rand_newick2 = re.sub(':0.00000;',';',rand_newick)
# Remove node names, use this to read into dendropy
no_nodes_dp = re.sub('\)n\d+:','):',rand_newick2)
# Remove trailing ";" use this to read into readTree
no_nodes = no_nodes_dp.strip(';')
# Print newick string
print(no_nodes)
# Convert to readTree Tree object
tree_random = Tree(no_nodes)
tree_random.newick(tree_random.root)

#return tree_random. # this works sometimes
readTree.NNI(tree_random)




############################## 
'''
#Test after readTree.NNI() works
Does one NNI move on starting readTree and outputs to file
Input starting tree, number of out trees
'''
############################## 
# Get input. Make a newick string
num_out_trees = 10
out_file = "outTrees.t"
in_tree = tree_random

in_tree_newick = in_tree.newick(in_tree.root)

# Start dendropy tree list with starting input tree
treez = dendropy.TreeList()
treez.append(dendropy.Tree.get(data=no_nodes_dp, schema='newick'))

for i in range(num_out_trees):
	new_tree = readTree.NNI(in_tree)
	new_tree = new_tree.newick(new_tree.root)+";"
	nni_tree = dendropy.Tree.get(data=new_tree, schema='newick')
	treez.append(nni_tree)


treez.write(path=out_file, schema='nexus')




############################## 
doo="(P:0.09,(Q:0.07,(X:0.02,((Y:0.03,Z:0.01):0.02,W:0.08):0.06):0.03):0.04)"
Zim = Tree(doo)
readTree.NNI(Zim)


Jim = Tree(doo)

Jim.newick(Jim.root)
Zim.newick(Zim.root)
readTree.NNI(Zim)
Jim.newick(Jim.root)
Zim.newick(Zim.root)

data = "(A:0.3,((B:0.05,C:0.1):0.15,D:0.2):0.5)"
Sim = Tree(data)


for key, value in Jim.node_dict(Jim.root).items():
	print(key.name)



