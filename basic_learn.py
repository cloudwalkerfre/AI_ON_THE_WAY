#coding:utf-8
import time
import calendar 
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

# x = {(x, x+1):(x - 1, x) for x in range(10)}
# print  x

# t = (5, 6)
# print type(t)
# print x[t], x[(1, 2)], t * 3

# #只以逗号分隔, 默认位元组 (中文注释,加 - #coding:utf-8)
# a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7
# print a, b, c, d, e, f, g


# def sign(si):
#     if 0 in si:
#         return si
#     elif 5 in si:
#         return si
#     else:
#         return 'nothing'

# for xx in x:
#     print sign(xx), sign(x[xx])

# def really(msg, bl = False):
#     if bl:
#         return msg
#     else:
#         return msg

# print really('no'), really('yes', True)


# print '__________________________________________________________'

# class FC(object):
#     def __init__(self, name):
#         self.name = name

#     def greet(self, Upper = False):
#         if Upper:
#             print self.name.upper()
#         else:
#             print self.name

# f = FC('names Jame')
# f.greet()
# f.greet(True)
# class messageMaster:
#     'I know all'
#     mc = 0

#     def __init__(self):
#         print 'Master\'ve been made!' 

#     def MC_Count(self):
#         print 'Master tell you: ', messageMaster.mc

#     def ackNew(self):
#         messageMaster.mc += 1

#     def ackDel(self):
#         messageMaster.mc -= 1

# mes = messageMaster()

# class Cdemo:
#     '说明'
#     Ccount = 0  

#     def __init__(self, name):
#         self.name = name
#         Cdemo.Ccount += 1
#         mes.ackNew()

#     def __del__(self):
#         if hasattr(self, 'name'):
#             print self.name,
#         print 'I\'m done'
#         mes.ackDel()        

#     def pCount(self):
#         print 'TOTAL: %d' % Cdemo.Ccount

#     def pName(self):
#         print 'NAME: %s' % self.name

# p = Cdemo('nice')
# p.pCount()
# p.pName()
# print hasattr(p, 'name')
# print hasattr(p, 'age')
# print getattr(p, 'name')
# print setattr(p, 'name', 'not_nice')
# p.pName()
# print delattr(p, 'name')
# print setattr(p, 'ok', 'not_nice')
# print getattr(p, 'ok')

# p.name = 'reset'
# p.age = 0
# p.pName()
# del p.name
# print hasattr(p, 'name')
# print hasattr(p, 'age')
# print getattr(p, 'age')

# q = Cdemo('again')

# mes.MC_Count()
# del p
# mes.MC_Count()
# del q
# mes.MC_Count()

# print '---'
    
# print 'doc:', Cdemo.__doc__
# print 'name:', Cdemo.__name__
# print 'module:', Cdemo.__module__
# print 'bases:', Cdemo.__bases__
# print 'dict:', Cdemo.__dict__


# print '__________________________________________________________'


# a, b = (1, 2), (3, 4)
# print cmp(a, b)

# c, d = (1, 'a'), (1, 'b')
# print cmp(c, d)

# e, f = (1, 'a'), (2, 'a')
# print cmp(e, f)

# # compare number first
# g, h = (1, 'b'), (2, 'a')
# print cmp(g, h)

# # auto type change
# i, j = (1, 1), (1.1, 1)
# print cmp(i, j)

# # number is consider the least
# k, l = (1, 'a'), ('a', 1)
# print cmp(k, l)

# print len(k), len((1, 2, 3))
# print max((1, 2, 3)), max((1, 2, 'a', 'b'))
# print min((1, 2, 3)), min((1, 2, 'a', 'b'))

# x = [1, 2, 3]
# y = tuple(x)

# print x, y, type(x), type(y)


# dic = {'a': 1, 'b': 2, 'c': 3}
# print str(dic), len(dic), type(dic)

# dir = dic.copy()

# dic.clear()
# print str(dic), len(dic), type(dic)
# print str(dir), len(dir), type(dir)

# dnew = dir.fromkeys(dir)
# print str(dnew), len(dnew), type(dnew)
# dnew = dir.fromkeys(dir, 123)
# print str(dnew), len(dnew), type(dnew)

# print dnew.get('a', 'no such')
# print dnew.get('d', 'no such')
# print dnew.has_key('a'), dnew.has_key('d')

# print dnew.items(), dnew.items()[0]
# print dnew.keys(), dnew.keys()[0]

# dnew.setdefault('d', 4)
# dnew['a'] = 1

# print str(dnew)
# print str(dir)
# dir.update(dnew)
# print str(dir)

# print dnew.values(), dnew.values()[0]

# print '__________________________________________________________'

# print time.strftime("%Y-%m-%d %a %A %b %B %l %y %H:%M:%S %c %j %p %U %w %Z", time.localtime())
# print time.strftime("%x %X", time.localtime())
# a = time.strftime("%Y-%m-%d %a %b %H:%M:%S", time.localtime())
# print time.mktime(time.strptime(a, "%Y-%m-%d %a %b %H:%M:%S"))

# b = time.clock()
# print  calendar.month(2016, 8)
# print time.clock() - b
# print time.time(), time.timezone
# print time.ctime(time.time())

# print calendar.isleap(2016), calendar.monthcalendar(2016, 8)
# print calendar.weekday(2016, 8, 28)



# print '__________________________________________________________'

something = raw_input()
print something







# print '__________________________________________________________'



# time.sleep(15)