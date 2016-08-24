#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

# # Compute the x and y coordinates for points on sine and cosine curves
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# # Plot the points using matplotlib
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()

# a = np.array([1, 2, 3])
# print type(a)
# print a.shape
# print a[0], a[1], a[2]
# a[0] = 5
# print a

# b = np.array([[1, 2, 3], [4, 5, 6]])
# b_c = np.array([[1, 2, 3], [4, 5, 8]])

# print b
# print b.shape
# print b[0, 0], b[0, 1], b[1, 0]

# print b_c, b_c.shape, b_c[1]
# b_c[1] = [4, 5, 6]
# print b_c, b_c.shape


# a = np.zeros((2, 2))
# print a

# b = np.ones((3, 2))
# print b

# c = np.full((2,4), 4)
# print c

# d = np.eye(2)
# e = np.eye(3)
# print d, e

# f = np.random.random((2, 2))
# print f, f[0, 1], f[1, 0], f[:1, 0:], f[:1, 1:]

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# b = a[:2, 1:3]
# print a.shape, b.shape
# print b[0, 0]
# b[0, 0] = 12
# print b, a
# c = a[0, :]
# d = a[0,]
# print c, d

# row_r1 = a[1, :]
# row_r2 = a[1:2, :]

# col_r1 = a[:, 1]
# col_r2 = a[:,1:2]

# print row_r1, row_r2, col_r1, col_r2
# print type(row_r1[0]), type(row_r2[0]), type(row_r2[0][0])
# print a[[0, 1, 2], [0, 1, 2]], np.array(a[[0, 1, 2], [0, 1, 2]])
# print dir(np.array)

# # pirnt members in class np.array
# types = [type(i) for i in [0, "0", [0], {0:1}, (0,)]]
# content = ""
# for k in dir(np.array):
#     content += "%s: %s\n" % (k, type(eval("np.array.%s" % k)))
#     if type(eval("np.array.%s" % k)) in types:
#         pass
#         content += "%s\n" % str(eval("np.array.%s" % k))
#     content += "\n"
# print content


# print a.dtype, np.array([1.0]).dtype
# x = np.array([1, 2], dtype = np.float64)
# print x.dtype, x[0]
# y = x[:]
# y.dtype = np.int64
# print y.dtype, y[0], y.shape, len(y)

# dt = np.dtype('>i4')
# print dt.byteorder, dt.itemsize, dt.name, dt.type

# ndt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
# print ndt['name'], ndt['grades']

# dt = np.array([('Name1', (8.0, 7.0)), ('name2', (6.0, 5.0))], dtype = ndt)
# print dt, dt["name"], dt['grades'], dt[0]['name'], dt[1]['grades']



# 'b'	boolean
# 'i'	(signed) integer
# 'u'	unsigned integer
# 'f'	floating-point
# 'c'	complex-floating point
# 'm'	timedelta
# 'M'	datetime
# 'O'	(Python) objects
# 'S', 'a'	(byte-)string
# 'U'	Unicode
# 'V'	raw data (void)

# dt = np.dtype('i4')   # 32-bit signed integer
# dt = np.dtype('f8')   # 64-bit floating-point number
# dt = np.dtype('c16')  # 128-bit complex floating-point number
# dt = np.dtype('a25')  # 25-character string

#--------------------------------------------------
# field named f0 containing a 32-bit integer
# field named f1 containing a 2 x 3 sub-array of 64-bit floating-point numbers
# field named f2 containing a 32-bit floating-point number
# >>> dt = np.dtype("i4, (2,3)f8, f4")

#--------------------------------------------------
# field named f0 containing a 3-character string
# field named f1 containing a sub-array of shape (3,) containing 64-bit unsigned integers
# field named f2 containing a 3 x 4 sub-array containing 10-character strings
# >>>
# >>> dt = np.dtype("a3, 3u8, (3,4)a10")

# Type strings

# Any string in numpy.sctypeDict.keys():
# Example
# >>>
# >>> dt = np.dtype('uint32')   # 32-bit unsigned integer
# >>> dt = np.dtype('Float64')  # 64-bit floating-point number
# (flexible_dtype, itemsize)

# The first argument must be an object that is converted to a zero-sized flexible data-type object, the second argument is an integer providing the desired itemsize.
# Example
# >>>
# >>> dt = np.dtype((void, 10))  # 10-byte wide data block
# >>> dt = np.dtype((str, 35))   # 35-character string
# >>> dt = np.dtype(('U', 10))   # 10-character unicode string

# dt = np.dtype("a3, 3u8, (3,4)a10")
# ndt = np.array(('ab',(123, 123, 123),(('abc', 'abc', 'abc', 'abc'), ('abc', 'abc', 'abc', 'abc'), ('abc', 'abc', 'abc', 'abc'))),dtype = dt)
# print ndt

# exp = np.array([(1, 2), (3, 4), (5, 6)])
# print exp.shape

# dj = np.dtype({'names':['t1', 't2', 't3', 't4'], 'formats':['a10']*4})
# dk = np.dtype({'names':['f1','f2','f3'], 'formats':[dj]*3})
# dt = np.dtype([('first', 'a3'), ('second', '3u8'), ('third', dk)])
# ndt = np.array(('ab',(123, 123, 123),(('abc', 'abs', 'abc', 'abc'), ('abc', 'abc', 'abc', 'abc'), ('abc', 'abc', 'abc', 'abc'))),dtype = dt)
# print ndt, ndt['third']
# print ndt['third']['f1'], ndt['third']['f1']['t2'], ndt['third']

# bool_idx = (ndt['third']['f1']['t2'] > 'abc')
# print bool_idx

# print (a > 2), a[a <= 2]

b = np.array([[12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]])

# print a + b, np.add(a, b)
# print a - b, np.subtract(a, b)
# print a * b, np.multiply(a, b)
# print a / b, np.divide(a, b)
# print np.sqrt(a, b)
# print a.dot(b.T), np.dot(a, b.T)

# axis=0 - 列之和, axis=1 - 行之和 
# print np.sum(a), np.sum(a, axis = 0), np.sum(a, axis = 1), np.sum(a, 0), np.sum(a, 1)

# c = np.empty_like(a)

# for i in range(3):
#     c[i, :] = a[i, :] + np.array([1, 0, 1, 0])

# print c

# d = np.tile(np.array([1, 0, 1, 0]), (3, 1))
# print a + d


v = np.array([1, 2, 3])
w = np.array([4, 5])

print np.reshape(v, (3, 1)), np.reshape(v, (3, 1)).T
print np.reshape(v, (3, 1)) * w
print np.array([[i + 1] for i in range(3)]) * w

