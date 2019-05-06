import sys
import glob
import errno
import re
import matplotlib.pyplot as plt
import numpy as np
import json

## agg backend is used to create plot as a .png file
#mpl.use('agg')

#import matplotlib.pyplot as plt 

path = '/Users/akshatgupta/Desktop/New Research/Data set/submitted_runs/trec8.adhoc/*.*'   
files = glob.glob(path)   
print(len(files))
topics = [str(i) for i in range(401,451)]

print(len(topics))
#files = files[:2]
pooling_depth = [5,10]
pool_lengths = []

file_contents = {}
partial_list = []
for name in files:
	file_contents[name] = []
	with open(name) as f: # No need to specify 'r': this is the default.
		lines = f.read().splitlines()
		for i in range(0,50):		
			for line in lines:
				line = line.split('\t')
				if line[0] == topics[i]:
					partial_list.append(line[2])
			file_contents[name].append(partial_list)
			partial_list = []

pooling_depths = [5]
pool = [[] for i in range(0,50)]
pool_lengths = []
for d in pooling_depths:
    partial_pool = []
    for i in range(0,50):
        for key, value in file_contents.items():
            partial_pool.extend(value[:d])
        pool[i] = partial_pool
        partial_pool = []

for i in range(0,50):
	pool[i] = set(pool[i])
	#overall_pool.extend(pool[i])
	count_pool = count_pool+len(pool[i])
	pool_lengths.append(count_pool)
	print(count_pool)
print(pool_lengths)
print(pool)
            

# p = 0.8

# for d in pooling_depth:
# 	initial_docs = []
# 	pool = []
# 	sort_pool = []
# 	pool = [[] for i in range(0,50)]
# 	for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
# 		#print(name)
		
# 		with open(name) as f: # No need to specify 'r': this is the default.
# 			lines = f.read().splitlines()
# 			# for line in lines:
# 			# 	lines1.append(line.split('\t'))
# 			for i in range(0,50):		
# 				for line in lines:
# 					line = line.split('\t')
# 					if line[0] == topics[i]:
# 						initial_docs.append(line[2])
# 				pool[i].extend(initial_docs[:d])
# 				initial_docs = []
# 				#pool[i] = set(pool[i])
# 	count_pool = 0
# 	for name in files:
# 		with open(name) as f: # No need to specify 'r': this is the default.
# 			lines = f.read().splitlines()
# 			ffor i in range(0,50):		
# 				for line in lines:
# 					line = line.split('\t')
# 					if line[0] == topics[i]:

	
# print(pool_lengths)  