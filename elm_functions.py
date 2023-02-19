#Extreme Learning Machine Functions
import numpy as np
import copy

#Relu function
def relu(x):
    return np.maximum(0, x)

def get_H(X, w, b):
    return relu(np.dot(X, w) + b)

def get_beta(H, T):
    return np.dot(np.linalg.pinv(H), T)

def get_prediction(beta, val_x, w, b):
    H_test = get_H(val_x, w, b)
    return np.dot(H_test, beta)

def get_error_elm(tr_x, tr_y, val_x, val_y, nodes):
    w = np.random.normal(size = (256, nodes))
    b = np.random.normal(size = nodes)
    H = get_H(tr_x, w, b)
    beta = get_beta(H, tr_y)
    preds = get_prediction(beta, val_x, w, b)
    err = np.sum(np.argmax(preds, axis = 1) !=
                 np.argmax(val_y, axis = 1))*100.0/val_y.shape[0]
    return err

#Cross-validation error based on number of nodes in hidden layer.
def cv_error_nodes(x_train, y_train, nodes):
    total_error = 0.0
    
    #Train on five different test sets and get error on five
    #different validation sets
    for i in range(5):
        #Get train/valid x/y for each run
        x_groups = np.array_split(x_train, 5)
        val_x = x_groups.pop(i) #Remove validation set
        tr_x = np.vstack(x_groups) #Recombine
        y_groups = np.array_split(y_train, 5)
        val_y = y_groups.pop(i)
        tr_y = np.vstack(y_groups)
        
        #Get ELM error
        total_error += get_error_elm(tr_x, tr_y, val_x, val_y, nodes)
        
    total_error /= 5.0
    
    return total_error
