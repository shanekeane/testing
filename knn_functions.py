import numpy as np
import copy

#KNN FUNCTIONS
#Get (squared) Euclidean distance between all train and test samples
def get_distances(train_x, test_x):
    #normalize
    tr_x_norm = (train_x.T/np.sqrt(np.einsum("ij,ij->i", 
                                             train_x, train_x))).T
    te_x_norm = (test_x.T/np.sqrt(np.einsum("ij,ij->i", 
                                            test_x, test_x))).T
    
    trte = np.dot(tr_x_norm, te_x_norm.T)
    trte2 = (2.0 - 2.0*trte)
    
    return trte2

#This function returns a prediction given a 1d array with
#a list of labels of k nearest elements.
def get_single_pred(arr):
    nums, first_inds, counts = np.unique(arr, return_index = True, 
                                         return_counts = True)
    return (nums[np.argsort(first_inds)])[np.argmax(counts
                                                    [np.argsort(first_inds)])]

#Returns predictions for all test samples based on the matrix of 
#distances between test/train samples. 
def predict_knn(distance_mat, train_y, k):
    near_inds = np.argsort(distance_mat, axis = 0)[:k,:]
    near_labs = train_y[near_inds]
    return np.apply_along_axis(get_single_pred, 0, near_labs)

def knn(train_x, train_y, test_x, k):
    distance_mat = get_distances(train_x, test_x)
    preds = predict_knn(distance_mat, train_y, k)
    return preds

#Get cross-validation error
def cv_error_k(x_train, y_train, k):
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
        tr_y = np.concatenate(y_groups)
        preds = knn(tr_x, tr_y, val_x, k)
        total_error += np.sum(preds != val_y)*100.0/len(val_y)
        
    return total_error/5.0      
