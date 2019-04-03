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
% fs=100;N=490;   %采样频率和数据点数
% n=0:N-1;t=n/fs;   %时间序列
% %x=0.5*sin(2*pi*15*t)+2*sin(2*pi*40*t); %信号
% y=fft(data_ac_x3,N);    %对信号进行快速Fourier变换
% mag=abs(y);     %求得Fourier变换后的振幅
% f=n*fs/N;    %频率序列
% subplot(1,2,1),plot(f,mag);   %绘出随频率变化的振幅
% xlabel('频率/Hz');
% ylabel('振幅');title('N=128');grid on;
% subplot(1,2,2),plot(f(1:N/2),mag(1:N/2)); %绘出Nyquist频率之前随频率变化的振幅
% xlabel('频率/Hz');
% ylabel('振幅');title('N=128');grid on;

figure
plot(data_ac_y3,'b');hold on;
figure
fs=100;N=490;   %采样频率和数据点数
n=0:N-1;t=n/fs;   %时间序列
%x=0.5*sin(2*pi*15*t)+2*sin(2*pi*40*t); %信号
y=fft(data_ac_y3,N);    %对信号进行快速Fourier变换
mag=abs(y);     %求得Fourier变换后的振幅
f=n*fs/N;    %频率序列
subplot(1,2,1),plot(f,mag);   %绘出随频率变化的振幅
xlabel('频率/Hz');
ylabel('振幅');title('N=128');grid on;
subplot(1,2,2),plot(f(1:N/2),mag(1:N/2)); %绘出Nyquist频率之前随频率变化的振幅
xlabel('频率/Hz');
ylabel('振幅');title('N=128');grid on;


