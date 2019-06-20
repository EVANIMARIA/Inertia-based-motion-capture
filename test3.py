import numpy as np
import os
from collections import deque
from sklearn import svm
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from multiprocessing.dummy import Pool as ThreadPool

path1 = '0523/stop/ac/'
path3 = '0523/wait/ac/'
path2 = '0523/straight go/ac/'

# reading the file,and turn the data into the form that
# each row contains a complete sample of one sensor


def reading(args):
    [path, name, max] = [x for x in args]
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


if __name__ == '__main__':
    # reading file of ac sensor of two kinds of action
    data_stop_ac_x1 = reading((path1, 'data_ac_x1.txt', 380))
    data_stop_ac_x2 = reading((path1, 'data_ac_x2.txt', 380))
    data_stop_ac_x3 = reading((path1, 'data_ac_x3.txt', 380))
    data_stop_ac_x4 = reading((path1, 'data_ac_x4.txt', 380))
    data_stop_ac_x5 = reading((path1, 'data_ac_x5.txt', 380))
    data_go_ac_x1 = reading((path2, 'data_ac_x1.txt', 380))
    data_go_ac_x2 = reading((path2, 'data_ac_x2.txt', 380))
    data_go_ac_x3 = reading((path2, 'data_ac_x3.txt', 380))
    data_go_ac_x4 = reading((path2, 'data_ac_x4.txt', 380))
    data_go_ac_x5 = reading((path2, 'data_ac_x5.txt', 380))
    data_wait_ac_x1 = reading((path3, 'data_ac_x1.txt', 380))
    data_wait_ac_x2 = reading((path3, 'data_ac_x2.txt', 380))
    data_wait_ac_x3 = reading((path3, 'data_ac_x3.txt', 380))
    data_wait_ac_x4 = reading((path3, 'data_ac_x4.txt', 380))
    data_wait_ac_x5 = reading((path3, 'data_ac_x5.txt', 380))
    # print(data_go_ac_x1)

    data_stop_read = [data_stop_ac_x1, data_stop_ac_x2,
                      data_stop_ac_x3, data_stop_ac_x4, data_stop_ac_x5]
    data_go_read = [data_go_ac_x1, data_go_ac_x2,
                    data_go_ac_x3, data_go_ac_x4, data_go_ac_x5]
    data_wait_read = [data_wait_ac_x1, data_wait_ac_x2,
                      data_wait_ac_x3, data_wait_ac_x4, data_wait_ac_x5]

    # turning data into a form that each row contain the avr of each process
    data_mean_temp = []
    for v in data_stop_read:
        data_mean_temp.append(np.mean(v, axis=1))
    data_stop_mean = np.array(data_mean_temp)

    data_mean_temp = []
    for k in data_go_read:
        print(k.shape)
        data_mean_temp.append(np.mean(k, axis=1))
    data_go_mean = np.array(data_mean_temp)

    data_mean_temp = []
    for n in data_wait_read:
        print(n.shape)
        data_mean_temp.append(np.mean(n, axis=1))
    data_wait_mean = np.array(data_mean_temp)

    # turning the data into a form that
    # stop_ac_1 stop_ac_2 stop_ac_3 stop_ac_4 stop_ac_5
    # ...
    # go_ac_1 go_ac_2 go_ac_3 go_ac_4 go_ac_5
    # ...
    data_mean = np.append(data_stop_mean, data_go_mean, axis=1)
    data_mean = np.append(data_mean, data_wait_mean, axis=1)
    print(data_mean.shape)
    data_mean = data_mean.T
    print(data_mean[:45, :].shape)
    print(data_mean[50:95, :].shape)
    print(data_mean[100:145, :].shape)
    train_mean = np.append(data_mean[:45, :], data_mean[50:95, :], axis=0)
    train_mean = np.append(train_mean, data_mean[100:145, :], axis=0)
    test_mean = np.append(data_mean[45:50, :], data_mean[95:100, :], axis=0)
    test_mean = np.append(test_mean, data_mean[145:, :], axis=0)
    print(train_mean.shape)
    print(test_mean.shape)

    # generating the tags group
    group1 = np.array([x - (x - 1) for x in range(46) if x >= 1])
    group2 = np.array([x - (x - 2) for x in range(47) if x >= 2])
    group3 = np.array([x - (x - 3) for x in range(48) if x >= 3])
    group = np.append(group1, group2)
    group = np.append(group, group3)
    group = group.T
    print(group.shape)

    # initializing the svc model and grid searching the best parameter
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
    clf.fit(train_mean, group)
    print(clf.best_params_)
    best_model = clf.best_estimator_

    # saving the model and do predicting using the test group
    joblib.dump(best_model, "test1.m")
    result = best_model.predict(test_mean)
    print(result)
