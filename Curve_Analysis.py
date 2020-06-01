import numpy as np
import pandas as pd
from pandas import read_csv
from pandas import DataFrame
from matplotlib import pyplot as plt
import seaborn as sns

series = read_csv('Template_2s10s_Decomposition.csv', header=0, index_col=0)

frame = DataFrame(series)
c1 = frame.iloc[-1]
sum = np.sum(c1, axis =0)
c1_pc = [c1/sum]

av = frame.median()
sum2 = np.sum(av, axis =0)
av_pc = [av/sum2]

print(av)

x = np.arange(219.)
y1 = frame["S 2-3"]
y2 = frame["S 3-4"]
y3 = frame["S 4-5"]
y4 = frame["S 5-6"]
y5 = frame["S 6-7"]
y6 = frame["S 7-8"]
y7 = frame["S 8-9"]
y8 = frame["S 9-10"]
y9 = [y1+y2+y3+y4+y5+y6+y7+y8]

print(sum)

labels = ["2-3", "3-4", "4-5", "5-6", "6-7", "7-8","8-9","9-10"]

gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))

ax1.stackplot(x, y1, y2, y3,y4,y5,y6,y7,y8, labels=labels)
ax1.legend(loc='upper left')
ax1.set_title('Curve Composition')


labels = ["2-3", "3-4", "4-5", "5-6", "6-7", "7-8","8-9","9-10"]

last_m = round(np.transpose(c1),2)
med_m = round(np.transpose(av) - last_m,2)
curve_pc = round(last_m/sum*100)

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

rects1 = ax2.bar(x - width/2, last_m, width, label='Last Observation')
rects2 = ax2.bar(x + width/2, med_m, width, label='Dist to Median')

# Add some text for labels, title and custom x-axis tick labels, etc.

ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax2.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()



ax3.bar(labels, curve_pc, align='center', alpha=0.5)
ax3.set_xticks(x)
ax3.set_xticklabels(labels)
ax3.set_title('Last Observation as % of 2s10s Curve')

plt.show()


print(curve_pc)
fig.tight_layout()
plt.show()

