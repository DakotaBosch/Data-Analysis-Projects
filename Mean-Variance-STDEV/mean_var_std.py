import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
        return
    
    c = np.zeros((6,3))
    c[0,2] = np.mean(list)
    c[1,2] = np.var(list)
    c[2,2] = np.std(list)
    c[3,2] = np.max(list)
    c[4,2] = np.min(list)
    c[5,2] = np.sum(list)
    
    np.array(list)
    mt = np.reshape(list, (3,3))

    calculations = {
  "mean": [str(np.mean(mt,axis=0)), str(np.mean(mt,axis=1)), str(np.mean(list))],
  "variance": [str(np.var(mt,axis=0)), str(np.var(mt,axis=1)), str(np.var(list))],
  "standard deviation": [str(np.std(mt,axis=0)), str(np.std(mt,axis=1)), str(np.std(list))],
    "max": [str(np.max(mt,axis=0)),str(np.max(mt,axis=1)),str(np.max(list))],
    "min": [str(np.min(mt,axis=0)),str(np.min(mt,axis=1)),str(np.min(list))],
    "sum": [str(np.sum(mt,axis=0)),str(np.sum(mt,axis=1)),str(np.sum(list))]
        
    }
    return calculations


    return calculations
