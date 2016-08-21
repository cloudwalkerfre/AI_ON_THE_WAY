#!/usr/bin/python
#coding:utf-8
import time
g_count = 100

def pTime():
    global g_count
    print time.strftime("%x %X", time.localtime())
    print g_count
    g_count += 1
