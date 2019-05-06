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

pooling_depth = [10,20,30,40,50,60,70,80,90,100,200]
file_cont = {}
docs = []
path = '/Users/akshatgupta/Desktop/New Research/Data set/submitted_runs/trec8.adhoc/*.*'   
files = glob.glob(path)   
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    try:
        with open(name, 'r') as f: # No need to specify 'r': this is the default.
        	line = f.readline()
        	while line:
        		cond = re.search('401\sQ0',line)
        		if cond:
        			docs.append(line.strip('\n').split('\t'))
        		line = f.readline()
        file_cont[name] = docs
        docs = []
        	#sys.stdout.write(f.read())

    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise # Propagate other kinds of IOError.
final_doc_list = []
for d in pooling_depth:
	statistics = {}
	statistics_graph = []
	doc_list = []
	statistics_detailed = {}
	stats = []
	run = []
	count = 0
	final_count = 0
	temp_list = []
	temp_list2 = []
	for key1 in file_cont.keys():
		statistics[key1] = {}
		run.append(key1[76:])
		temp_list = file_cont[key1][0:d]
		for doc in temp_list:
			for key2 in file_cont.keys():
	 			temp_list2 = file_cont[key2][d:(2*d)]
	 			for doc1 in temp_list2:
	 				if doc[2] in doc1:
	 					count = count + 1
			stats.append(count)
			statistics[key1][doc[2]] = count

		doc_list.append(count)
		count = 0
		statistics_detailed[key1] = stats
		statistics_graph.append(stats)
		stats = []
	print doc_list
	final_doc_list.append(doc_list)
# count =0	
# for keys in statistics.keys():
# 	print keys
# 	print statistics[keys]
# 	count = count+1
# 	for keys1 in statistics[keys].keys():
# print count
# print statistics_detailed
# print run
# print doc_list
# print len(doc_list)
# print len(run)
# print len(statistics_graph)

# fig = plt.figure(1, figsize=(20, 16))

# # Create an axes instance
# ax = fig.add_subplot(111)

# # Create the boxplot
# bp = ax.boxplot(statistics_graph[:60])
# ax.set_xticklabels(run[:60],rotation='vertical')
# # Save the figure
# fig.savefig('fig1.png', bbox_inches='tight')
#bp = boxplot(statistics_graph[:30], positions = pos[:30], widths = 0.6)
#show()
fig1 = plt.figure(1, figsize=(20, 16))

# Create an axes instance
ax1 = fig1.add_subplot(111)

# Create the boxplot
bp1 = ax1.boxplot(final_doc_list)
ax1.set_xticklabels(pooling_depth)
ax1.set_title('Documents retrieved across different runs for different pool depths for query 351 ')
ax1.set_xlabel('pooling depth d')
ax1.set_ylabel('Documents retrieved across different runs')
# Save the figure
fig1.savefig('fig2.png', bbox_inches='tight')
#bp = boxplot(statistics_graph[:30], positions = pos[:30], widths = 0.6)
#show()


def setBoxColors(bp):
    setp(bp['boxes'][0], color='blue')
    setp(bp['caps'][0], color='blue')
    setp(bp['caps'][1], color='blue')
    setp(bp['whiskers'][0], color='blue')
    setp(bp['whiskers'][1], color='blue')
    setp(bp['fliers'][0], color='blue')
    setp(bp['fliers'][1], color='blue')
    setp(bp['medians'][0], color='blue')

    setp(bp['boxes'][1], color='red')
    setp(bp['caps'][2], color='red')
    setp(bp['caps'][3], color='red')
    setp(bp['whiskers'][2], color='red')
    setp(bp['whiskers'][3], color='red')
    setp(bp['fliers'][2], color='red')
    setp(bp['fliers'][3], color='red')
    setp(bp['medians'][1], color='red')
# for key in statistics.keys():
#  	print key
#  	print statistics[key]
	 		

