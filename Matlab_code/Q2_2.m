clear;
A=xlsread('C:\Users\win\Desktop\��ģ����\2020��MathorCup��У��ѧ��ģ��ս����Ŀ\C\����\����1���ֿ�����.xlsx','����');
B=xlsread('C:\Users\win\Desktop\��ģ����\����2��ֵ');
D=B(:,1);
n=size(D,1);
C=A(:,1:2);
P=zeros(n,2);
 for i=1:n
          a=(floor((D(i,1)/100))-1)*15+mod(D(i,1),100);
             P(i,1:2)=C(a,1:2);
 end
 xlswrite('C:\Users\win\Desktop\��ģ����\3_P.xls',P);