import os
import pandas as pd
import numpy as np
import xlwt

file4_0 = 'T4/4_1.xlsx'
case4_0 = pd.read_excel(file4_0 , header = None, index = False)
case4_1 = pd.read_excel('T4/4_xlscheck.xls' , header = None, index = False)
case4_2 = pd.read_excel('T4/4_2_People.xls' , header = None, index = False)
case4_3 = pd.read_excel('T4/中转T4.xlsx' , header = None, index = False)
#计算两个复核台之间距离
def gap(a, b):
    return frame[3001+int(b)][3001+int(a)]
#判断函数
def J(a):
    i = a.index(max(a))
    if ((i<len(a)-1 and a[i+1]==max(a)-1) or a[i-1] == max(a)-1):
        return True
    elif(i == len(a) and a[0] == max[a]-1):
        return True
    else:
        return False

#预处理成表格进行算法实现
def substract0(cas, n):
    mini = 9999999
    re = []
    x = 3
    for k in range(cas.shape[0]):
        i = (n-1)*10+k
        s = (cas[1][i]).split(' ')
        #print(s)
        a = []
        for j in range(3, cas.shape[1]):
            if (cas[j][i]!=0):
                a.append(cas[j][i])
            else:
                break
        print(len(a))
        if ((cas[2][i] - gap(s[0], s[1]))<mini):
            if (s[0] != s[1] and J(a)):
                re.append(k)
                mini = cas[2][i] - gap(s[0], s[1])
            elif(s[0] == s[1]):
                re.append(k)
                mini = cas[2][i] - gap(s[0], s[1])
    #print(re)
    li = []
    for j in range(3, cas.shape[1]):
        if (cas[j][re[-1]+(n-1)*10]!=0):
            li.append(cas[j][re[-1]+(n-1)*10])
        else:
            break
    sm = (cas[1][re[-1]+(n-1)*10]).split(' ')
    return mini, re[-1], sm, li

#计算每个货单的挑货时间
def genmer(case, T):
    mer = []
    for i in range(case.shape[0]):
        if case[0][i] == T:
            mer.append(case[2][i])
        
    print(mer)
    return mer
mer = genmer(case4_1, 1)

def calptime(mer):
    time = 30
    for m in mer:
        if(m<3):
            time += m*5
        elif(m>=3):
            time += m*4
    print(time)
    return time
#定义结构体
class merc:
    def __init__(self, s, e, mintime, num, state, li):
        self.s = s#起始点
        self.e = e#终止点
        self.mintime = mintime#最小耗时
        self.num = num#所属货单号
        self.state = state#状态
        self.li = li#货物编号
      
    
#最终计算结果
def ultim(mertime, case4_0):
    merclist = []
    for n in range(1,50):
        m = (n-1)*10
        mini, rec, sm, li= substract0(case4_0[m:m+9], n)
        print(sm)
        mintime = ((mini/1000)/1.5)+mertime[n-1]
        #print((mini/1000)/1.5)
        a = merc(sm[0], sm[1], mintime, n, 0, li)
        #print(sm[0])
        merclist.append(a)
        if (sm[0] != sm[1]):
            b = merc(sm[1], sm[0], mintime, n, 0, li)
            merclist.append(b)
        #print(merclist[0].mintime)
    return merclist
#排序准则
def take(a):
    return a.mintime

if __name__ == '__main__':
    mertime = []
    for i in range(49):
        mertime.append(calptime(genmer(case4_1, i+1)))
    merclist = ultim(mertime, case4_0)
    merclist.sort(key = take)#按照耗时长短进行排序
    book = xlsxwriter.Workbook('T4/中转T4.xlsx', {'constant_memory': True})
    sheet = book.add_worksheet('test')
    for i in range(len(merclist)):
        sheet.write(i, 0, merclist[i].num)
        sheet.write(i, 1, merclist[i].state)
        sheet.write(i, 2, merclist[i].mintime)
        sheet.write(i, 3, merclist[i].s)
        sheet.write(i, 4, merclist[i].e)
        sheet.write(i, 5, merclist[i].li)
    book.close()