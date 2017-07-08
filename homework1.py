# -*-coding:utf-8-*-
# python2.7
# 庄建伟
# jupyter notebook上不能正常运行。。
import numpy as np
import pandas as pd

list1 = []
list2 = [chr(i) for i in range(65,91)]
list3 = ['one','two','three','four']


x = np.random.binomial(1,0.5,[26,4])   #生成了26*4服从二项分布的数组
print x
print

for i,j in enumerate(x):      #从数组中选出大于0.5的数据
    for k in x[i]:
        if k > 0.5:
            list1.append(k)
print list1
print

frame = pd.DataFrame(x,list2,list3)   #生成行索引为26个字母，列索引为'one','two','three','four'的dataframe
print frame
print
print frame[[1]]  #  = frame['two']，取出‘two’列的方法
print

print frame.sort_values('two',ascending=False).head(5)  #取出‘two’列排序前五的行
print

#计算‘one’列           等价的做法：# from numpy import sum,median,var
print np.sum(frame['one'])         # = print sum(frame['one'])
print np.median(frame['one'])      # = print median(frame['one'])
print np.var(frame['one'])         # = print var(frame['one'])

#print frame[frame.two>1]#保留dataframe中符合，two>1的数据。
