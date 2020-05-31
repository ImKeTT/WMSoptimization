def jisuan(azhe):
    return 15*int(azhe[:-2])+(int(azhe[-2:])-15)
#定义结构体
class worker:
    def __init__(self, worklist):
        self.worklist = worklist
#寻找对应的任务单
def findjob(case4_2):
    worklist = []
    for j in range(9):
        num = []
        for i in range(int((case4_2.shape[0]-1)/2)):
            if (not np.isnan(case4_2[j*2][2*i])):
                com = case4_2[j*2][2*i+1]-case4_2[j*2][2*i]
                #print(com)
                for k in range(case4_3.shape[0]):
                    if (round(com,2) == round(case4_3[2][k],2) and case4_2[j*2+1][2*i] 
                        == case4_3[3][k] and case4_2[j*2+1][2*i+1] == case4_3[4][k]):
                        num.append(case4_3[0][k])
                        #print(num)
        b = worker(num)
        worklist.append(b)
    return worklist
#特殊字符处理
def w(a):
    if int(a/10) == 0:
        return 'T000'+str(a)
    else:
        return 'T00'+str(a)

def w2(a):
    if int(a/10) == 0:
        return 'FH0'+str(int(a))
    else:
        return 'FH'+str(int(a))

def w3(a):
    if int(a/10) == 0:
        return 'S0000'+str(a)
    elif(int(a/100) == 0):
        return 'S000'+str(a)
    elif(int(a/1000) == 0):
        return 'S00'+str(a)
    elif(int(a/10000) == 0):
        return 'S0'+str(a)
    else:
        return 'S'+str(a)

#写入附件表格
def wi(shuru):
    leng = 0
    for i in range(shuru):
        l = len(worklist[i].worklist)
        for j in range(l):
            h = i+1
            sheet.write(leng, 0, 'P'+str(h))
            sheet.write(leng, 1, w(worklist[i].worklist[j]))
            sheet.write(leng, 2, w2(case4_2[2*i+1][2*j]))
            sheet.write(leng, 3, 3000+case4_2[2*i+1][2*j])
            sheet.write(leng, 4, 0)
            leng+=1
            for k in range(case4_1.shape[0]):
                if case4_1[0][k] == worklist[i].worklist[j]:
                    sheet.write(leng, 0, 'P'+str(h))
                    sheet.write(leng, 1, w(worklist[i].worklist[j]))
                    sheet.write(leng, 2, w3(int(case4_1[1][k])))
                    sheet.write(leng, 3, jisuan(str(case4_1[1][k])))
                    sheet.write(leng, 4, case4_1[2][k])
                    leng += 1
    book.close()
    
if __name__ == '__main__':
    worklist = findjob(case4_2)
    book = xlsxwriter.Workbook('T4/附件T4.xlsx', {'constant_memory': True})
    sheet = book.add_worksheet('test') 
    wi(9)