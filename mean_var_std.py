import numpy as np

def calculate(lst):
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst[:9]).reshape((3,3))    
    means = [list(arr.mean(axis=0)), list(arr.mean(axis=1)), arr.mean()] 
    deviations = [list(arr.std(axis=0)), list(arr.std(axis=1)), arr.std()] 
    variances = [list(arr.var(axis=0)), list(arr.var(axis=1)), arr.var()] 
    maxs = [list(arr.max(axis=0)), list(arr.max(axis=1)), arr.max()] 
    mins = [list(arr.min(axis=0)), list(arr.min(axis=1)), arr.min()] 
    sums = [list(arr.sum(axis=0)), list(arr.sum(axis=1)), arr.sum()] 
    calculations = {"mean": means, "variance": variances, "standard deviation": deviations, "max": maxs, "min": mins, "sum": sums}



    return calculations