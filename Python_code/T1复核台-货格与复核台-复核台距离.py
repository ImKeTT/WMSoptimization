#计算复核台与货格之间距离以及复核台与复核台之间距离
#的上三角矩阵
#输入为完整的货架号码
#x为货格号，y为复核台1-8
def Judge2(x, y):
    d0 = 1000
    L = 800
    G = 750
    x_x = int(case.loc[case[0] == x, 1])
    x_y = int(case.loc[case[0] == x, 2])
    y_x = int(case1.loc[case1[0] == y, 1])
    y_y = int(case1.loc[case1[0] == y, 2])
    D = abs(x_x-y_x)+abs(x_y-y_y)#欧式距离
    x1 = int(x[1:4])
    if (x_x<=y_x+100):
        if (x1&1):
            d = D+0.5*(L-d0)+2*G
        elif(not x1&1):
            d = D-0.5*(L+d0)
    else:
        if (x1&1):
            d = D-1.5*d0+0.5*L
        elif(not x1&1):
            d = D+1.5*(L-d0)+2*G
    return d

#复核台9-13与货格之间的距离
def Judge3(x, y):
    d0 = 1000
    L = 800
    G = 750
    x_x = int(case.loc[case[0] == x, 1])
    x_y = int(case.loc[case[0] == x, 2])
    y_x = int(case1.loc[case1[0] == y, 1])
    y_y = int(case1.loc[case1[0] == y, 2])
    x_flagdown = int(case.loc[case[0] == x[:4]+str(0)+str(1), 2])
    x_flagup = int(case.loc[case[0] == x[:4]+str(1)+str(5), 2])
    D = abs(x_x-y_x)+abs(x_y-y_y)#欧式距离
    f1 = 2*(0.5*L+G+abs(x_y-x_flagdown))
    f2 = 2*(0.5*L+G+abs(x_y-x_flagup))
    if (int(x[1:4])&1):
        if (int((int(x[1:4])-1)/8) == 0):
            d = D-1.5*d0+0.5*L
        else:
            d = D-1.5*d0+0.5*L+min(f1,f2)
    elif(not int(x[1:4])&1):
        d = D+1.5*(L-d0)+2*G+min(f1,f2)
    return d

#复合台之间的距离
def Judge4(x,y):
    x_x = int(case1.loc[case1[0] == x, 1])
    x_y = int(case1.loc[case1[0] == x, 2])
    y_x = int(case1.loc[case1[0] == y, 1])
    y_y = int(case1.loc[case1[0] == y, 2])
    if (x == y):
        d = 0
    else:
        d = abs(x_x-y_x)+abs(x_y-y_y)
    return d

#分别将矩阵写入表格
if __name__ == '__main()__':
    frame = pd.read_excel('result.xlsx', header = None, )
    for i in range(1, 3001):
        for j in range(3001, 3009):
            m = j-3000
            x = case[0][i]
            y = case1[0][m]
            frame[j][i] = Judge2(x, y)#计算1-8
            
    for i in range(1, 3001):
        for j in range(3009, 3014):
            m = j-3000
            x = case[0][i]
            y = case1[0][m]
            frame[j][i] = Judge3(x,y)#计算9-13
            
    for i in range(3001, 3014):
        for j in range(i, 3014):
            m = i-3000
            n = j-3000
            x = case1[0][m]
            y = case1[0][n]
            frame[j][i] = Judge4(x, y)#计算复核台距离
    frame.to_excel('result.xlsx', index = None, header = None)