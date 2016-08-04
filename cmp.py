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
has_error=False
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

def cmp_file(srcdir,dstdir):
	prefix = srcdir
	plen = len(srcdir)
	allfile = 0
	rmfile = 0
	for parent,dirnames,filenames in os.walk(srcdir):
		for filename in filenames:
			srcpath = parent+"\\"+filename
			dstpath = dstdir+srcpath[plen:len(srcpath)]
			#print(srcpath)
			#print(dstpath)
			allfile=allfile+1
			if cmp_file_md5(srcpath,dstpath):
				rmfile=rmfile+1
	print("srcfile: ",allfile)
	print("samfile: ",rmfile)
	allfile=0
	for parent,dirnames,filenames in os.walk(dstdir):
		for filename in filenames:
			allfile=allfile+1
	print("outfile: ",allfile)	
	return allfile

def filter_file(srcdir,endlist):
	for parent,dirnames,filenames in os.walk(srcdir):
		for filename in filenames:
			srcpath = parent+"\\"+filename
			for end in endlist:
				if re.match(".+"+end+"$",srcpath):
					os.remove(srcpath)

def rm_dir(dir):
	if os.path.isdir(dir):
		print "remove ",dir
		os.system("rd /s /q "+dir)
	
def run():
	os.system("echo off")
	if len(sys.argv)<3:
		print "please input a,b dir"
		return
	srcdir = os.getcwd()+"\\"+sys.argv[1]
	dstdir = os.getcwd()+"\\"+sys.argv[2]
	outdir = os.getcwd()+"\\"+sys.argv[2]+"out"
	rm_dir(outdir)
	os.mkdir(outdir)
	copy_dir(dstdir,outdir)
	filter_file(outdir,['.db','.svn','.git'])
	diffs = cmp_file(srcdir,outdir)
	if diffs>0:
		print "zip diff"
		os.system("7z.exe a -tzip -r diff.zip " + outdir +"\*.*")
		os.system("7z.exe l diff.zip")
		print "zip diff File : diff.zip"
		return "diff.zip"
	else:
		print "no diff File"	


#run()
#py cmp.py A B
#'''