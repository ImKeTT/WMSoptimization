clear;
A=xlsread('C:\Users\win\Desktop\��ģ����\result1_true');
B=xlsread('C:\Users\win\Desktop\��ģ����\4_xlscheck.xls');
A2=xlsread('C:\Users\win\Desktop\��ģ����\2020��MathorCup��У��ѧ��ģ��ս����Ŀ\C\����\����1���ֿ�����.xlsx','����');
sssum=0;N=size(B,1);E=zeros(49*10,1);num=1;G=zeros(49*10,50);
for kk=1:49
    for ii=1:4
        for jj=ii:4
    ssum=0;
for i=1:N
if B(i,1)==kk;
    ssum=ssum+1;
end
end
if ii<jj
F=B([sssum+1:sssum+ssum N-4+ii N-4+jj],2);
else
 F=B([sssum+1:sssum+ssum N-4+ii],2);
end


n=size(F,1);
D=zeros(n,n);
for i=1:n
    for j=i:n
        if i~=j
          a=(floor((F(i,1)/100))-1)*15+mod(F(i,1),100);b=(floor((F(j,1)/100))-1)*15+mod(F(j,1),100);
             D(i,j)=A(a,b);
        else
            D(i,j)=eps;      %i=jʱ�����㣬Ӧ��Ϊ0�����������������Ҫȡ��������eps��������Ծ��ȣ���ʾ
        end
        D(j,i)=D(i,j);   %�Գƾ���
    end
   
end
 CL=A2(:,1:2);
C=zeros(n,2);
 for i=1:n
          a=(floor((F(i,1)/100))-1)*15+mod(F(i,1),100);
             C(i,1:2)=CL(a,1:2);
 end 
 
 
 %C=xlsread('C:\Users\win\Desktop\��ģ����\3_P1.xlsx');
NC_max=100;
m=100;
Alpha=1;
Beta=5;
Rho=0.5;
Q=1;
%%��һ����������ʼ��
n=size(C,1);%n��ʾ����Ĺ�ģ�����и�����
%D=xlsread('C:\Users\win\Desktop\��ģ����\3_2.xls');%D��ʾ��ȫͼ�ĸ�Ȩ�ڽӾ���
Eta=1./D;          %EtaΪ�������ӣ�������Ϊ����ĵ���
Tau=ones(n,n);     %TauΪ��Ϣ�ؾ���
Tabu=zeros(m,n);   %�洢����¼·��������
NC=1;               %��������������¼��������
R_best=zeros(NC_max,n);       %�������·��
L_best=inf.*ones(NC_max,1);   %�������·�ߵĳ���
L_ave=zeros(NC_max,1);        %����·�ߵ�ƽ������
 
while NC<=NC_max        %ֹͣ����֮һ���ﵽ������������ֹͣ
    %%�ڶ�������mֻ���Ϸŵ�n��������
        Randpos=[];   %�����ȡ
    for i=1:(ceil(m/n))
        Randpos=[Randpos,randperm(n)];
    end
    Tabu(:,1)=(Randpos(1,1:m))';    %�˾䲻̫��⣿
 
    %%��������mֻ���ϰ����ʺ���ѡ����һ�����У���ɸ��Ե�����
    for j=2:n     %���ڳ��в�����
        for i=1:m    
            visited=Tabu(i,1:(j-1)); %��¼�ѷ��ʵĳ��У������ظ�����
            J=zeros(1,(n-j+1));       %�����ʵĳ���
            P=J;                      %�����ʳ��е�ѡ����ʷֲ�
            Jc=1;
            for k=1:n
                if length(find(visited==k))==0   %��ʼʱ��0
                J(Jc)=k;
                Jc=Jc+1;                         %���ʵĳ��и����Լ�1
                end
            end
            %��������ѡ���еĸ��ʷֲ�
            for k=1:length(J)
                P(k)=(Tau(visited(end),J(k))^Alpha)*(Eta(visited(end),J(k))^Beta);
            end
            P=P/(sum(P));
            %������ԭ��ѡȡ��һ������
            Pcum=cumsum(P);     %cumsum��Ԫ���ۼӼ����
            Select=find(Pcum>=rand); %������ĸ��ʴ���ԭ���ľ�ѡ������·��
            to_visit=J(Select(1));
            Tabu(i,j)=to_visit;
        end
    end
    if NC>=2
        Tabu(1,:)=R_best(NC-1,:);
    end
    %%���Ĳ�����¼���ε������·��
    L=zeros(m,1);     %��ʼ����Ϊ0��m*1��������
    for i=1:m
        R=Tabu(i,:);
        for j=1:(n-1)
            L(i)=L(i)+D(R(j),R(j+1));    %ԭ������ϵ�j�����е���j+1�����еľ���
        end
        L(i)=L(i)+D(R(1),R(n));      %һ���������߹��ľ���
    end
    L_best(NC)=min(L);           %��Ѿ���ȡ��С
    pos=find(L==L_best(NC));
    R_best(NC,:)=Tabu(pos(1),:); %���ֵ���������·��
    L_ave(NC)=mean(L);           %���ֵ������ƽ������
    NC=NC+1;                      %��������
    %%���岽��������Ϣ��
    Delta_Tau=zeros(n,n);        %��ʼʱ��Ϣ��Ϊn*n��0����
    for i=1:m
        for j=1:(n-1)
            Delta_Tau(Tabu(i,j),Tabu(i,j+1))=Delta_Tau(Tabu(i,j),Tabu(i,j+1))+Q/L(i);          
        %�˴�ѭ����·����i��j���ϵ���Ϣ������
        end
            Delta_Tau(Tabu(i,n),Tabu(i,1))=Delta_Tau(Tabu(i,n),Tabu(i,1))+Q/L(i);
        %�˴�ѭ��������·���ϵ���Ϣ������
    end
    Tau=(1-Rho).*Tau+Delta_Tau; %������Ϣ�ػӷ������º����Ϣ��
    %%�����������ɱ�����
    Tabu=zeros(m,n);             %%ֱ������������
end
%%���߲���������
Pos=find(L_best==min(L_best)); %�ҵ����·������0Ϊ�棩
Shortest_Route=R_best(Pos(1),:); %���������������·��
Shortest_Length=L_best(Pos(1)); %��������������̾���
%subplot(1,2,1);                  %���Ƶ�һ����ͼ��
    %%=========================================================================
    %% DrawRoute.m
    %% ��·��ͼ���Ӻ���
    %%-------------------------------------------------------------------------
    %% C Coordinate �ڵ����꣬��һ��N��2�ľ���洢
%     %% R Route ·��
%     %%=========================================================================
% 
%     N=length(R);
%     scatter(C(:,1),C(:,2));
%     hold on
%     plot([C(R(1),1),C(R(N),1)],[C(R(1),2),C(R(N),2)],'g')
%     hold on
%     for ii=2:N
%         plot([C(R(ii-1),1),C(R(ii),1)],[C(R(ii-1),2),C(R(ii),2)],'g')
%         hold on
%     end
%     title('�����������Ż���� ')
%  
% subplot(1,2,2);                  %���Ƶڶ�����ͼ��
%  
% plot(0,8000,'r');
% plot(L_best);
% hold on ;                        %����ͼ��
% plot(L_ave,'r');
% title('ƽ���������̾���') ;    %����
E(num,1)=Shortest_Length;
G(num,1:size(Shortest_Route,2))=Shortest_Route(1,:);
num=num+1;
        end
    end
    sssum=sssum+ssum;
end
xlswrite('C:\Users\win\Desktop\��ģ����\4_shortlc.xls',E);
xlswrite('C:\Users\win\Desktop\��ģ����\4_shortluji.xls',G);