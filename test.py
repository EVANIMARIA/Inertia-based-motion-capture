import numpy as np
import os
from collections import deque
from sklearn import svm
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA

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


train1 = dataxy1[10:17, :]
train2 = dataxy2[10:17, :]
train3 = dataxy1[:7, :]
train4 = dataxy2[:7, :]

train1_mean = np.mean(train1, axis=1)
train2_mean = np.mean(train2, axis=1)
train3_mean = np.mean(train3, axis=1)
train4_mean = np.mean(train4, axis=1)
train1_mean = train1_mean.reshape(-1, 1)
train2_mean = train2_mean.reshape(-1, 1)
train3_mean = train3_mean.reshape(-1, 1)
train4_mean = train4_mean.reshape(-1, 1)
train_mean_sum_temp1 = np.append(train1_mean, train3_mean, axis=1)
train_mean_sum_temp2 = np.append(train2_mean, train4_mean, axis=1)
train_mean_sum = np.append(train_mean_sum_temp1, train_mean_sum_temp2, axis=0)
print(train_mean_sum.shape)

train1_var = np.var(train1, axis=1)
train2_var = np.var(train1, axis=1)
train3_var = np.var(train1, axis=1)
train4_var = np.var(train1, axis=1)
train1_var = train1_var.reshape(-1, 1)
train2_var = train2_var.reshape(-1, 1)
train3_var = train3_var.reshape(-1, 1)
train4_var = train4_var.reshape(-1, 1)
train_var_sum_temp1 = np.append(train1_var, train3_var, axis=1)
train_var_sum_temp2 = np.append(train2_var, train4_var, axis=1)
train_var_sum = np.append(train_var_sum_temp1, train_var_sum_temp2, axis=0)

train_sum = np.append(train_mean_sum, train_var_sum, axis=1)
print(train_sum.shape)

'''
train_temp = np.append(train1, train3,axis=1)
train_temp2 = np.append(train2,train4,axis=1)
train = np.append(train_temp,train_temp2,axis=0)
print(train.shape)
'''
'''
pca = PCA(n_components=2)
pca.fit(train)
train_new = pca.transform(train)
print(pca.n_components)
'''


'''
np.savetxt("train.txt",train1)
np.savetxt("train2.txt",train2)
'''
group = np.array([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]).T
print(group.shape)

'''
test_temp = np.append(dataxy1[17:, :], dataxy1[7:10, :],axis=1)
test_temp2 = np.append(dataxy2[17:, :],dataxy2[7:10, :],axis=1)
test = np.append(test_temp,test_temp2,axis=0)
print(test.shape)
'''

'''
np.savetxt("temp.txt",test)
'''
test1_mean = np.mean(dataxy1[17:, :], axis=1)
test2_mean = np.mean(dataxy1[7:10, :], axis=1)
test3_mean = np.mean(dataxy2[17:, :], axis=1)
test4_mean = np.mean(dataxy2[7:10, :], axis=1)
test1_mean = test1_mean.reshape(-1, 1)
test2_mean = test2_mean.reshape(-1, 1)
test3_mean = test3_mean.reshape(-1, 1)
test4_mean = test4_mean.reshape(-1, 1)
test_mean_sum_temp1 = np.append(test1_mean, test2_mean, axis=1)
test_mean_sum_temp2 = np.append(test3_mean, test4_mean, axis=1)
test_mean_sum = np.append(test_mean_sum_temp1, test_mean_sum_temp2, axis=0)
print(test_mean_sum)

test1_var = np.var(dataxy1[17:, :], axis=1)
test2_var = np.var(dataxy1[7:10, :], axis=1)
test3_var = np.var(dataxy2[17:, :], axis=1)
test4_var = np.var(dataxy2[7:10, :], axis=1)
test1_var = test1_var.reshape(-1, 1)
test2_var = test2_var.reshape(-1, 1)
test3_var = test3_var.reshape(-1, 1)
test4_var = test4_var.reshape(-1, 1)
test_var_sum_temp1 = np.append(test1_var, test2_var, axis=1)
test_var_sum_temp2 = np.append(test3_var, test4_var, axis=1)
test_var_sum = np.append(test_var_sum_temp1, test_var_sum_temp2, axis=0)


test_sum = np.append(test_mean_sum, test_var_sum, axis=1)
print(test_sum.shape)

'''
clf = svm.SVC(C=0.8, kernel='rbf', gamma=90, decision_function_shape='ovr')
clf_result = clf.fit(train_mean_sum, group)
joblib.dump(clf_result,'clf.model')
result = clf.predict(test_mean_sum)
print(result)
'''

svc = svm.SVC()
parameters = [
    {
        'C': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
        'gamma': [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000],
        'kernel': ['rbf']
    },
    {
        'C': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
        'kernel':['linear']
    }
]
clf = GridSearchCV(svc, parameters, cv=5, n_jobs=8)
clf.fit(train_sum, group)
print(clf.best_params_)
best_model = clf.best_estimator_
result = best_model.predict(test_sum)
print(result)
