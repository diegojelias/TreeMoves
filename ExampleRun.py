
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
import readTree
import dendropy
from cStringIO import StringIO
from Bio import Phylo

############################################################ 
#Scratch paper
############################################################
############################## 
# rf distances
############################## 

############################## 
# Iterate through file
############################## 

readTree.compare_tree_file(in_file='outFile1.t',total_trees=11,distance_metric="uRF")



############################## 
# compare topology in python
############################## 
# Read in original tree and NNI tree
in_tree_object=readTree.read_nexus('outFile1.t',0)
new_tree_object=readTree.read_nexus('outFile1.t',8)

# Visualize trees with biopython
tree_object1=in_tree_object
tree_object2=new_tree_object
tree_newick1 = StringIO(tree_object1.newick(tree_object1.root))
tree_newick2 = StringIO(tree_object2.newick(tree_object2.root))
tree1 = Phylo.read(tree_newick1, "newick")
tree2 = Phylo.read(tree_newick2, "newick")
print("Tree 0")
print(tree_object1.newick(tree_object1.root))
Phylo.draw_ascii(tree1)
print("Tree 8")
print(tree_object2.newick(tree_object2.root))
Phylo.draw_ascii(tree2)

rf_unweighted(in_tree_object,new_tree_object)

#Tree 0 
(P:0.09,(Q:0.07,(X:0.02,((Y:0.03,Z:0.01):0.02,W:0.08):0.06):0.03):0.04)

#Tree 8
((P:0.09,Q:0.07):0.04,(X:0.02,((Y:0.03,Z:0.01):0.02,W:0.08):0.06):0.03)


############################################################  
#Scratch paper. works
############################################################  
############################## 
# compare RF of input tree and 1 NNI move tree
############################## 
def rf_unweighted(tree_object1,tree_object2): 
	tree_newick1 = tree_object1.newick(tree_object1.root)+";"
	tree_newick2 = tree_object2.newick(tree_object2.root)+";"
	print(tree_newick1)
	print(tree_newick2)
	taxa = dendropy.TaxonNamespace() #set taxa same for all 
	tree1=dendropy.Tree.get(data=tree_newick1,schema='newick',taxon_namespace=taxa)
	tree2=dendropy.Tree.get(data=tree_newick2,schema='newick',taxon_namespace=taxa)
	dist=dendropy.calculate.treecompare.symmetric_difference(tree1,tree2)
	return dist

boo="(P:0.01,(Q:0.01,(X:0.01,((Y:0.01,Z:0.01):0.01,W:0.01):0.01):0.01):0.01)"
# Create readTree.tree object
in_tree_object = Tree(boo)
new_tree_object = readTree.NNI(orig_tree=in_tree_object,node_choice='exponential')
rf_unweighted(tree_object1=in_tree_object,tree_object2=new_tree_object)

############################## 
# print out 
############################## 
# Visualize trees with biopython
tree_object1=in_tree_object
tree_object2=new_tree_object
def view_phylo(tree_object):
	tree_newick = StringIO(tree_object.newick(tree_object.root))
	tree = Phylo.read(tree_newick, "newick")
	print("Tree")
	print(tree_object.newick(tree_object.root))
	Phylo.draw_ascii(tree)

###############################################################################
#Examples of working parts
###############################################################################

############################## 
#Input tree options
############################## 
# From string
doo="(P:0.09,(Q:0.07,(X:0.02,((Y:0.03,Z:0.01):0.02,W:0.08):0.06):0.03):0.04)"
boo="(P:0.01,(Q:0.01,(X:0.01,((Y:0.01,Z:0.01):0.01,W:0.01):0.01):0.01):0.01)"
# Create readTree.tree object
in_tree_object = Tree(doo)

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
new_tree_object = readTree.NNI(orig_tree=in_tree_object,node_choice='exponential')

# Print newick string
new_tree_object.newick(new_tree_object.root)

# Make multiple trees, each with one NNI move from starting tree. Output as nexus file.
readTree.NNI_mult_trees(in_tree=in_tree_object,num_out_trees=10,out_file='outFile1.t',node_choice='random')




