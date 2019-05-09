import numpy as np
import os
from collections import deque
from sklearn import svm
from sklearn.externals import joblib

path1 = 'filter_code/dataxy'
path2 = 'filter_code/dataxy2/'

dataxy1 = []
dataxy2 = []

for dirpath, dirnames, filenames in os.walk(path1):
    for file in filenames:
        fullpath1 = os.path.join(dirpath, file)
        with open(fullpath1) as fp1:
            dataxy_n = fp1.read().split()
            dataxy_n_iter_list = deque(maxlen=590)
            for dataxy_n_iter in dataxy_n:
                dataxy_n_iter_list.append(float(dataxy_n_iter))
            # dataxy_n = list(filter(None,dataxy_n.split(' ')))
            # dataxy1 = np.append(dataxy1, dataxy_n_iter_list, axis=0)
            # dataxy1 = np.reshape(dataxy1, (20, -1))
            dataxy1.append(dataxy_n_iter_list)
dataxy1 = np.array(dataxy1)
print(dataxy1.shape)

for dirpath, dirnames, filenames in os.walk(path2):
    for file in filenames:
        fullpath2 = os.path.join(dirpath, file)
        with open(fullpath2) as fp2:
            dataxy_n = fp2.read().split()
            dataxy_n_iter_list = deque(maxlen=590)
            for dataxy_n_iter in dataxy_n:
                dataxy_n_iter_list.append(float(dataxy_n_iter))
            dataxy2.append(dataxy_n_iter_list)
dataxy2 = np.array(dataxy2)
print(dataxy2.shape)
'''
train1 = dataxy1[10:17, :]
train2 = dataxy2[10:17, :]
train3 = dataxy1[:7,:]
train4 = dataxy2[:7,:]
train_temp = np.append(train1, train3,axis=0)
train_temp2 = np.append(train2,train4,axis=0)
train = np.append(train_temp,train_temp2,axis=0)

np.savetxt("train.txt",train1)
np.savetxt("train2.txt",train2)

group = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
'''
test_temp = np.append(dataxy1[17:, :], dataxy1[7:10, :],axis=0)
test_temp2 = np.append(dataxy2[17:, :],dataxy2[7:10, :],axis=0)
test = np.append(test_temp,test_temp2,axis=0)
'''
np.savetxt("temp.txt",test)
'''
clf = joblib.load('clf.model')
result = clf.predict(test)
print(result)
