#!/usr/bin/python
# -*- coding: UTF-8 -*-
#compare dir file diff
import os
import sys,re
import string
import codecs
import shutil
import time
import subprocess
from hashlib import md5
#print "sys.arg ",len(sys.argv)
def md5_file(name):
    m = md5()
    a_file = open(name, 'rb')    #需要使用二进制格式读取文件内容
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()

def is_cmp(infile,end):
	return re.match(".+"+end+"$",infile)

def copy_dir(src,dst):
	cmd = "XCOPY "+src + "\*	"+ dst +" /S /R /E /Y"
	print cmd
	os.system(cmd)

def cmp_file_md5(src,dst):
	rm = False
	if os.path.isfile(src) and os.path.isfile(dst):
		if md5_file(src)==md5_file(dst):
			rm = True
	if rm:
		os.remove(dst)		
		return True
	return False

def list_file(srcdir):
	alldir=[]
	allfile=[]
	plen=len(srcdir)
	for parent,dirnames,filenames in os.walk(srcdir):
		for dirname in dirnames:
			srcpath = os.path.join(parent,dirname)
			alldir.append(srcpath[plen+1:len(srcpath)])
		for filename in filenames:
			srcpath = os.path.join(parent,filename)
			tp=(srcpath[plen+1:len(srcpath)],md5_file(srcpath),int(os.path.getsize(srcpath)))
			allfile.append(tp)
			#print(srcpath)
			#print(dstpath)
	#print("dirs: ",alldir)
	#print("file: ",allfile)
	return alldir,allfile

def filter_file(srcdir,endlist):
	for parent,dirnames,filenames in os.walk(srcdir):
		for filename in filenames:
			srcpath = parent+"/"+filename
			for end in endlist:
				if re.match(".+"+end+"$",srcpath):
					os.remove(srcpath)

def rm_dir(dir):
	if os.path.isdir(dir):
		print "remove ",dir
		os.system("rd /s /q "+dir)
def rm_file(f):
	if os.path.isfile(f):
		os.remove(f)

def stringlize(dirlist,filelist):
	buf = "--dirct=" + str(len(dirlist)) + "\n"
	buf = buf + "--filect=" + str(len(filelist)) + "\n"
	buf = buf + "local list = {\n" 
	buf = buf + "\tappdir = \"" + (appdir) + "\",\n"
	buf = buf + "\tappname = \"" + (appname) + "\",\n"
	buf = buf + "\tappver = \"" + (appver) + "\",\n" 
	buf = buf + "\tresver = \"" + (resver) + "\",\n" 
	buf = buf + "\tresvercode = " + str(resvercode) + ",\n" 
	buf = buf + "\tdirs = {\n"
	for dname in dirlist:
		item="\t\t\"%s\",\n"%(dname)
		buf=buf+item
	buf = buf+"\t},\n"

	buf = buf+"\tfiles = {\n"
	for tp in filelist:
		nm = tp[0]
		md = tp[1]
		sz = tp[2]
		item="\t\t{\"%s\",\"%s\",%d},\n"%(nm,md,sz)
		buf = buf+item
	buf = buf+"\t},\n" 
	buf = buf+"}\n\n" 
	buf = buf+"return list"
	buf=re.sub(r'\\',r'/',buf)
	return buf
	
def run():
	global appdir
	global appname
	global appver
	global resver
	global resvercode
	appdir="A"
	appname="A game"
	appver="1.0"
	resver="1.13"
	resvercode=113
	os.system("echo off")
	if len(sys.argv)<2:
		print "please input dir"
		return
	srcdir = os.getcwd()+"/"+sys.argv[1]
	filter_file(srcdir,['.db','.svn','.git'])	
	dirlist,filelist = list_file(srcdir)
	buff = stringlize(dirlist,filelist)
	print buff
	outfile = os.getcwd()+"/"+"list.txt"
	fd = open(outfile,'wb+')
	fd.write(buff)
	fd.close()
	os.system("7z.exe a -tzip -r list.zip " + outfile)
	
run()
#py cmp.py A B
#'''