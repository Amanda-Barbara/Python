import numpy as np

if __name__ == "__main__":
    A = np.asarray([[1,0,1,0,0,0,0,0,0],
         [0,0,0,1,0,1,0,0,0],
         [0,0,0,0,0,0,1,0,1],
         [0,2,1,0,0,0,0,0,0],
         [0,0,0,0,2,1,0,0,0],
         [0,0,0,0,0,0,0,2,1],
         [-1,2,1,0,0,0,0,0,0],
         [0,0,0,-1,2,1,0,0,0],
         [0,0,0,0,0,0,-1,2,1]], np.float32)
    # print(A)
    # print(np.linalg.det(A))
    # print(np.linalg.inv(A))
    b = np.asarray([[1], [0], [1], [1], [2], [1], [0], [2], [1]], np.float32)
    # print(b)
    print(np.linalg.solve(A, b))
