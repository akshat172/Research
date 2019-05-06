import sys
import glob
import errno
import re
import matplotlib.pyplot as plt
import numpy as np
import pickle
import json
from matplotlib import style
from numpy import median
style.use('ggplot')

with open("results_trec7.txt", "rb") as f:
	statistics = json.load(f)
	#pp = pickle.load(new_filename)
with open("results_trec7_d1.txt", "rb") as f:
	statistics1 = json.load(f)
with open("results_trec7_d2.txt", "rb") as f:
	statistics2 = json.load(f)


median0 = []
median1 = []
median2 = []

for item in statistics:
	# print(item)
	median0.append(median(item))
for item in statistics1:
	# print(item)
	median1.append(median(item))
for item in statistics2:
	# print(item)
	median2.append(median(item))

# print(median0)
# print(median1)
# print(median2)

pooling_depth = [10,20,30,40,50,60,70,80,90,100]

from statistics import mean


# xs = np.array([1,2,3,4,5], dtype=np.float64)
# ys = np.array([5,4,6,5,6], dtype=np.float64)

def best_fit_slope(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m,b

m1,b1 = best_fit_slope(np.array(pooling_depth, dtype=np.float64),np.array(median0, dtype=np.float64))
m2,b2 = best_fit_slope(np.array(pooling_depth, dtype=np.float64),np.array(median1, dtype=np.float64))
m3,b3 = best_fit_slope(np.array(pooling_depth, dtype=np.float64),np.array(median2, dtype=np.float64))
print("slope of best fit at leveld",m1,"\nintercept at leveld",b1)
print("slope of best fit at leveld",m2,"\nintercept at leveld",b2)
print("slope of best fit at leveld",m3,"\nintercept at leveld",b3)
# print(b)

regression_line1 = [(m1*x)+b1 for x in pooling_depth]
regression_line2 = [(m2*x)+b2 for x in pooling_depth]
regression_line3 = [(m3*x)+b3 for x in pooling_depth]


def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure(1)

bpl = plt.boxplot(statistics, positions = np.array(range(len(statistics)))*3.0-0.8, sym='', widths=0.5)
bpc = plt.boxplot(statistics1, positions = np.array(range(len(statistics1)))*3.0, sym='', widths=0.5)
bpr = plt.boxplot(statistics2, positions = np.array(range(len(statistics2)))*3.0+0.8, sym='', widths=0.5)

set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpc, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend


plt.xticks(range(0, len(pooling_depth) * 3, 3), pooling_depth)
plt.xlim(-2, len(pooling_depth)*3)
plt.ylim(0, 1.5)
plt.xlabel('Pooling depth d')
plt.ylabel('Fraction of documents retrieved across different runs')
# plt.plot(pooling_depth, regression_line)
# plt.tight_layout()
plt.savefig("pooling_depths_trec7.pdf")
plt.savefig("pooling_depths_trec7.png")

# plt.show()

fig = plt.figure(2)
ax = fig.add_subplot(111)
ax.plot([1,2,3,4,5,6,7,8,9,10],regression_line1)
bp = ax.boxplot(statistics, sym='',widths=0.5)

ax.set_xticklabels(pooling_depth)
ax.set_ylim(0,1.2)
ax.set_xlabel('pooling depth d')
ax.set_ylabel('Fraction of documents retrieved across different runs')
fig.savefig("best_fit_1_trec7.pdf")
fig.savefig("best_fit_1_trec7.png")
# plt.xticks(range(0, len(pooling_depth) * 3, 3), pooling_depth)
# plt.xlim(-2, len(pooling_depth)*3)
# plt.ylim(0, 1.5)

#plt.plot(pooling_depth, regression_line1)
# plt.plot(pooling_depth, regression_line2)
# plt.plot(pooling_depth, regression_line3)
fig1 = plt.figure(3)
ax1 = fig1.add_subplot(111)
ax1.plot([1,2,3,4,5,6,7,8,9,10],regression_line2)
bp1 = ax1.boxplot(statistics1, sym='',widths=0.5)

ax1.set_xticklabels(pooling_depth)
ax1.set_ylim(0,1.2)
ax1.set_xlabel('pooling depth d')
ax1.set_ylabel('Fraction of documents retrieved across different runs')
fig1.savefig("best_fit_2_trec7.pdf")
fig1.savefig("best_fit_2_trec7.png")

fig2 = plt.figure(4)
ax2 = fig2.add_subplot(111)
ax2.plot([1,2,3,4,5,6,7,8,9,10],regression_line3)
bp2 = ax2.boxplot(statistics2, sym='',widths=0.5)

ax2.set_xticklabels(pooling_depth)
ax2.set_ylim(0,1.2)
ax2.set_xlabel('pooling depth d')
ax2.set_ylabel('Fraction of documents retrieved across different runs')

fig2.savefig("best_fit_3_trec7.pdf")
fig2.savefig("best_fit_3_trec7.png")

plt.show()

