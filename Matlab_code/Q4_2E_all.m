clear;
E=xlsread('C:\Users\win\Desktop\建模国赛\4_2C.xlsx');
D=zeros(9*2^9,3);num=0;n=size(E,1);
for i1=1:2
     if i1==2
        temp=E(1,3);
    E(1,3)=E(1,2);
    E(1,2)=temp;
                            end
    for i2=1:2
         if i2==2
        temp=E(2,3);
    E(2,3)=E(2,2);
    E(2,2)=temp;
                            end
        for i3=1:2
             if i3==2
        temp=E(3,3);
    E(3,3)=E(3,2);
    E(3,2)=temp;
                            end
            for i4=1:2
                 if i4==2
        temp=E(4,3);
    E(4,3)=E(4,2);
    E(4,2)=temp;
                            end
                for i5=1:2
                     if i5==2
        temp=E(5,3);
    E(5,3)=E(5,2);
    E(5,2)=temp;
                            end
                    for i6=1:2
                         if i6==2
        temp=E(6,3);
    E(6,3)=E(6,2);
    E(6,2)=temp;
                            end
                        for i7=1:2
                             if i7==2
        temp=E(7,3);
    E(7,3)=E(7,2);
    E(7,2)=temp;
                            end
                            for i8=1:2
                                 if i8==2
        temp=E(8,3);
    E(8,3)=E(8,2);
    E(8,2)=temp;
                            end
                                for i9=1:2        
                            if i9==2
        temp=E(9,3);
    E(9,3)=E(9,2);
    E(9,2)=temp;
                            end
                          
                            D(1+n*num:n+n*num,:)=E;
                              num=num+1;
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end
xlswrite('C:\Users\win\Desktop\建模国赛\4_2_E_all.xls',D);
                                    
                            
    