import numpy as np
# import sparse module from SciPy package
from scipy import sparse
# import uniform module to create random numbers
# from scipy.stats import uniform
# import NumPy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # row indices
    row_ind = np.array([0, 1, 1, 3, 4])
    # column indices
    col_ind = np.array([0, 2, 4, 3, 4])
    # data to be stored in COO sparse
    m_entries = np.array([1, 2, 3, 4, 5], dtype=float)
    # create COO sparse matrix from three arrays
    mat_coo = sparse.coo_matrix((m_entries, (row_ind, col_ind)))
    print(mat_coo.toarray())
    print()
    mat_coo._add_sparse([1], ([4], [15]))
    #print(mat_coo.row[2])
    print(mat_coo.toarray())
    asd = 3*mat_coo.getrow(4)
    #mat_coo.data.put([1,*], )[1] = mat_coo.getrow(1) + asd

'''
    print(asd.toarray())
    print()
    # print coo_matrix
    print(mat_coo.toarray())
    print()
    print(mat_coo)
'''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
