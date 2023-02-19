#Useful functions
import numpy as np

#For splitting data
def get_knn_data_split(dat):
    indices = np.arange(dat.shape[0])
    np.random.shuffle(indices)
    rand_dat = dat[indices]
    train_dat = rand_dat[:7438]
    test_dat = rand_dat[7438:]
    train_y, train_x = np.hsplit(train_dat, [1])
    train_y = train_y.reshape(7438,)
    test_y, test_x = np.hsplit(test_dat, [1])
    test_y = test_y.reshape(1860,)
    return train_x, train_y, test_x, test_y
    
#Returns an array of one hot vectors given 
#1d array of numbers. One hot required for ELM.
def one_hot(y_vec):
    out_vec = np.zeros((len(y_vec), 10))
    for i in range(len(y_vec)):
        out_vec[i][y_vec[i].astype(int)] = 1
        
    return out_vec

def get_elm_data_split(dat_x, dat_y):
    #Shuffle indices
    indices = np.arange(len(dat_y))
    np.random.shuffle(indices)
    rand_x = dat_x[indices]
    rand_y = dat_y[indices]
    train_x = rand_x[:7438]
    test_x = rand_x[7438:]
    train_y = rand_y[:7438]
    test_y = rand_y[7438:]

    return train_x, train_y, test_x, test_y
