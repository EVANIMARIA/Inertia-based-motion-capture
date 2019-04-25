#Define process of forward propagation and parameters
import numpy as np
import tensorflow as tf

INPUT_NODE=590
OUTPUT_NODE=9
LAYER1_NODE=500

data_ac_x1=np.loadtxt('data_ac_x1.txt',dtype=np.float32)
data_ac_x1=np.reshape(data_ac_x1,[590,1])
#print(data_ac_x1.shape)=(590,)
data_ac_x2=np.loadtxt('data_ac_x2.txt',dtype=np.float32)
data_ac_x2=np.reshape(data_ac_x2,[590,1])
data_ac=np.hstack((data_ac_x1,data_ac_x2))
#print(data_ac.shape)=(590,2)

def get_weight_variable(shape,regularizer):
    weights=tf.get_variable("weights",shape,initializer=tf.truncated_normal_initializer(stddev=0.1))

    if regularizer!=None:
        tf.add_to_collection('losses',regularizer(weights))
    return weights

#forward propagation
def inference(input_tensor,regularizer):
    with tf.variable_scope('layer1'):
        weights=get_weight_variable([INPUT_NODE,LAYER1_NODE],regularizer)
        biases=tf.get_variable("biases",[LAYER1_NODE],initializer=tf.constant_initializer(0.0))
        layer1=tf.nn.relu(tf.matmul(input_tensor,weights)+biases)

    with tf.variable_scope('layer2'):
        weights=get_weight_variable([LAYER1_NODE,OUTPUT_NODE],regularizer)
        biases=tf.get_variable("biases",[OUTPUT_NODE],initializer=tf.constant_initializer(0.0))
        layer2=tf.matmul(layer1,weights)+biases

    return layer2
print("Done~")