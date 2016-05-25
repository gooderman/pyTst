#!/usr/bin/python
# -*- coding: UTF-8 -*-
#covert form csv by excel output(gb2312) to utf8(no bom)
import os
import sys,re
import string
import codecs
import shutil
#print "sys.arg ",len(sys.argv)
def isconvert(infile,end):
	return re.match(".+"+end+"$",infile)
def cvt(infile):
	f=open(os.path.join(os.getcwd(),infile),"rb")
	o=open(os.path.join(os.getcwd()+"/out/",infile),"wb")
	s=os.path.getsize(os.path.join(os.getcwd(),infile))
	buff = f.read(s)
	if buff[0]=='\xef' and buff[1]=='\xbb' and buff[2]=='\xbf':
		#buff = buff[3:s+1]
		f.close()
		o.write(buff)
		o.close()
		print "no cvt",infile
	else:		
		#a_unicode = buff.decode('gb2312')
		#first conver to utf8
		a_unicode = buff.decode('gb2312')
		buff = a_unicode.encode("UTF-8")
		f.close()
		o.write("\xef\xbb\xbf")
		o.write(buff)
		o.close()
		print "cvt ok",infile
	
def cvtdir(dir,end):
	flist=[]	
	for parent,dirnames,filenames in os.walk(dir):	#三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
		#for dirname in dirnames:	#输出文件夹信息
			#print "parent is:" + parent
			#print "dirname is" + dirname
			#print "dir : "+os.path.join(parent,dirname)
		for filename in filenames:                        #输出文件信息
			#print "parent is:" + parent
			#print "filename is:" + filename
			tup1 = os.path.splitext(filename)
			if tup1[1]==end:
				#print "file: " + os.path.join(parent,filename) #输出文件路径信息
				flist.append(filename)
			#else:
				#print "file no csv"		
	for v in flist:
		#print "ccvt ",v
		try:
			cvt(v)
		except BaseException:
			print 'cvt error:',v
			os.system("pause")
if os.path.isdir(os.getcwd()+"/out/"):
	print "remove out"
	os.system("rd /s /q out")
	#os.rmdir(os.getcwd()+"/out/")
os.mkdir(os.getcwd()+"/out/")
cvtdir(os.getcwd(),'.csv')
os.system("pause")
