#coding:utf-8
# import time

# x = 3
# print type(x)
# print x
# print x + 1
# print x * 2
# print x ** 2
# x += 1
# print x
# x *= 2
# print x
# y = 2.5
# print type(y)
# print y, y + 1, y * 2, y ** 2
# print '__________________________________________________________'

# t = True
# f = False
# print type(t)
# print t
# print t and f
# print t or f
# print not t
# print t != f


# print '__________________________________________________________'


# hello = 'hello'
# world = 'world'

# print len(hello)

# hw = hello + ' ' + world
# print hw

# hw12 = '%s, %s, %d' % (hello, world, 12)
# print hw12

# print '__________________________________________________________'


# s = 'hello'

# print s.capitalize()
# print s.upper()
# print s.rjust(7)
# print s.center(7)
# print s.replace('ll','g')

# print '__________________________________________________________'


# x = [3, 1, 2]
# print x, x[1]
# x[-1] = 'null'
# print x[2]
# print x
# x.append('2')
# print x
# print x.pop()
# num = range(12)
# print num
# print num[:10]
# print num[10:]
# print num[:-1]
# print num[2:4]
# num[2:4] = num[8:10]
# print num

# print '__________________________________________________________'

# some = range(10)
# for i in some:
#     print i

# for e, i in enumerate(some):
#     print '#%d, %d' % (e+1, i)

# square = []
# for i in some:
#     square.append(i ** 2)

# print square

# newSqur = [i ** 2 for i in some]
# print newSqur

# newSqur1 = [i ** 2 for i in some if i % 2 == 0]
# print newSqur1

# print '__________________________________________________________'

# d = {'a': 'b', 'c': 'd'}
# print d['a'], d['c'], 'a' in d, 'b' in d
# d['e'] = 'f'
# d['a'] = 'B'

# print d
# print d.get('a', 'N/A'), d.get('A', 'N/A'), d.get('A', 'NOT FOUND')
# del d['e']
# print d, len(d)

# for e, i in enumerate(d):
#     print '#%d, %s, %s' % (e+1, i, d[i])

# for e, f in d.iteritems():
#     print '%s, %s' % (e, f)

# x = range(4)
# y = {i:i ** 2 for i in x } 
# print y
# y = {i:i ** 2 for i in x if i != 0} 
# print y

# print '__________________________________________________________'


# some = {'a', 'b', 'c', 'd'}
# print some
# print 'a' in some, 'e' in some, len(some)
# some.add('e')
# print 'a' in some, 'e' in some, len(some)
# some.remove('a')
# print 'a' in some, 'e' in some, len(some)
# print some

# for e, i in enumerate(some):
#     print '#%d, %s' % (e+1, i)

# re = {x.upper() for x in some}
# print re

# re = {x.upper() for x in some if x != 'b'}
# print re

# from math import sqrt
# nums = {int(sqrt(x)) for x in range(30)}
# print nums



# print '__________________________________________________________'

x = {(x, x+1):(x - 1, x) for x in range(10)}
print  x

t = (5, 6)
print type(t)
print x[t], x[(1, 2)], t * 3

#只以逗号分隔, 默认位元组 (中文注释,加 - #coding:utf-8)
a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7
print a, b, c, d, e, f, g


# def sign(si):
#     if 0 in si:
#         return si
#     elif 5 in si:
#         return si
#     else:
#         return 'nothing'

# for xx in x:
#     print sign(xx), sign(x[xx])

def really(msg, bl = False):
    if bl:
        return msg
    else:
        return msg

print really('no'), really('yes', True)


# print '__________________________________________________________'

# print '__________________________________________________________'


# time.sleep(15)