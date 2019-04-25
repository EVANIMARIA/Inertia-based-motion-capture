#Define process of training
import os
import tensorflow as tf
#from tensorflow.examples.tutorials.mnist import input_data
import muldiv_inference

BATCH_SIZE=100
LEARNING_RATE_BASE=0.8
LEARNING_RATE_DECAY=0.99
REGULARAZTION_RATE=0.0001
TRAINING_STEPS=30000
MOVING_AVERAGE_DECAY=0.99
MODEL_SAVE_PATH="/path/model"
MODEL_NAME="model.ckpt"

def train(mull):
    x=tf.placeholder(tf.float32,[muldiv_inference.INPUT_NODE,None],name='x-input')
    y_=tf.placeholder(tf.int32,[None,muldiv_inference.OUTPUT_NODE],name='y-input')
    
    regularizer=tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)
    y=muldiv_inference.inference(x,regularizer)
    global_step=tf.Variable(0,trainable=False)

    variable_averages=tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
    variables_averages_op=variable_averages.apply(tf.trainable_variables())
    #argmax得到正确答案序号，再计算交叉熵
    cross_entropy=tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.argmax(y_,1),logits=y)
    cross_entropy_mean=tf.reduce_mean(cross_entropy)
    loss=cross_entropy_mean+tf.add_n(tf.get_collection('losses'))
    #mnist.train.num_examples/BATCH_SIZE
    learning_rate=tf.train.exponential_decay(LEARNING_RATE_BASE,global_step,mull.train.num_examples/BATCH_SIZE,LEARNING_RATE_DECAY)
    train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step=global_step)
    with tf.control_dependencies([train_step,variables_averages_op]):
        train_op=tf.no_op(name='train')

    #初始化Tensorflow持久化类
    saver=tf.train.Saver()
    with tf.Session() as sess:
        tf.initialize_all_variables().run()

        for i in range(TRAINING_STEPS):
            #系统化数据文件读取！！！！！！
            xs,ys=mull.train.next_batch(BATCH_SIZE)
            _,loss_value,step=sess.run([train_op,loss,global_step],feed_dict={x:xs,y_:ys})
            if i % 1000 == 0:
                print("after %d training steps,loss on training batch is %g" %(step,loss_value))
                saver.save(sess,os.path.join(MODEL_SAVE_PATH,MODEL_NAME),global_step=global_step)

def main(argv=None):
    mull=input_data.read_data_sets("/tmp/data",one_hot=True)
    train(mull)
#主函数入口，import到其他函数不会运行
if __name__ =='__main__':
    tf.app.run()

print("Done~~")