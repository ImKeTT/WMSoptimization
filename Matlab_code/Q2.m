clear;
A=xlsread('C:\Users\win\Desktop\建模国赛\result1_true');
B=xlsread('C:\Users\win\Desktop\建模国赛\问题2初值');
n=size(B,1);%B矩阵的大小；
D=zeros(n,n);
for i=1:n
    for j=i:n
        if i~=j
          a=(floor((B(i,1)/100))-1)*15+mod(B(i,1),100);b=(floor((B(j,1)/100))-1)*15+mod(B(j,1),100);
             D(i,j)=A(a,b);
        else
            D(i,j)=eps;      %i=j时不计算，应该为0，但后面的启发因子要取倒数，用eps（浮点相对精度）表示
        end
        D(j,i)=D(i,j);   %对称矩阵
    end
   
end

 xlswrite('C:\Users\win\Desktop\建模国赛\3_T06_D.xls',D);
    