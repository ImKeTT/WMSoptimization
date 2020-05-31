clear;
G=xlsread('C:\Users\win\Desktop\建模国赛\4_2_E_all.xls');
F=zeros(3*2^9,13);
H=zeros(2^9,2);
for k=1:2^9
    A=xlsread('C:\Users\win\Desktop\建模国赛\中转t42.xlsx');
    B=zeros(100,18);C=zeros(9,3);D=zeros(3,13);
    E=zeros(9,3);
E=G(1+(k-1)*9:9+(k-1)*9,:);
num=0;N=size(A,1);
B(1,:)=2;

for i=1:9
B(2,2*i-1:2*i)=[0 E(i,2)];
end
C=E;
while num <=40
    plog=0;plog2=0;plog1=0;
    for i=1:9
        if C(i,1)==min(C(:,1))
           mip=i; 
        end
    end
        B(B(1,2*mip)+1,2*mip-1:2*mip)=[B(B(1,2*mip)+1,2*mip-1)+C(mip,1) C(mip,3)];
        if D(1,C(mip,3))-B(B(1,2*mip)+1,2*mip-1)<=30 && D(1,C(mip,3))-B(B(1,2*mip)+1,2*mip-1)>0
            D(1,C(mip,3))=C(mip,1)+30+D(1,C(mip,3))-B(B(1,2*mip)+1,2*mip-1);
            D(2,C(mip,3))=30+D(1,C(mip,3))-B(B(1,2*mip)+1,2*mip-1)+D(2,C(mip,3));
        else
           D(1,C(mip,3))=C(mip,1)+30;
           D(2,C(mip,3))=30+D(2,C(mip,3));
            D(3,C(mip,3))=30+D(3,C(mip,3));
        end
        B(B(1,2*mip)+2,2*mip-1:2*mip)=[ D(1,C(mip,3)) C(mip,3)];
        num=num+1;
        for i=1:N
            if A(i,2)==0 && A(i,4)==B(B(1,2*mip)+2,2*mip) && plog==0
                c=i;
             C(mip,:)=[D(1,C(mip,3))+A(i,3) A(i,4:5)];   
        if A(i,4)==A(i,5)
            A(i,2)=1;
        else
            for j=1:N 
                if A(j,1)==A(i,1)&&plog2==0
                   A(j:j+1,2)=1;
                   plog2=1;
                end
            end
        end
         plog=1;
            end
        end
        B(1,2*mip)=B(1,2*mip)+2;
         
end
if A(:,2)==1
              plog1=1; 
           end
F(1+(k-1)*3:3+(k-1)*3,:)=D;
H(k,1)=max(C(:,1));
    H(k,2)=plog1;
end
%xlswrite('C:\Users\win\Desktop\建模国赛\4_2_FH.xls',D);
%xlswrite('C:\Users\win\Desktop\建模国赛\4_2_People.xls',B);
%xlswrite('C:\Users\win\Desktop\建模国赛\4_2_Time.xls',F);
xlswrite('C:\Users\win\Desktop\建模国赛\4_2_Timetrue.xls',H);