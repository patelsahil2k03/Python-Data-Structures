# print('''Code written by
# SAHIL PATEL
# 20CE101''')

from re import A
import statistics
import panda as pd

sr = pd.Series([10, 25, 3, 25, 24, 6])

mean = sr.mean()
median = sr.median()
mode = sr.mode()
range1 = sr.max() - sr.min();
stdeviation = sr.std(axis=0, skipna=True)

print(mean)
print(median)
print(mode)
print(range1)
print(stdeviation)
print("Variance of sample set is % s"
      % (statistics.variance(sr)))
