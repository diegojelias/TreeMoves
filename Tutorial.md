```python
# open python
import readTree
# create a newick string
myTreeString = "(P:0.09,(Q:0.07,(X:0.02,((Y:0.03,Z:0.01):0.02,W:0.08):0.06):0.03):0.04);"

# put into tree object
myTree = readTree.Tree(myTreeString)

# make an NNI move on your original tree and make aa new tree object
newTree = readTree.NNI(myTree)

# compare trees
newTree.newick(newTree.root)
myTree.newick(myTree.root)

##Other things to do
# get tip names 
myTree.print_names(myTree.root)
# get tip object
myTree.list_term_nodes(myTree.root)
# get total tree length
myTree.tree_len(myTree.root)
# get instances of all nodes in tree 
myTreeDict = myTree.node_dict(myTree.root)


```