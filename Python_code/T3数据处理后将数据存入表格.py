import os
import pandas as pd
import numpy as np
import xlwt

#根据处理过的数据计算两复核台不成圈的情况
file3 = '问题三所有解.xlsx'
lis = []
case3 = pd.read_excel(file3 , header = None, index = False)
root2 = 'C/附件/'
file2 = os.path.join(root2, '附件1：仓库数据.xlsx')
case2 = pd.read_excel(file2, sheetname = '任务单' , header = None, index = False)

def substract(case3):
    minus = 25500#PH03和FH11之间的距离
    row = case3.shape[0]
    i = 1
    F03_F11_dis = []
    while (i<row):
        media = (case3[1][i]*10**5)-minus
        F03_F11_dis.append(round(media, 6))
        i += 4
    return F03_F11_dis
#读取生成货单中货物数量
def genmer(case2, T):
    mer = []
    for i in range(case2.shape[0]):
        if case2[0][i] == T:
            mer.append(case2[3][i])
        
    print(mer)
    return mer
#根据上述计算得到的不同货单时间
T2 = [451600.0, 464100.0, 454400.0]
T3 = [409500.0, 401100.0, 432100.0]
T4 = [439300.0, 438300.0, 463200.0]
T5 = [376000.0, 378100.0, 399000.0]
T6 = [469900.0, 476800.0, 475500.0]
#计算时间
def caltime(mer, dis):
    timeline = []
    for i in dis:
        time = 30
        time += (i/1000)/1.5
        for m in mer:
            if(m<3):
                time += m*5
            elif(m>=3):
                time += m*4
        print(time)
        timeline.append(time)
    mintime = min(timeline)
    index = timeline.index(mintime)
    return index, mintime, timeline
indexT2 , mintimeT2 , timelineT2= caltime(genmer(case2, 'T0002'), T2)
print(indexT2, mintimeT2)
indexT3, mintimeT3, timelineT3 = caltime(genmer(case2, 'T0003'), T3)
indexT4, mintimeT4, timelineT4 = caltime(genmer(case2, 'T0004'), T4)
indexT5, mintimeT5, timelineT5 = caltime(genmer(case2, 'T0005'), T5)
indexT6, mintimeT6, timelineT6 = caltime(genmer(case2, 'T0006'), T6)
index0 = []
for i in range(2, 7):
    index0.append(eval('indexT'+str(i)))
#计算利用率和最小时间mitime
mitime = 0
for i in range(2,7):
    mitime+= eval('mintimeT'+str(i))
#输入货格编号
def jisuan(azhe):
    return 15*int(azhe[1:4])+(int(azhe[4:])-15)
#主函数
if __name__ == '__main__':
    F03_F11_dis = substract(case3)
    n1 = index0.count(1)
    n2 = index0.count(0)
    F3ratio = ((n1+int(n2/2))*30/mitime)*100
    F11ratio = ((int(n2/2)+1)*30/mitime)*100
    
r = []
x = 0
while(x<5):
    r0 = 3*x+(1+x)+index0[x]
    r.append(r0)
    x += 1
case4 = pd.read_excel('3_T02_D.xls' , header = None, index = False)
t2p = []
for i in range(2, 30):
    t2p.append(case3[i][r[0]])
t2p0 = []
for i in t2p:
    t2p0.append(case4[i][0])

case5 = pd.read_excel('3_T03_D.xls' , header = None, index = False)
t3p = []
for i in range(2, 30):
    t3p.append(case3[i][r[1]])
print(t3p)
t3p0 = []
for i in t3p:
    if (np.isnan(i)):
        t3p0.append(0)
    else:
        t3p0.append(case5[i][0])
case6 = pd.read_excel('3_T04_D.xls' , header = None, index = False)
print(case6[0][2])
t4p = []
for i in range(2, 30):
    t4p.append(case3[i][r[2]])
print(t4p)
t4p0 = []
for i in t4p:
    if (np.isnan(i)):
        t4p0.append(0)
    else:
        t4p0.append(case6[i][0])
        
case7 = pd.read_excel('3_T05_D.xls' , header = None, index = False)
t5p = []
for i in range(2, 30):
    t5p.append(case3[i][r[3]])
print(t5p)
t5p0 = []
for i in t5p:
    if (np.isnan(i)):
        t5p0.append(0)
    else:
        t5p0.append(case7[i][0])

case8 = pd.read_excel('3_T06_D.xls' , header = None, index = False)
t6p = []
for i in range(2, 30):
    t6p.append(case3[i][r[4]])
print(t6p)
t6p0 = []
for i in t6p:
    if (np.isnan(i)):
        t6p0.append(0)
    else:
        t6p0.append(case8[i][0])
to_excel = pd.DataFrame({'T02':t2p0, 'T03':t3p0, 'T04':t4p0, 'T05':t5p0, 'T06':t6p0})
to_excel.to_excel('T3.xlsx', index = None, header = True)


    
    #存入附件表格
    nimd = pd.read_excel('C/附件/附件4：计算结果.xlsx' ,sheetname = 'Ques3' ,header = None, index = False)
    print(nimd)
    book = xlsxwriter.Workbook('中转T30.xlsx', {'constant_memory': True})
    sheet = book.add_worksheet('test')
    for i in range(1, nimd.shape[0]):
        print(nimd[2][i])
        if (nimd[2][i][0] == 'S'):
            sheet.write(i, 0, jisuan(nimd[2][i]))
        else:
            sheet.write(i, 0, 0)
        sheet.write(0,i ,jisuan(nimd[i][0]))
        for j in range(case2.shape[0]):
            if case2[0][j] == nimd[1][i]:
                if (case2[2][j] == nimd[2][i]):
                    sheet.write(i, 2, case2[3][j])
                #print(case2[3][j])
    book.close()


