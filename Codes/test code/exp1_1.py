import sys
import glob
import errno
import re
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt 

path = '/Users/akshatgupta/Desktop/New Research/Data set/submitted_runs/trec7.adhoc/*.*'   
files = glob.glob(path)   
print len(files)

pooling_depth = [10,20,30,40,50,60,70,80,90,100]

merge_statistics = []
statistics1 = []
statistics2 = []
statistics = []
initial_statistics = []
topics = [str(i) for i in range(351,401)]
print(len(topics))
for d in pooling_depth:
	count = 0.0 
	lines1 = []
	initial_docs = []
	documents = {}
	doc = []
	total_docs = d * len(files) * len(topics)
	print(total_docs)
	for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
		documents[name] = []
		with open(name, 'r') as f: # No need to specify 'r': this is the default.
			lines = f.read().splitlines()
			for line in lines:
				lines1.append(line.split('\t'))
			for topic in topics:		
				for line in lines1:
					if line[0] == topic:
						initial_docs.append(line[2])
				item = initial_docs[:(3*d)]
			
				documents[name].append(item)
				initial_docs = []

				
		lines1 = []		

	for key,value in documents.iteritems():
		for key1, value1 in documents.iteritems():
			for i in range(0,len(topics)):
				for item in value[i][:d]:
					if item in value1[i][:d]:
						count += 1
		initial_statistics.append(count/total_docs)
		count = 0.0
	print initial_statistics
	statistics.append(initial_statistics)
	initial_statistics = []

	start = d + 1
	end = 2 * d
	for key,value in documents.iteritems():
		for key1, value1 in documents.iteritems():
			for i in range(0,len(topics)):
				for item in value[i][d+1:end]:
					if item in value1[i][:d]:
						count += 1
		initial_statistics.append(count/total_docs)
		count = 0.0
	print initial_statistics
	statistics1.append(initial_statistics)
	initial_statistics = []	

	start = d + 1
	end = 3 * d
	for key,value in documents.iteritems():
		for key1, value1 in documents.iteritems():
			for i in range(0,len(topics)):
				for item in value[i][2*d+1:end]:
					if item in value1[i][:d]:
						count += 1
		initial_statistics.append(count/total_docs)
		count = 0.0
	print initial_statistics
	statistics2.append(initial_statistics)
	initial_statistics = []	

# for i in range(0,len(statistics)):
# 	initial_statistics.append()
print(statistics)
fig1 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax1 = fig1.add_subplot(111)

# Create the boxplot
bp1 = ax1.boxplot(statistics)
ax1.set_xticklabels(pooling_depth)
ax1.set_title('Documents retrieved across different runs for different pool depths')
ax1.set_xlabel('pooling depth d')
ax1.set_ylabel('Documents retrieved across different runs')
# Save the figure
fig1.savefig('leveld7.png', bbox_inches='tight')

fig2 = plt.figure(2, figsize=(9, 6))

# Create an axes instance
ax2 = fig2.add_subplot(111)

# Create the boxplot
bp2 = ax2.boxplot(statistics1)
ax2.set_xticklabels(pooling_depth)
ax2.set_title('Documents retrieved across different runs for pool depths d+1 to 2d ')
ax2.set_xlabel('pooling depth d')
ax2.set_ylabel('Documents retrieved across different runs')
# Save the figure
fig2.savefig('leveld17.png', bbox_inches='tight')

fig3 = plt.figure(3, figsize=(9, 6))

# Create an axes instance
ax3 = fig3.add_subplot(111)

# Create the boxplot
bp3 = ax3.boxplot(statistics2)
ax3.set_xticklabels(pooling_depth)
ax3.set_title('Documents retrieved across different runs for pool depths 2d+1 to 3d ')
ax3.set_xlabel('pooling depth d')
ax3.set_ylabel('Documents retrieved across different runs')
# Save the figure
fig3.savefig('leveld27.png', bbox_inches='tight')
fig1.savefig('leveld7.pdf', bbox_inches='tight')
fig2.savefig('leveld17.pdf', bbox_inches='tight')
fig3.savefig('leveld27.pdf', bbox_inches='tight')