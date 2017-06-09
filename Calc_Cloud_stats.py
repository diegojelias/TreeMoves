
#!/usr/bin/env python
############################## 

############################## 

from __future__ import (division, print_function)
import dendropy
import re
import os
import numpy

def cluster_density_avg(in_file,NNI_trees,starting_tree_number=0):
	'''
	Input number of NNI trees = total trees - start tree
	Compares all NNI created cloud trees to initial seed tree. 
	Counts trees from 0
	'''
	nRF_list = []
	x = starting_tree_number + 1
	y = x + NNI_trees -1
	# print(x,y)
	version = dendropy.__version__.split(".")[0]
	if version == '4':
		for i in range(x,y):
			taxa = dendropy.TaxonNamespace()
			in_tree = dendropy.Tree.get(path=in_file,schema="nexus",taxon_namespace=taxa, tree_offset=starting_tree_number,rooting='force-rooted')
			new_tree = dendropy.Tree.get(path=in_file,schema="nexus",taxon_namespace=taxa, tree_offset=i,rooting='force-rooted')
			in_tree.encode_bipartitions()
			new_tree.encode_bipartitions()
			dist=dendropy.calculate.treecompare.symmetric_difference(in_tree,new_tree)
			print(dist)
			max_RF = 2*(len(taxa)-2)
			norm_dist = dist/max_RF
			both = [dist,norm_dist]
			nRF_list.append(norm_dist)
	elif version == '3':
		for i in range(x,y):
			taxa = dendropy.TaxonSet() 
			in_tree = dendropy.Tree.get_from_path(path=in_file,schema="nexus", taxon_set=taxa, tree_offset=starting_tree_number,rooting='force-rooted')
			new_tree = dendropy.Tree.get_from_path(path=in_file,schema="nexus",taxon_set=taxa, tree_offset=i,rooting='force-rooted')
			in_tree.encode_bipartitions()
			new_tree.encode_bipartitions()
			dist=dendropy.calculate.treecompare.symmetric_difference(in_tree,new_tree)
			max_RF = 2*(len(taxa)-2)
			norm_dist = dist/max_RF
			both = [dist,norm_dist]
			nRF_list.append(norm_dist)
	return numpy.mean(nRF_list)
			

def calc_clouds(filePrefix,cloudSize):
	for i in range(1,11):
		# Title run
		name = str(filePrefix)+str(i)
		# Total out trees per cloud
		cloud_size = cloudSize
		print(str(name))
		print("Calculating stats on clouds...")
		# Calculate average density of each cloud
		RF_cloud1 = cluster_density_avg(in_file='%s_cloud.nex' % name, NNI_trees= int(cloud_size)-1, starting_tree_number=0)
		RF_cloud2 = cluster_density_avg(in_file='%s_cloud.nex' % name, NNI_trees= int(cloud_size)-1, starting_tree_number=cloud_size)
		#RF_cloud1 = 'Slithy'
		#RF_cloud2 = 'Toves'
		print("Writing values to log files...")
		# Write to log file
		mainDir = os.getcwd()
		log_file = os.path.join(mainDir, str(name)+'.log')
		with open(log_file, "r+") as f:
			filedata = f.read()
			filedata = re.sub("RF_calc1: twas","RF_calc1:"+str(RF_cloud1), filedata)
			filedata = re.sub("RF_calc1: brillig","RF_calc2:"+str(RF_cloud2), filedata)
			f.seek(0)
			f.write(filedata)
			f.truncate()

def main():
	calc_clouds('10tip_1000trees_0.125_1.0start_',100)
	calc_clouds('10tip_1000trees_0.125_1.0start_',1000)
	calc_clouds('10tip_1000trees_0.125_0.5start_',100)
	calc_clouds('10tip_1000trees_0.125_0.5start_',1000)


if __name__=='__main__':
	main()
