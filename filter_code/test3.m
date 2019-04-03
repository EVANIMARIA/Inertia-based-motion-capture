clear
data_ac_y3=load('data_ac_y3.txt');
data_ac_x3=load('data_ac_x3.txt');
data_ac_z3=load('data_ac_z3.txt');

%plot(data_ac_y3,'r');hold on;
%plot(data_ac_x3,'b');hold on;
%plot(data_ac_z3,'g');hold on;

%data_ac_x3=smooth(data_ac_x3,11);
data_ac_y3=smooth(data_ac_y3,11);
% plot(data_ac_x3,'b');hold on;
% figure
% fs=100;N=490;   %²ÉÑùÆµÂÊºÍÊý¾ÝµãÊý
% n=0:N-1;t=n/fs;   %Ê±¼äÐòÁÐ
% %x=0.5*sin(2*pi*15*t)+2*sin(2*pi*40*t); %ÐÅºÅ
% y=fft(data_ac_x3,N);    %¶ÔÐÅºÅ½øÐÐ¿ìËÙFourier±ä»»
% mag=abs(y);     %ÇóµÃFourier±ä»»ºóµÄÕñ·ù
% f=n*fs/N;    %ÆµÂÊÐòÁÐ
% subplot(1,2,1),plot(f,mag);   %»æ³öËæÆµÂÊ±ä»¯µÄÕñ·ù
% xlabel('ÆµÂÊ/Hz');
% ylabel('Õñ·ù');title('N=128');grid on;
% subplot(1,2,2),plot(f(1:N/2),mag(1:N/2)); %»æ³öNyquistÆµÂÊÖ®Ç°ËæÆµÂÊ±ä»¯µÄÕñ·ù
% xlabel('ÆµÂÊ/Hz');
% ylabel('Õñ·ù');title('N=128');grid on;

figure
plot(data_ac_y3,'b');hold on;
figure
fs=100;N=490;   %²ÉÑùÆµÂÊºÍÊý¾ÝµãÊý
n=0:N-1;t=n/fs;   %Ê±¼äÐòÁÐ
%x=0.5*sin(2*pi*15*t)+2*sin(2*pi*40*t); %ÐÅºÅ
y=fft(data_ac_y3,N);    %¶ÔÐÅºÅ½øÐÐ¿ìËÙFourier±ä»»
mag=abs(y);     %ÇóµÃFourier±ä»»ºóµÄÕñ·ù
f=n*fs/N;    %ÆµÂÊÐòÁÐ
subplot(1,2,1),plot(f,mag);   %»æ³öËæÆµÂÊ±ä»¯µÄÕñ·ù
xlabel('ÆµÂÊ/Hz');
ylabel('Õñ·ù');title('N=128');grid on;
subplot(1,2,2),plot(f(1:N/2),mag(1:N/2)); %»æ³öNyquistÆµÂÊÖ®Ç°ËæÆµÂÊ±ä»¯µÄÕñ·ù
xlabel('ÆµÂÊ/Hz');
ylabel('Õñ·ù');title('N=128');grid on;


