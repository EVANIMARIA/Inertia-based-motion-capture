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
% fs=100;N=490;   %����Ƶ�ʺ����ݵ���
% n=0:N-1;t=n/fs;   %ʱ������
% %x=0.5*sin(2*pi*15*t)+2*sin(2*pi*40*t); %�ź�
% y=fft(data_ac_x3,N);    %���źŽ��п���Fourier�任
% mag=abs(y);     %���Fourier�任������
% f=n*fs/N;    %Ƶ������
% subplot(1,2,1),plot(f,mag);   %�����Ƶ�ʱ仯�����
% xlabel('Ƶ��/Hz');
% ylabel('���');title('N=128');grid on;
% subplot(1,2,2),plot(f(1:N/2),mag(1:N/2)); %���NyquistƵ��֮ǰ��Ƶ�ʱ仯�����
% xlabel('Ƶ��/Hz');
% ylabel('���');title('N=128');grid on;

figure
plot(data_ac_y3,'b');hold on;
figure
fs=100;N=490;   %����Ƶ�ʺ����ݵ���
n=0:N-1;t=n/fs;   %ʱ������
%x=0.5*sin(2*pi*15*t)+2*sin(2*pi*40*t); %�ź�
y=fft(data_ac_y3,N);    %���źŽ��п���Fourier�任
mag=abs(y);     %���Fourier�任������
f=n*fs/N;    %Ƶ������
subplot(1,2,1),plot(f,mag);   %�����Ƶ�ʱ仯�����
xlabel('Ƶ��/Hz');
ylabel('���');title('N=128');grid on;
subplot(1,2,2),plot(f(1:N/2),mag(1:N/2)); %���NyquistƵ��֮ǰ��Ƶ�ʱ仯�����
xlabel('Ƶ��/Hz');
ylabel('���');title('N=128');grid on;


