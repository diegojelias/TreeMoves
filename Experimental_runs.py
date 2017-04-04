
#!/usr/bin/env python

from __future__ import (division, print_function)
from readTree import Node
from readTree import Tree
import readTree
import dendropy 

'''
NNI = number moves
TIPS = number of tips in starting tree
TREES = number of output trees
START = out file for starting tree
OUT = out file for NNI move trees
'''

def write_single_tree(in_tree_object):
	# turn into newick
	newick_tree = in_tree_object.newick(in_tree_object.root) + ";"
	# read into dendropy
	dp_tree = dendropy.Tree.get(data=newick_tree, schema='newick')
	# write to file
	dp_tree.write(path=start_tree_outfile, schema='nexus')

############################
# Default. Ignore
############################
brl_avg = 1
brl_std = None
node_choice = 'random'
no_dup_start = 'T'

############################
# Constant variables for all conditions
############################
TREES = 100

############################
# Start trees
############################
in_tree_10 = readTree.rand_tree(tips=10,brl_avg=brl_avg,brl_std=brl_std,verbose='F')
in_tree_50 = readTree.rand_tree(tips=50,brl_avg=brl_avg,brl_std=brl_std,verbose='F')
in_tree_100 = readTree.rand_tree(tips=100,brl_avg=brl_avg,brl_std=brl_std,verbose='F')


############################
# One NNI Move
############################
NNI = 1
START = in_tree_10
OUT = '10_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)

START = in_tree_50
OUT = '50_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)

START = in_tree_100
OUT = '100_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)

############################
# Four NNI Move
############################
NNI = 4
START = in_tree_10
OUT = '10_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)

START = in_tree_50
OUT = '50_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)

START = in_tree_100
OUT = '100_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)
############################
# Eight NNI Move
############################
NNI = 8
START = in_tree_10
OUT = '10_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)

START = in_tree_50
OUT = '50_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)

START = in_tree_100
OUT = '100_tips_'+str(NNI)+'_nni.trees'

readTree.NNI_mult_trees(in_tree=START, num_out_trees=TREES,num_nni_moves=NNI, out_file=OUT, node_choice=node_choice, no_dup_start_tree=no_dup_start)
