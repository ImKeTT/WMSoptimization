%�������Ա�����߽��
A=xlsread('C:\Users\win\Desktop\��ģ����\4_2_FH.xls');
B=xlsread('C:\Users\win\Desktop\��ģ����\4_2_People.xls');
for i=1:2 %1:9 ����һ��
   x=B(:,2*i-1); y=B(:,2*i); 
   if i==1
   plot(x,y,'r-');
   hold on;
   else
       plot(x,y,'g-');
   hold on;
   end
   
end
title('���Ա���߽��');

% %%��������ʱ��ͼ
% B=xlsread('C:\Users\win\Desktop\��ģ����\4_2_Timetrue.xls');
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
% title('��Ա���ų���ʱ����');