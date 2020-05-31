%画出拣货员的行走结果
A=xlsread('C:\Users\win\Desktop\建模国赛\4_2_FH.xls');
B=xlsread('C:\Users\win\Desktop\建模国赛\4_2_People.xls');
for i=1:2 %1:9 任意一个
   x=B(:,2*i-1); y=B(:,2*i); 
   if i==1
   plot(x,y,'r-');
   hold on;
   else
       plot(x,y,'g-');
   hold on;
   end
   
end
title('拣货员行走结果');

% %%画出出库时间图
% B=xlsread('C:\Users\win\Desktop\建模国赛\4_2_Timetrue.xls');
% for i=1:2^9
%     
%    x=i; y=B(i,1);
%    if B(i,2)==1
%    plot(x,y,'r.');
%    hold on;
%    else
%          plot(x,y,'g.');
%           hold on;
%    end
%    if i==400||i==398||i==497||i==499
%        plot(x,y,'b.');
%           hold on;
%    end
%    
%    
% end
% title('人员安排出库时间结果');