%%��ͬһ��������ͬ����ŵĻ������ϲ�
clear ;
B=xlsread('C:\Users\win\Desktop\��ģ����\����2��ֵ');%�������ݱ�
N=size(B,1);ssum=0;sssum=0;C=zeros(N,3);num=1;
for k=1:49
     ssum=0;i=1;
for j=1:N
if B(j,1)==k;
    ssum=ssum+1;
end
end
    while i<=ssum
        C(num,:)=B(sssum+i,:);
    if B(sssum+i,2)==B(sssum+i+1,2)
        C(num,3)=B(sssum+i,3)+B(sssum+i+1,3);
        i=i+1;
    end
    num=num+1;i=i+1;
    end
    sssum=sssum+ssum;
end
xlswrite('C:\Users\win\Desktop\��ģ����\4_xlscheck.xls',C);%�����������ݱ���