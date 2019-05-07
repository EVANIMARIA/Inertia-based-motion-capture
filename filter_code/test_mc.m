clear
file=dir('D:\matlab\bin\SVM\dataxy\*.txt');
for n=1:length(file)
    D1{n,1}=importdata(['D:\matlab\bin\SVM\dataxy\',file(n).name]);
end

A1=cellfun(@mean,D1);
S1=cellfun(@std,D1);

file=dir('D:\matlab\bin\SVM\dataxy2\*.txt');
for n=1:length(file)
    D2{n,1}=importdata(['D:\matlab\bin\SVM\dataxy2\',file(n).name]);
end

A2=cellfun(@mean,D2);
S2=cellfun(@std,D2);

train1=[A1(1:7) S1(1:7) A1(11:17) S1(11:17)];
train2=[A2(1:7) S2(1:7) A2(11:17) S2(11:17)];
train=[train1;train2];

test1=[A1(8:10) S1(8:10) A1(18:20) S1(18:20)];
test2=[A2(8:10) S2(8:10) A2(18:20) S2(18:20)];
test=[test1;test2];
group=[1,1,1,1,1,1,1,2,2,2,2,2,2,2];

svmModel = svmtrain(train,group,'kernel_function','rbf','showplot',true);
classfication=svmclassify(svmModel,test,'Showplot',true);
groupTest=[1,1,1,2,2,2]; 

count=0;
for i=(1:3)
   if isequal(classfication(i),groupTest(i))
      count=count+1;
   end
end
fprintf('���ྫ��Ϊ��%f\n' ,count/3);




