# from pylab import plot, show, savefig, xlim, figure, \
#                 hold, ylim, legend, boxplot, setp, axes

import sys
import glob
import errno
import re
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt 

pooling_depth = [10,20,30,40,50,60,70,80,90,100]
total_files = []
file_cont = {}
topics = []
docs = {}
initial_docs = []
path = '/Users/akshatgupta/Desktop/New Research/Data set/submitted_runs/trec8.adhoc/*.*'   
files = glob.glob(path)   
print len(files)
for d in pooling_depth:
	total_files.append(d* len(files))


topics = [str(i) for i in range(351,401)]
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
	with open(name, 'r') as f: # No need to specify 'r': this is the default.
		line = f.readline() 	
		while line:
			initial_docs.append(line.strip('\n').split('\t'))
			line = f.readline()
		file_cont[name] = initial_docs
		initial_docs = []
for topic in topics:
	docs[topic] = []
print(docs.keys())

for key in file_cont.keys():
	print(file_cont[key])
	break