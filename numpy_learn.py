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

# pirnt members in class np.array
types = [type(i) for i in [0, "0", [0], {0:1}, (0,)]]
content = ""
for k in dir(np.array):
    content += "%s: %s\n" % (k, type(eval("np.array.%s" % k)))
    if type(eval("np.array.%s" % k)) in types:
        pass
        content += "%s\n" % str(eval("np.array.%s" % k))
    content += "\n"
print content