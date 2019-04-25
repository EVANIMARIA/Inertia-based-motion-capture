#Define process of testing
import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import muldiv_inference
import muldiv_train

#10s to load again newest model
EVAL_INTERVAL_SECS=10

def evaluate(mull):
    with tf.Graph().as_default() as g:
        #define format of IO
        x=tf.placeholder(tf.float32,[None,muldiv_inference.INPUT_NODE],name='x-input')
        y_=tf.placeholder(tf.float32,[None,muldiv_inference.OUTPUT_NODE],name='y-input')
        validate_feed={x:mull.validation.images,y_:mull.validation.labels}

        #test doen't care regularizer
        y=muldiv_inference.inference(x,None)
        #argmax预测输入sample的类别
        correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
        accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
        #重命名加载模型，前向传播不需调用滑动平均来求均值，可以共用muldiv_inference中的前向传播过程
        variable_averages=tf.train.ExponentialMovingAverage(muldiv_train.MOVING_AVERAGE_DECAY)
        variables_to_restore=variable_averages.variables_to_restore()
        saver=tf.train.Saver(variables_to_restore)

        while True:
            with tf.Session() as sess:
                ckpt=tf.train.get_checkpoint_state(muldiv_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess,ckpt.model_checkpoint_path)
                    global_step=ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score=sess.run(accuracy,feed_dict=validate_feed)
                    print("After %s training steps, validation accuracy = %g"%(global_step,accuracy_score))
                else:
                    print('No checkpoint file found')
                    return
            time.sleep(EVAL_INTERVAL_SECS)

def main(argv=None):
    mull=input_data.read_data_sets("/tmp/data",one_hot=True)
    evaluate(mull)

if __name__=='__main__':
    tf.app.run()













