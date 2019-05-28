import numpy as np
import os
from collections import deque
from sklearn import svm
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from multiprocessing.dummy import Pool as ThreadPool

path1 = '0523/stop/ac/'
path2 = 'data/ac'



def reading(args):
    [path,name,max] = [x for x in args]
    temp_arr = []
    file_count = 50
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file[4:] == str(name):
                if file_count == 0:
                    break
                else:
                    file_count -= 1
                fullpath1 = os.path.join(dirpath, file)
                with open(fullpath1) as fp1:
                    dataxy_n = fp1.read().split()
                    dataxy_n_iter_list = deque(maxlen=max)
                    for dataxy_n_iter in dataxy_n:
                        dataxy_n_iter_list.append(float(dataxy_n_iter))
                    temp_arr.append(dataxy_n_iter_list)
    result = np.array(temp_arr)
    return result

data_stop_ac_x1 = reading((path1,'data_ac_x1.txt',380))
data_stop_ac_x2 = reading((path1,'data_ac_x2.txt',380))
data_stop_ac_x3 = reading((path1,'data_ac_x3.txt',380))
data_stop_ac_x4 = reading((path1,'data_ac_x4.txt',380))
data_stop_ac_x5 = reading((path1,'data_ac_x5.txt',380))
data_go_ac_x1 = reading((path1,'data_ac_x1.txt',380))
data_go_ac_x2 = reading((path1,'data_ac_x2.txt',380))
data_go_ac_x3 = reading((path1,'data_ac_x3.txt',380))
data_go_ac_x4 = reading((path1,'data_ac_x4.txt',380))
data_go_ac_x5 = reading((path1,'data_ac_x5.txt',380))

data_stop_read = [data_stop_ac_x1,data_stop_ac_x2,data_stop_ac_x3,data_stop_ac_x4,data_stop_ac_x5]
data_go_read = [data_go_ac_x1,data_go_ac_x2,data_go_ac_x3,data_go_ac_x4,data_go_ac_x5]

data_mean_temp = []
for v in data_stop_read:
    data_mean_temp.append(np.mean(v,axis=1))
data_stop_mean = np.array(data_mean_temp)

data_mean_temp = []
for v in data_go_read:
    data_mean_temp.append(np.mean(v,axis=1))
data_go_mean = np.array(data_mean_temp)

data_mean = np.append(data_stop_mean,data_go_mean,axis=1)
data_mean = data_mean.T
print(data_mean[:45,:].shape)
print(data_mean[50:95,:].shape)
train_mean = np.append(data_mean[:45,:],data_mean[50:95,:],axis=0)
test_mean = np.append(data_mean[45:50,:],data_mean[95:,:],axis=0)
print(train_mean.shape)

group1 = np.array([x - (x - 1) for x in range(46) if x >= 1])
group2 = np.array([x - (x - 2) for x in range(47) if x >= 2])
group = np.append(group1,group2)
group = group.T
print(group.shape)


svc = svm.SVC()
parameters = [
    {
        'C': [1,3,5,7,9,11,13,15,17,19],
        'gamma': [0.00001,0.0001,0.001,0.01,0.1,1,10,100,1000],
        'kernel': ['rbf']
    },
    {
        'C': [1,3,5,7,9,11,13,15,17,19],
        'kernel':['linear']
    }
]
clf = GridSearchCV(svc,parameters,cv=5,n_jobs=8)
clf.fit(train_mean,group)
print(clf.best_params_)
best_model = clf.best_estimator_
joblib.dump(best_model,"test1.m")
result = best_model.predict(test_mean)
print(result)
