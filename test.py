#!/usr/bin/python3
import os
import sys
import shutil
import re
import json
import zipfile
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
	name = 'http://ab.com/ui new/abc def.png'
	print 'find space %d' % name.find(" ")
	name = 'http://ab.com/ui_new/abc_def.png'
	print 'find space %d' % name.find(" ")

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
	print "list len=%d" % len(ll)

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
	filepath = os.path.join(os.getcwd(),'tst.txt')
	fd = open(filepath,'r+w')
	lines = file.readlines(fd)
	print '\n\n#############################'
	for i in range(len(lines)) :
		print ":%-4d %s" % (i,lines[i])
	print '#############################\n\n'
	file.write(fd,'123456789\r\n')
	file.close(fd)

def tst_re():
	content = "a name is jack,b name is lisa,c name is lucy"
	patten = r"(\w*)\sname\sis\s(\w*)[,]*"
	obj = re.match(patten,content)
	print obj.group()
	print obj.group(1)
	print obj.group(2)

	print re.findall(patten,content)

def tst_json():
	print 'sys.argv', len(sys.argv), sys.argv
	jstr='[1,2,3,4]'
	print json.loads(jstr)
	# strdata = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
	# dic = json.loads(strdata)
	# if dic:
	# 	print dic
	# 	print dic['a']
def tst_zip():
	zf = zipfile.ZipFile('zz.zip','w',zipfile.ZIP_DEFLATED)
	zf.write('tst.txt','/aaa/Ztst.txt')
	info  = zf.getinfo('aaa/Ztst.txt')
	print info.filename
	print info.date_time
	print info.compress_type
	print info.file_size
	print info.compress_size
	print info.CRC
	zf.close()

	zf = zipfile.ZipFile('zz.zip','r')
	zf.extractall(os.path.join(os.getcwd(),'zdir/'))
	infos  = zf.infolist()
	for info in infos:
		print info

def tst_os():
    # for k in os.environ.keys():
    # 	print k+"  :  "+os.environ[k]
	print os.name
	ppp = os.path.join(os.getcwd(),"abc")
	if os.path.exists(ppp):
		for root,dirs,files in os.walk(ppp,False):
			print root
			print dirs
			print files
			for file in files:
				os.remove(os.path.join(root,file))
			for dd in dirs:
				os.rmdir(os.path.join(root,dd))
		os.removedirs(ppp)
	os.mkdir(ppp)
	os.makedirs(os.path.join(ppp,"def/hij/abc"))
	print os.listdir(ppp)

def tst_exception():
	 raise Exception("tst_exception")

# print 'g_var = ' , g_var
# tst_function()
tst_string()
tst_list()	
# tst_tupe()
# tst_set()
# tst_dic()
# tst_if()
# tst_for()
# tst_class()
# tst_file()
# tst_re()
# tst_json()
# tst_zip()
tst_os()
tst_exception()
