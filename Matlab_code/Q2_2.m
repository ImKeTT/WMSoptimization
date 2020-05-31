clear;
A=xlsread('C:\Users\win\Desktop\建模国赛\2020年MathorCup高校数学建模挑战赛题目\C\附件\附件1：仓库数据.xlsx','货格');
B=xlsread('C:\Users\win\Desktop\建模国赛\问题2初值');
D=B(:,1);
n=size(D,1);
C=A(:,1:2);
P=zeros(n,2);
 for i=1:n
          a=(floor((D(i,1)/100))-1)*15+mod(D(i,1),100);
             P(i,1:2)=C(a,1:2);
 end
 xlswrite('C:\Users\win\Desktop\建模国赛\3_P.xls',P);