#coding:utf-8
import urllib2
import threading
import Queue
import time

# a = '淡鬼'
# print a.find('淡鬼', 0, len(a))

exitFlag = 0

class qTread(threading.Thread):
    def __init__(self, threadID, threadName, qWorking):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.qWorking = qWorking
    def run(self):
        print 'starting:', self.threadName
        process(self.threadID, self.threadName, self.qWorking)
        print 'exiting:', self.threadName

def process(ID, name, qWorking):
    global exitFlag
    speedo = 0.001
    count = 0
    while not exitFlag: 
        if not qWorking.empty():
            queLcok.acquire()
            que = qWorking.get()
            print 'processing:', name, '-', que
            queLcok.release()
            try:
                response = urllib2.urlopen("http://jandan.duoshuo.com/api/users/profile.json?user_id=%d" % que)
                if response.read().find('淡鬼', 0, len(response.read())) != -1:
                    f = open('DBS.txt', 'r+')
                    f.write(response.read())
                    print '====== FIND TARGET ======'
                    exitFlag = 1
            except:
                print 'ERROR'   
            count = 0
            speedo = 0.001 
        else:
            # print ID, 'Que empty'
            time.sleep(speedo)
            count += 1
            speedo += count * 0.001


qW = Queue.Queue(600)
queLcok = threading.Lock()
threads = []

for i in range(30):
    T = qTread(i + 1, '#Thread%s' % str(i+1), qW)
    T.start()
    threads.append(T)
time.sleep(1)

data = range(100000)
for i in data:
    speedo = 0.0001
    count = 0
    tmp = 1500000 + i + 1
    while qW.full():
        # print 'data waiting for put:', tmp
        time.sleep(speedo)
        count += 1
        speedo += count * 0.001
    queLcok.acquire()
    qW.put(tmp)
    queLcok.release()
    # print 'Que put:', tmp
    #   time.sleep(random.uniform(0, 0.5))

time.sleep(10)
exitFlag = 1

for t in threads:
    t.join()

print '-- WE DONE HERE --'

while 1:
    pass