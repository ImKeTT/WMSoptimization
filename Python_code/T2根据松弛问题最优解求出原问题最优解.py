#根据利用蚁群算法计算出来的松弛问题解
#再分情况进行讨论，得到原问题的近似解
import os
import pandas as pd
import numpy as np
import xlwt

root = '../Downloads/'
file = os.path.join(root, '问题2_visit.xls')
file0 = os.path.join(root, '2_5.xls')#要遍历图的点的坐标
file1 = os.path.join(root, '2_4.xls')#要遍历图的权重矩阵
lis = []
#读取表格为dataframe
case = pd.read_excel(file , header = None, index = False)
case0 = pd.read_excel(file0 , header = None, index = False)
case1 = pd.read_excel(file1 , header = None, index = False)
root2 = 'C/附件/'
file2 = os.path.join(root2, '附件1：仓库数据.xlsx')
case2 = pd.read_excel(file2, sheetname = '任务单' , header = None, index = False)

#计算复合台左右索引
index = lis.index(24)#相邻index
left = lis[index-1]
right = lis[index+1]

#计算对应在距离最大矩阵中的行数
#case1是要遍历图的权重矩阵
se_left = case1[0][left]
se_right = case1[0][right]
#计算这两个货格在距离大矩阵(frame)中行数
y_left = 15*int(se_left[1:4])+(int(se_left[4:])-15)
y_right = 15*int(se_right[1:4])+(int(se_right[4:])-15)

#是否替换
def findmin(y, n):
    mi = 9999999#设置较大
    se = []
    for i in range(3001, 3014):
        if (frame[i][y]<mi):
            mi = frame[i][y]
            se.append(i-3000)
    diff = frame[n+3000][y] - mi
    if (diff<=0):
        print("不用换了，就是：%d\t"%n)
    else:
        print("要换哦，差值是：%d\t"%diff)
    return se[-1],  mi

#计算修改后长度
def caldis(index, lis, mi):
    le = len(lis)
    dis = 0
    x = 0
    while(x<le-1):
        #print(case1[lis[index]][lis[index-1]])
        dis += case1[lis[index]][lis[index-1]]
        index -= 1
        x+=1
    dis += mi
    print(dis)
    return dis
    
#计算货单中商品的个数
def genmer(case2, T):
    mer = []
    for i in range(case2.shape[0]):
        if case2[0][i] == T:
            mer.append(case2[3][i])
        
    print(mer)
    return mer

#计算总时间
def caltime(mer, dis):
    time = 30
    time += (dis/1000)/1.5
    for m in mer:
        if(m<3):
            time += m*5
        elif(m>=3):
            time += m*4
    print(time)
    return time


if __name__ == '__main__':
    se1, mi1 = findmin(y_left ,10)
    se2, mi2 = findmin(y_right, 10)
    dis = caldis(index, lis, mi2) #最短长度
    mer = genmer(case2, 'T0001')#货单商品
    time = caltime(mer, dis)#最终时间