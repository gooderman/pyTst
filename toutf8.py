#!/usr/bin/python
# -*- coding: UTF-8 -*-
#covert form csv by excel output(gb2312) to utf8(no bom)
import os
import sys,re
import string
import codecs
import shutil
import time
#print "sys.arg ",len(sys.argv)
has_error=False
def isconvert(infile,end):
	return re.match(".+"+end+"$",infile)
#read base and combine fortask to out
def cvt(infile):
	f=open(os.path.join(os.getcwd()+"/base/",infile),"rb")
	o=open(os.path.join(os.getcwd()+"/out/",infile),"wb")
	s=os.path.getsize(os.path.join(os.getcwd()+"/base/",infile))
	buff = f.read(s)
	if buff[0]=='\xef' and buff[1]=='\xbb' and buff[2]=='\xbf':
		#buff = buff[3:s+1]
		f.close()
		o.write(buff)
		#'''
		rbuf = read_fortask(infile)
		if rbuf!=None:
			o.write(rbuf)
			print "cmb ok",infile
		#'''	
		o.close()
		print "no cvt",infile
	else:		
		#a_unicode = buff.decode('gb2312')
		#first conver to utf8
		'''
		try:
			a_unicode = buff.decode('gb2312')
		except BaseException,e:
			a_unicode = buff.decode('gbk')
		'''	
		a_unicode = buff.decode('gbk')	
		buff = a_unicode.encode("UTF-8")	
		f.close()
		o.write("\xef\xbb\xbf")
		o.write(buff)
		#'''
		rbuf = read_fortask(infile)
		if rbuf!=None:
			o.write(rbuf)
			print "cmb ok",infile
		#'''	
		o.close()
		print "cvt ok",infile

def read_fortask(infile):
	allpath=os.path.join(os.getcwd()+"/fortask/",infile)
	if not os.path.isfile(allpath):
		return
	f=open(allpath,"rb")
	if(f==None):
		return
	s=os.path.getsize(allpath)
	buff = f.readline()
	f.readline()
	cur = f.tell()
	buff3 = f.read(s-cur)
	if buff[0]=='\xef' and buff[1]=='\xbb' and buff[2]=='\xbf':
		#buff = buff[3:s+1]
		f.close()
		return buff3[3:s+1]
	else:		
		#a_unicode = buff.decode('gb2312')
		#first conver to utf8
		'''
		try:
			a_unicode = buff3.decode('gb2312')
		except BaseException,e:
			a_unicode = buff3.decode('gbk')
		'''
		a_unicode = buff3.decode('gbk')
		buff3 = a_unicode.encode("UTF-8")
		f.close()
		return buff3
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
		except BaseException,e:
			print 'cvt error:',v,e
			os.system("pause")
			has_error=True
def rmfile(dir,end):
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
				flist.append(dir+filename)	
			#else:
				#print "file no csv"	
		#only walk top dir
		break		
	for v in flist:
		#print "ccvt ",v
		os.remove(v)
#'''
def rmdir(dir):
	if os.path.isdir(os.getcwd()+"/"+dir):
		print "remove ",dir
		os.system("rd /s /q "+dir)
		#os.rmdir(os.getcwd()+"/"+dir)
rmdir("out")		
os.mkdir(os.getcwd()+"/out/")
cvtdir(os.getcwd()+"/base/",'.csv')
if has_error:
	os.system("pause")
else:
	os.system("echo off")
	rmfile(os.getcwd()+"/",".csv")
	#time.sleep(1)
	os.system("XCOPY out\* .\ /S /R /E /Y")
	os.system("XCOPY base\*.json .\ /S /R /E /Y")
	os.system("XCOPY fortask\*.json .\ /S /R /E /Y")	
	rmdir("out")
	os.system("pause")
#'''