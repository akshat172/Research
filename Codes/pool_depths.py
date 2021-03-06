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
print len(files)

pooling_depth = [10,20,30,40,50,60,70,80,90,100]

merge_statistics = []
statistics1 = []
statistics2 = []
statistics = []
initial_statistics = []
initial_statistics1 = []
initial_statistics2 = []
topics = [str(i) for i in range(401,451)]
print(len(topics))

for d in pooling_depth:
	pool = []
	count = 0.0 
	count_1 = 0.0
	count_2 = 0.0
	lines1 = []
	initial_docs = []
	#files = files[:4]
	total_docs_perrun = d * len(topics)
	print(total_docs_perrun)


	docs = []
	topic_list = []

	for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
		#print(name)
		
		with open(name, 'r') as f: # No need to specify 'r': this is the default.
			lines = f.read().splitlines()
			# for line in lines:
			# 	lines1.append(line.split('\t'))
			for topic in topics:		
				for line in lines:
					line = line.split('\t')
					if line[0] == topic:
						initial_docs.append(line[2])
				item = initial_docs[:(3*d)]
				topic_list.append(item)
				pool.append(initial_docs[:d])
				#pool1 = list(set(pool))

				# documents[name].extend(item)
			
				#pool.append
				initial_docs = []
			docs.append(topic_list)
			topic_list = []
			#print(docs)
	#print(docs)
	#print(len(pool))
	#print(pool)
	#pool = list(set(pool))
	print("length of docs",len(docs))
	print("length of first",len(docs[0]))
	print("length",len(pool))
	for value in docs:
		for value1 in value:
			#print(value1[2*d:3*d])
			for item in value1[d:2*d]:
				if item not in pool:
					#print(item)
					count_1 += 1
			for item in value1[:d]:
				if item not in pool:
					count += 1
			for item in value1[2*d:3*d]:
				if item not in pool:
					count_2 += 1

		initial_statistics.append(1- count/total_docs_perrun)
		initial_statistics1.append(1-count_1/total_docs_perrun)
		initial_statistics2.append(1-count_2/total_docs_perrun)
		count = 0.0
		count_1 = 0.0
		count_2 = 0.0

	statistics.append(initial_statistics)
	statistics1.append(initial_statistics1)
	statistics2.append(initial_statistics2)
	initial_statistics = []
	initial_statistics1=[]
	initial_statistics2=[]
print(statistics)
print(statistics1)
print(statistics2)


def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(statistics, positions = np.array(xrange(len(statistics)))*3.0-0.8, sym='', widths=0.5)
bpc = plt.boxplot(statistics1, positions = np.array(xrange(len(statistics1)))*3.0, sym='', widths=0.5)
bpr = plt.boxplot(statistics2, positions = np.array(xrange(len(statistics2)))*3.0+0.8, sym='', widths=0.5)

set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpc, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend

plt.xticks(xrange(0, len(pooling_depth) * 3, 3), pooling_depth)
plt.xlim(-2, len(pooling_depth)*3)
plt.ylim(0, 1.5)
# plt.tight_layout()
plt.savefig("pooling_depths_trec8.pdf")
plt.savefig("pooling_depths_trec8.png")

plt.show()


    
with open("results_trec8.txt", "w") as f:
	json.dump(statistics, f)
	#pp = pickle.load(new_filename)
with open("results_trec8_d1.txt", "w") as f:
	json.dump(statistics, f)
with open("results_trec8_d2.txt", "w") as f:
	json.dump(statistics, f)


