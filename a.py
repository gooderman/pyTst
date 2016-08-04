#!/usr/bin/python
# -*- coding: UTF-8 -*-
def look():
	print "def function look"
look()
print '================================='
print "and False and 1 or 2\t",False and 1 or 2
print "and True and 1 or 2\t",True and 1 or 2
exec("print 'exec'")
print "not True\t",not True
print "not False\t",not False
print "not 1==2\t",not 1==2
print '================================='
try:
	print "try"
	a=1
	b=2
	assert a==b
except AssertionError:
	print "except assert 1==2","error"
finally:
	print "finally"
print '================================='	
for i in range(1,5):
	print "for",i
	if i==3:
		print "continue"
		continue
	elif i==4:
		print "break"
		break
	elif i==2:
		pass
		print 'pass'
print '================================='
print 'Tc class'		
class Tc(object):
	"""Tc name of class"""
	def __init__(self, arg):
		self.arg = arg
	def __log___(self):
		print self.arg
tc = Tc('ins of Tc')
tc.__log___()	
del tc
try:
	tc.__log___()
except BaseException:
	print 'tc is del'
else:
	print 'no exception'	
print '================================='	
from math import pi
print 'from math import pi',pi
import os
print 'import os os.getcwd',os.getcwd()
print "os.getevn",os.getenv('PATH')
print '================================='
def tstglobal():
	global y
	y=100
	global x
	x=200
	print "global y",y
	print "global x",x
x=100
print 'before x',x
tstglobal()	
print 'after x',x
print 'after y',y		
print '================================='
try:
	raise AssertionError
except BaseException:
	print "raise exception"
print '================================='
a=200
del a
print "del a"
print '================================='
a=8
while a<=10:
	print "while ",a
	a-=1
	a+=1.5
print '================================='
a=8
b=8
c='cd'
d='cd'
print "a is b",a is b,a,b
print "c is d",d is d,c,d	
print '================================='
a=[1,2,3,4,5]
print(a[2:4])
print '================================='
class Cw(object):
	"""docstring for Cw"""
	def __init__(self, arg):
		super(Cw, self).__init__()
		self.arg = arg
	def __exit__(self,type,value,traceback):
		print "Cw exit"
	def __enter__(self):
		print "Cw enter"
		return 'Cw ist'		

with Cw('cw ins') as b:
	print "cw_with ",b
print '================================='
print "yield"
def func():
	for i in range(1,10):
		yield i*100
f = func()
print "f.next",f.next()
print "f.next",f.next()
print "f.next",f.next()
print "f.next",f.next()
print "f.next",f.next()
print '================================='
l = lambda a,b,c:a*b*c
print 'lambda a,b,c:a*b*c','2,4,10',l(2,4,10)
print '================================='
q='''123
abc
456
'''
print "multi line\n",q
print '================================='
print "raw_input"
#abc = raw_input(r"\n\nplease input")
#abc = raw_input("\n\nplease input:\t")
#print "input ",abc
print '================================='
print 1/2.0
print 1//2.0
print 1%2
print 2**3
print 10.0/3
print 10%3
print 10.0//3
print '================================='
print "list"
a=[1,2,3,4,5]
print a*2
print a[0:4]*2
print a+[6]+[7]+[8]
del a[0],a[0],a[0]
print a
a[0]=100
print a
for i in a:
	print "i in list a",i
print '================================='
print 'tuple'
tp=(1,2,3)
try:
	tp[0]=100
except BaseException:
	print "tuple cant be modify value"
print tp*2
print tp[0:2]
for	i in tp:
	print "i in tuple tp ", i
print '================================='
st={'a':'A','b':'B','c':'C',100:'10D'}
print st
print st.keys()
print st.values()
print st['b']
print st[100]
print '================================='
print int("243")
print str(123)
print long(123)
print float("123.789")
print list((1,2,3,4,5))
print tuple([1,2,3,4,5,6])
print set((1,2,3,4,5))
print ord('0')
print ord(';')
print hex(10)
print oct(10)
print '================================='
import calendar
cal = calendar.month(2016,5)
print cal
import time
print time.time()
print time.localtime(time.time())
ltm = time.localtime(time.time())
print ltm.tm_year,ltm.tm_mon,ltm.tm_mday,ltm.tm_hour,ltm.tm_min,ltm.tm_sec
print ltm.tm_wday,ltm.tm_yday,ltm.tm_isdst
print '================================='
fo = open('a.lua','r')
print fo.name
print fo.closed
print fo.mode
print fo.softspace
print fo.readline()
print fo.next()
print fo.next()
print fo.next()
print fo.next()
print fo.next()
print fo.next()
fo.close()
if(not os.path.isdir("bbb")):
	os.mkdir("bbb")
else:
	print "bbb \tisdir\texsit"	
	os.rmdir('bbb')
dirs = os.listdir(os.getcwd())
# 输出所有文件和文件夹
for file in dirs:
   print file,"\tisdir\t",os.path.isdir(file)
print os.path.abspath('bbb')
print os.path.splitext("d:/python/a.lua")
print os.path.split("d:/python/a.lua")
print os.path.dirname("d:/python/a.lua")
print os.path.basename("d:/python/a.lua")
print os.path.isabs("d:/python/a.lua")
print os.path.isabs("d:/python/a")
print os.path.isfile("a.lua")
print '================================='
bb=None
if os.path.isfile('a.yy'):
	bb=1	
if not bb:
	print "bb.t is None"
else:
	print "bb is\t",bb	
if None <> False:
	print "None <> False"
if None != False:
	print "None != False"	

print '================================='
print os.sys.api_version
print os.sys.byteorder
print os.sys.copyright
os.system("dir");
print '================================='
print "type(os)",type(os)
print "type(int)",type(5)
print "type(None)",type(None)
print "type(look)",type(look)
print "type(type(look))",type(type(look))
print "type([1,2,3])",type([1,2,3])
print "type((1,2,3)",type((1,2,3))
print "type({'1':2})",type({'1':2})
if type(5)==int:
	print "type(5)==int"
if type('abc')==str:
	print "type('abc')==str"
if type([1,2,3])==list: #tuple dict
	print "type('[1,2,3]')==list"
#if type(look)==function:
#	print "type(look)=='function'"
print '================================='
print "httplib"
import httplib
import urllib
try:
	con = httplib.HTTPSConnection("cn.bing.com")
	con.request("GET","/","",{"auth":"jeep"})
	httpres=con.getresponse()
	print httpres.status  
	print httpres.reason
	body = httpres.read(140)
	print len(body)
	import re
	rst = re.search(r"(EN).*((html){3})(.*)","ENppop \" \"> fadsfffhtmlhtmlhtml---fds")
	#print body
	#rst = re.search(r"(EN).*?(html ){3}(.*).*",body)
	if rst:
		print "rst 0",rst.group()
		print "rst 1",rst.group(1)
		print "rst 2",rst.group(2)
		print "rst 3",rst.group(3)
		print "rst 4",rst.group(4)
	else:
		print "rst None"
except BaseException,Arguments:
	print "except httplib ",Arguments
finally:
	print "finally httplib "
print '================================='
print 'string.format'
item='{"%s","%s",%d}'%("a","B",123)
#item=R'{ "%s" , "%s" , %d }'%("a","B",123)
print item
item="{name},{size}".format(name="Lisa",size=100)
print item
print '================================='