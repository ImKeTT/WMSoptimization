#T1计算货格之间的距离
import os
import pandas as pd
import numpy as np
import xlwt

root = 'C/附件/'
file = os.path.join(root, '附件1：仓库数据.xlsx')
case = pd.read_excel(file, sheetname = '货格' , header = None, index = False)

def Judge(x, y):
    if ((x&1 and y&1)or(not x&1 and not y&1)):
        if (int((x-1)/8) == int((y-1)/8)):
            return 1
        else:
            return 2
    elif( x&1 and not y&1):
        if (x%8+1 == y%8):
            return 3
        else:
            return 4
    elif(not x&1 and y&1):
        if (x%8-1 == y%8):
            return 5
        else:
            return 6
        
def cal(flag, a, b):
    G = 750#绕过障碍物的间隔
    L = 800#货格的边长
    #提取坐标
    x0 = int(case.loc[case[0] == a, 1])
    y0 = int(case.loc[case[0] == a, 2])
    x1 = int(case.loc[case[0] == b, 1])
    y1 = int(case.loc[case[0] == b, 2])
    #对应最底部的箱格y坐标
    y0_flagdown = int(case.loc[case[0] == a[:4]+str(0)+str(1), 2])
    y1_flagdown = int(case.loc[case[0] == b[:4]+str(0)+str(1), 2])
    y0_flagup = int(case.loc[case[0] == a[:4]+str(1)+str(5), 2])
    y1_flagup = int(case.loc[case[0] == b[:4]+str(1)+str(5), 2])
    D = abs(x0-x1)+abs(y0-y1)#欧式距离
    f1 = 2*(0.5*L+G+min(abs(y0-y0_flagdown), abs(y1-y1_flagdown)))
    f2 = 2*(0.5*L+G+min(abs(y0-y0_flagup), abs(y1-y1_flagup)))
    choose = int(a[4:])+int(b[4:])#判断从上走还是从下走
    if(flag == 1):
        d = D+2*G
    elif(flag == 2):
        if (choose<=15):
            d = 2*G+D+f1
        else:
            d = d = 2*G+D+f2
    elif(flag == 3):
        if(choose<=15):
            d = D+4*G+L+f1
        else:
            d = D+4*G+L+f2
    elif(flag == 4):
        d = D+4*G+L
    elif (flag == 5):
        if (choose<=15):
            d = D-L+f1
        else:
            d = D-L+f2
    elif(flag == 6):
        d = D+4*G
    return d

#求解上三角矩阵写入表格
def Dis(case):
    book = xlsxwriter.Workbook('result.xlsx', {'constant_memory': True})
    sheet = book.add_worksheet('test')
    for i in range(1, 3001):
        sheet.write(i, i, 0)
        for j in range(i+1, 3001):
            x = int(case[0][i][1:4])
            y = int(case[0][j][1:4])
            flag = Judge(x, y)
            sheet.write(i, j, cal(flag, case[0][i], case[0][j]))
            sheet.write(j, i, cal(flag, case[0][i], case[0][j]))
            
    book.close()
    
if __name__ == '__main__':
    Dis(case)