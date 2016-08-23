#coding:utf-8
import time
# import calendar 
# import math
import random
import re
import thread
import threading
# import Queue
# import pymongo
# from bson.code import Code
import os


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

# something = raw_input()
# print something   

# print '__________________________________________________________'


# print math.ceil(1.1)
# print math.floor(1.1)

# print abs(-10)
# print math.fabs(-10)

# print math.log(8, 2)
# print math.log10(100)

# print math.modf(1.1)
# print math.pow(2, 3)
# print math.sqrt(4)


# print random.random()
# print random.choice(range(10))
# print random.randrange(10, 100, 5)
# x = range(10)
# print x
# random.shuffle(x)
# print x
# print random.uniform(1, 2)

# print math.degrees(math.acos(0.5))
# print math.radians(math.degrees(math.acos(0.5)))
# print math.cos(math.pi / 3)
# print math.sin(math.pi / 6)
# print math.degrees(math.asin(math.sqrt(0.75)))
# print math.radians(math.degrees(math.asin(math.sqrt(0.75))))


# print '__________________________________________________________'

# var1 = 'hello ha'
# var2 = var1[:6] + '\n\000cloudwalker'
# print var2

# print '\v1 \t2 \r \f'
# print r'\v1 \t2 \r \f'
# print R'\v1 \t2 \r \f'

# var3 = range(3)
# var4 = ['#%d: %s' % (e + 1, i) for e, i in enumerate(var3) ]
# print var4

# ht = ''' I'm gonna type in what ever the fuck
# I want to type, yeah !#%$%&^*(&()&&$&%^(&))
# and you gonna copy'''

# print ht,'\n',ht.capitalize(), '\n', ht.upper()
# print ht.count('I', 0, len(ht))
# print ht.find('I', 0, len(ht))
# print ht.index('I', 0, len(ht))
# print ht.isalnum()
# print ht.isalpha()
# print str(var3).isdigit()
# encode = ht.encode('base64', 'strict')
# decode = encode.decode('base64', 'strict')
# print encode, decode
# seq = ('a', 'b', 'c')
# print ' - '.join(str(range(10)))
# print '-'.join(seq)
# print u'hello\u0020world'

# print str(var3).center(5)

# print '__________________________________________________________'

# line = "Cats are smarter than dogs"

# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# for i in matchObj.groups():
#     print i
# print matchObj.group(), len(matchObj.groups())

# ipn = '192.168.1.1 shdfh'

# mp = re.match('((2[0-4]\d|25[0-5]|[01]?\d\d?.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?))', ipn, re.M|re.I)
# print mp.group(0)    

# s = 'abcdefghijklmnopq'
# sp = re.match('\w{3}', s, re.M)









# print '__________________________________________________________'

# def pTime(pName, count):
#     i = 0  
#     while i < count:
#         time.sleep(1)
#         print "%s: %s" % (pName, time.ctime(time.time()))
#         i += 1

# try:
#     thread.start_new_thread(pTime, ('p2', 10,))
#     thread.start_new_thread(pTime, ('p1', 5,))
# except:
#     print 'erro'

# exitFlag = 0

# class cp(threading.Thread):
#       def __init__(self, threadID, name, count):
#             threading.Thread.__init__(self)
#             self.threadID = threadID
#             self.name = name
#             self.count = count
#       def run(self):    
#             print 'starting:', self.name
#             threadLock.acquire()
#             pTime(self.name, self.count)
#             threadLock.release()
#             print 'exiting:', self.name
# def pTime(name, count):
#       i = 0
#       while i < count:
#             if exitFlag: break
#             time.sleep(1)
#             print '%s: %s' % (name, time.ctime(time.time()))
#             i += 1
      
# threadLock = threading.Lock()
# threads = []

# cp1 = cp(1, "p1", 10)
# cp2 = cp(2, "p2", 5)

# cp2.start()
# cp1.start()

# threads.append(cp1)
# threads.append(cp2)

# for t in threads:
#       t.join()
# print 'ALL DONE'


# time.sleep(3)
# exitFlag = 1


# # 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print "%s: %s" % ( threadName, time.ctime(time.time()) )

# # 创建两个线程
# try:
#    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print "Error: unable to start thread"


# exitFlag = 0

# class qTread(threading.Thread):
#       def __init__(self, threadID, threadName, qWorking):
#             threading.Thread.__init__(self)
#             self.threadID = threadID
#             self.threadName = threadName
#             self.qWorking = qWorking
#       def run(self):
#             print 'starting:', self.threadName
#             process(self.threadID, self.threadName, self.qWorking)
#             print 'exiting:', self.threadName

# def process(ID, name, qWorking):
#       while not exitFlag: 
#             if not qWorking.empty():
#                   queLcok.acquire()
#                   print 'processing:', name, '-', qWorking.get()
#                   queLcok.release()
#                   time.sleep(0.2)
#                   # print 'finishing:', name, '-', qWorking.get()
#             else:
#                   print ID, 'Que empty'
#             time.sleep(random.uniform(1, 2))

# qW = Queue.Queue(10)
# queLcok = threading.Lock()
# threads = []

# for i in range(5):
#       T = qTread(i + 1, '#Thread%s' % str(i+1), qW)
#       T.start()
#       threads.append(T)

# ###STRAT
# st = time.time()


# # data = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g')*10
# data = range(200)
# for i in data:
#       while qW.full():
#             print 'data waiting for put:', i
#             time.sleep(0.5)
#       queLcok.acquire()
#       qW.put(i)
#       queLcok.release()
#       print 'Que put:', i
#       time.sleep(random.uniform(0, 0.5))

# time.sleep(10)
# exitFlag = 1

# for t in threads:
#       t.join()


# ###FINSIN
# ft = time.time()
# print (ft - st)/200

# print '__________________________________________________________'


# client = pymongo.MongoClient("localhost", 27017)
# db = client.pymo_learn
# print db.collection_names()#, db.firstMsg.find_one()
# fMsg = db.firstMsg
# # for i in range(10):
# #       fMsg.insert({('test%d' % (i + 3)):('newMSG%d' % (i+3))})
# for i in fMsg.find():
#       print i
# print fMsg.find_one({'test4':''}), fMsg.find().count()


# s = [{'N_ID':'%d' % (x + 1),'u_Time':'%s' % str(time.time())}  for x in range(150)]
# fMsg.insert_many(s)
# print fMsg.find().count()

# mapper = Code('''
#             function(){
#                   this.N_ID.forEach(function(z){
#                         emit(z, 1);
#                   });
#             }
#             ''')

# reducer = Code('''
#             function(key, values){
#                   var total = 0;
#                   for(var i = 0; i < values.length; i++){
#                         total += values[i];
#                   }
#                   return total;
#             }
#             ''')

# results = fMsg.map_reduce(mapper, reducer, "myresults")
# for r in results:
#       print r

# print '__________________________________________________________'


# f = open('py_file_test.txt', 'r+')
# print f.name, f.closed, f.mode, f.softspace
# try:
#       # f.write('LINE5: d')
#       # print f.read(), f.tell()
#       # f.seek(0, 0)
#       # print f.tell()
#       # os.rmdir('pydir') 
#       print os.getcwd()

#       for l in f.readlines():
#             print l

#       f.seek(0, 0)
#       tmp = f.readlines()
#       print len(tmp), str(tmp)
#       t = tmp[4]
#       tmp[4] = tmp[3]
#       tmp[3] = t
 
#       f.seek(0, 0)
#       f.writelines(tmp)

#       f.seek(0, 0)
#       for l in f.readlines():
#             print l

# except ValueError, Argument:
#       print 'I/O Error', Argument

# f.close()

# print '__________________________________________________________'


# import time_p
# p = time_p.pTime
# p()
# p()
# p()
# reload(time_p)
# p()
# p()
# p()

# print '__________________________________________________________'

# MAKE SURE CONSOLE STAYS -- So at least I can see ...
# while 1:
#       pass