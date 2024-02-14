# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

def PrintMatrix(matrix, text="Matrix: "):
    nrows, ncols = matrix.shape
    print("\n" + text)
    for i in range(nrows):
        print("[", end="")
        for j in range(ncols):
            if matrix[i,j] >= 0:
                if j == ncols-1:
                    print(" {:.3f}".format(matrix[i,j]), end="")
                    continue
                print(" {:.3f}".format(matrix[i,j]), end=" ")
                continue
            if j == ncols-1:
                print("{:.3f}".format(matrix[i,j]), end="")
                continue
            print("{:.3f}".format(matrix[i,j]), end=" ")
            
        print("]")