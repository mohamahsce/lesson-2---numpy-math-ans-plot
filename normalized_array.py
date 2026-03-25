import numpy as np

def normalized_array(input_array):
    # 1. Find the minimum and maximum values
    min_val = np.min(input_array)
    max_val = np.max(input_array)
    
    # 2. Calculate the range (denominator)
    diff = max_val - min_val
    
    # 3. Handle the edge case: if all values are equal, diff will be 0.
    # We return an array of zeros with the same shape to avoid division by zero.
    if diff == 0:
        return np.zeros_like(input_array, dtype=float)
    
    # 4. Apply the formula: (x - min) / (max - min)
    # This happens to every element in the array at once!
    new_array = (input_array - min_val) / diff
    
    return new_array
