clear;
A=xlsread('C:\Users\win\Desktop\��ģ����\result1_true');
B=xlsread('C:\Users\win\Desktop\��ģ����\����2��ֵ');
n=size(B,1);%B����Ĵ�С��
D=zeros(n,n);
for i=1:n
    for j=i:n
        if i~=j
          a=(floor((B(i,1)/100))-1)*15+mod(B(i,1),100);b=(floor((B(j,1)/100))-1)*15+mod(B(j,1),100);
             D(i,j)=A(a,b);
        else
            D(i,j)=eps;      %i=jʱ�����㣬Ӧ��Ϊ0�����������������Ҫȡ��������eps��������Ծ��ȣ���ʾ
        end
        D(j,i)=D(i,j);   %�Գƾ���
    end
   
end

 xlswrite('C:\Users\win\Desktop\��ģ����\3_T06_D.xls',D);
    