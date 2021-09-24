import numpy as np
a = np.array([[0, 1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10, 11],
              [12, 13, 14, 15, 16, 17],
              [18, 19, 20, 21, 22, 23],
              [24, 25, 26, 27, 28, 29],
              [30, 31, 32, 33, 34, 35]])

print("\n a[2::2, ::2]=\n", a[2::2, ::2])

print("\n a[2::2, ::-1]=\n", a[2::2, ::-1]) # ::-1表示从最后一列开始往前数，

# A 3 dimensional array.
# ellipsis index operator
b = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24]]
])

print(b[..., 1])  # Equivalent to b[: ,: ,1 ]

a = np.array([[1, 2],
              [3, 4],
              [5, 6]
              ])
print(a[[0, 1, 2], [0, 0, 1]]) # Equivalent to a[0, 0] a[1, 0] a[2, 1]
print(*zip([0, 1, 2], [0, 0, 1]))

a = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])
print(a.shape)
print(a[1:2, 1:3])
print(a[1:2, [1, 2]])

a = np.array([10, 40, 80, 50, 100])
print(a[a>50])
# [80 100]

a = np.array([10, 40, 80, 50, 100])
print(a[a%40==0]**2)
# [1600 6400]


b = np.array([[5, 5],
              [4, 5],
              [16, 4]])
sumrow = b.sum(1) # 按行求和，求取的结果的行数与b的行数一致，
print(sumrow)
print(sumrow%10==0)
print(b[sumrow%10==0])

print(*[f'{x}_curve.png' for x in ('F1', 'PR', 'P', 'R')])