import numpy as np

# 1-d array - vector
# 2-d array - matrix
# 3-d array - tensor

x = [1, 2, 3, 4, 5]
y = np.array(x)
print(y.ndim)
print(type(y))
print(y.shape)

# reshape into 2-d array

y = y.reshape(5,1)
print(y.shape)

# a = [1, 2, 3, 4, 5, 6]

# create an array with 6 elements

# b = np.arange(6)
# b = b.reshape(2, 3)
# print(b)
# print(b.shape)

# number of ways in which we can reshape (1,6), (6,1), (2,3), (3,2)

# 3-d array

# c = np.array([[[10, 20, 30]], [[30, 40, 50]], [[1, 2, 3]]])
# print(c)

# e = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
#               [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
# print(e)
# print(e.shape)

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print(c.shape)
print(c.ndim)

# zero matrix

z = np.zeros(4)
print(z)
print(z.dtype)

z1 = np.zeros((3,4))
print(z1)

# convert float 0 to int 0

z2 = np.zeros((3, 4), dtype=int)
print(z2)

# ones matrix

z3 = np.ones(4, dtype=int)
print(z3)

z4 = np.ones((4, 3), dtype=int)
print(z4)

z5 = np.ones((3, 5), dtype=int)
z5 = z5*6
print(z5)

r = np.random.randint(10)
print(r)

r1 = np.random.randint(50, size=(5, 3))
print(r1)

# identity matrix

id = np.eye(4, dtype=int)
print(id)

# diagonal matrix

id1 = np.diag((1, 2, 3))
print(id1)