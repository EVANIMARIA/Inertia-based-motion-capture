import csv
import tensorflow as tf
import os
file_name="data_ac_x1.csv"
with open(file_name,'w') as csvfile:
    spamwriter=csv.writer(csvfile,dialect='excel')
    with open('data_ac_x1.txt','r') as file_txt:
        for line in file_txt:
         line_datas=line.strip('\n').split(' ')
        spamwriter.writerow(line_datas)
# read csvfile
csvfile=open(file_name,'r')
reader=csv.reader(csvfile)
#print(reader)

#定义训练数据batch大小
batch_size=8;

#定义神经网络的参数
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x=tf.placeholder(tf.float32,shape=(None,2),name='x-input')
y_=tf.placeholder(tf.float32,shape=(None,3),name='y-input')

#前向传播
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

#定义损失函数和反向传播算法
cross_entropy=-tf.reduce_mean(y_*tf.log(tf.clip_by_value(y,1e-10,1.0)))
train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

#生成模拟训练集，并确定其大小
X=
Y=
dataset_size=128;

#运行Tensorflow的会话
with tf.Session() as sess:
	init_op=tf.initialize_all_variables() #全部初始化
	sess.run(init_op)
	print sess.run(w1)
	print sess.run(w2)
#得到训练前的参数值

#Time for training
steps=5000;
for i in range(steps):
	start=(i*batch_size)%dataset_size;
	end=min(start+batch_size,dataset_size);
	
#通过样本训练后更新神经网络参数
sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
if i%1000==0:
#每隔一段时间输出交叉熵
total_cross_entropy=sess.run(cross_entropy,feed_dict={x:X,y_:Y})
print("After %d training steps,cross entropy on all data is %g"%(i,total_cross_entropy))

#输出交叉熵应该随训练增加而减小，表示预测值趋于精准

print sess.run(w1)
print sess.run(w2)

