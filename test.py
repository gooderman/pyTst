#!/usr/bin/python3
import os
import sys
import shutil
import re
def tst_function() :
	print 'tst_function'
	sam = lambda a,b : a+b
	print 'tst_lambda',sam(100,200)


def tst_base() :
	g_var = 100
	a,b,c = 10,9.99,True
	print type(a),type(b),type(c)
	print isinstance(a,int),isinstance(b,float),isinstance(c,bool)	
	print not c
	print b/3,b//3,a%3,a**3

def tst_string() :
	name = 'jeep'
	print name+' is my name'
	print name*2
	print name[:2]
	print name[1:-1]
	print 'e' in name
	print 'k' in name
	print 'e' not in name
	print 'format %s,%d' % (name,100)
	print 'format {0}-{1}-{0}'.format(100,200)
	# print 'format {0:-4d}-{0:04d}-{0:04X}'.format(16)
	# print "format {aaa},{bbb}".format( "aaa"=100, "bbb"=200 )

def tst_list() :
	ll = []
	print ll
	ll.append(123)
	ll = ll + [456,789]
	print ll
	ll = [1,2,3,4,5,6,7,8,9,0]
	print ll[0:5]
	print ll[5:]
	print 2 in ll
	print 10 in ll

def tst_tupe() :
	tu = ()
	print tu
	tu = (100,) ## (100)==100
	print tu
	tu = (1,2,3,'abc')
	print tu
	print tu[2:]
	print 'abc' in tu
	print 100 in tu

def tst_set() :
	st0 = set()
	st1 = set('abcdefg')
	st2 = {'a','b','c',1,2,3}
	print st1,st2
	print st1 - st2
	print st1 | st2
	print st1 & st2
	print st1 ^ st2

def tst_dic():
	dic = {}
	print dic
	dic = {'a':1,'b':2,'c':'c'}
	print dic
	print dic['a'],dic['c']

def tst_if():
	a = 200
	b = 200
	if a>b :
		print 'a>b'
	elif a<b :
		print 'a<b'
	else :
		print 'a==b'			

def tst_for():
	a = 10
	while a>0 :
		print 'while %d' % a
		a-=1
	else:
		print 'while else'
	a = 10
	for i in range(a+1) :
		print 'for %d' % i
		if i==a :
			print 'for break'
			break
		else:
			print '  for continue'
			continue

	ll = [10,20,300,4000,50000]
	for i in ll:
		print 'for list %d' % i




	dic = {'a':1,'b':2,'c':3}
	for k in dic.keys() :
		print 'for dic %s=%d' % (k,dic[k])

	it = iter(dic.values())
	for k in it :
		print 'iter ',k

class A:
	name = ''
	age = 0
	kind = 'class'
	def __init__(self):
		name,age = 'older' ,100
	def print_info(self):
		print '%s,%d-%s' % (self.name,self.age,self.kind)

class B(A):
	def __init__(self,name,age):
		A.__init__(self)
		self.name,self.age = name,age	
def tst_class():
	a = A()
	a.print_info()
	b = B('jack',99)
	b.print_info()
	del a
	del b

def tst_file():
	filepath = os.path.join(os.getcwd(),'test.py')
	fd = open(filepath,'r')
	lines = file.readlines(fd)
	print '\n\n#############################'
	for i in range(len(lines)) :
		print ":%-4d %s" % (i,lines[i])
	print '#############################\n\n'
	file.close(fd)

def tst_re():
	content = "a name is jack,b name is lisa,c name is lucy"
	patten = r"(\w*)\sname\sis\s(\w*)[,]*"
	obj = re.match(patten,content)
	print obj.group()
	print obj.group(1)
	print obj.group(2)

	print re.findall(patten,content)
############################################
global g_var
tst_base()
# print 'g_var = ' , g_var
tst_function()
tst_string()
tst_list()	
tst_tupe()
tst_set()
tst_dic()
tst_if()
tst_for()
tst_class()
tst_file()
tst_re()
