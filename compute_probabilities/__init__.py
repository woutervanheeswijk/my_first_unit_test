import numpy as np


def probabilities(my_data):
    """Compute probability corresponding to each positive numerical value in data"""
    # Initialize numpy probability array
    my_prob_array = np.zeros(len(my_data))
    if type(my_data) not in (list, tuple, np.ndarray):

        raise TypeError(
            "Input data is",
            type(my_data),
            "should be list, tuple or Numpy array",
        )

    # Normalize
    for i in range(len(my_data)):
        my_prob_array[i] = max(0, my_data[i]) / sum(my_data)

    print("Sum probabilities", sum(my_prob_array))

    return my_prob_array
