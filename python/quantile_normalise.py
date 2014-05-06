"""

Naiive implementation of Quantile normalisation
http://en.wikipedia.org/wiki/Quantile_normalization

Author: Petr Klus

"""

import numpy as np
def quantile_normalize(test_arr):
    ranks_table = np.zeros(test_arr.shape)

    for row_index in range(test_arr.shape[0]):
        row = test_arr[row_index]
        values = np.array(sorted(np.unique(row)))
        ranks = [np.argwhere(values==el)[0][0] for el in row]
        ranks_table[row_index] = ranks
        # sorted_vals = np.sort(test_arr, axis=1)

    # now means of ranks
    column_means = np.mean(np.sort(test_arr, axis=1), axis=0)

    # quick&naiive
    normalised_table = np.zeros(test_arr.shape)

    for row in range(normalised_table.shape[0]):
        for col in range(normalised_table.shape[1]):
            normalised_table[row, col] = column_means[ranks_table[row, col]]

    return normalised_table


reference = """[ 5.66666667,  2.        ,  3.        ,  4.66666667]
[ 4.66666667,  2.        ,  4.66666667,  3.        ],
[ 2.        ,  3.        ,  4.66666667,  5.66666667],
"""
if __name__ == "__main__":

    print "Reference calculation:"
    print reference
    
    test_arr = np.array([[5,2, 3, 4], [4,1,4,2], [3,4,6,8]])

    normalised_table = quantile_normalize(test_arr)
    
    print normalised_table