import numpy as np

def get_data(data):
    data = {
        'mean': [
            [data[:, i].mean() for i in range(data.shape[0])], 
            [data[i].mean() for i in range(data.shape[1])],
            data.flatten().mean()
        ],
        'variance': [
            [data[:, i].var() for i in range(data.shape[0])], 
            [data[i].var() for i in range(data.shape[1])],
            data.flatten().var()
        ],
        'standard deviation': [
            [data[:, i].std() for i in range(data.shape[0])], 
            [data[i].std() for i in range(data.shape[1])],
            data.flatten().std()
        ],
        'max': [
            [data[:, i].max() for i in range(data.shape[0])], 
            [data[i].max() for i in range(data.shape[1])],
            data.flatten().max()
        ],
        'min': [
            [data[:, i].min() for i in range(data.shape[0])], 
            [data[i].min() for i in range(data.shape[1])],
            data.flatten().min()
        ],
        'sum': [
            [data[:, i].sum() for i in range(data.shape[0])], 
            [data[i].sum() for i in range(data.shape[1])],
            data.flatten().sum()
        ],       
    }

    return data        

def calculate(array):
    if len(array) != 9:
        raise ValueError('List must contain nine numbers.')   

    array = np.array(array).reshape((3, 3))
    data_processed = get_data(array)

    return data_processed