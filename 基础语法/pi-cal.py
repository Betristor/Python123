from random import random,seed
from time import perf_counter
darts = 1000*1000
hits = 0.0
start = perf_counter()
seed(10)
for i in range(1,darts+1):
    x,y = random(),random()
    if pow(x,2)+pow(y,2)<=1:
        hits += 1
pi = 4*hits/darts
print("圆周率的值为:'{0}'".format(pi))
print("所用的时间为：" + str(int(perf_counter() - start)))