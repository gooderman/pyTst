import os
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
#set res dir
resdir='Resources'
resdst='Resources_out'
os.system('cd ' + os.getcwd())
os.system('rd '+ resdst + ' /S /Q')
os.system('xcopy ' + resdir + '\\* ' + resdst + '\\ /S /R /E /Y')
def isFileNeedEncytp(fileName):
    if fileName.find('TileMap') > -1 :
        print 'filter '+fileName
        return False
    if os.path.isdir(fileName):
        return True		
    if fileName.find('.png') > -1 :
        return True
    return False

def folderEncytp(folderPath):
	#print folderPath
	if isFileNeedEncytp(folderPath):
		for file in os.listdir(folderPath):
			if os.path.isdir(folderPath + file + '\\'):
				folderEncytp(folderPath + file + '\\')
			else:
				if isFileNeedEncytp(file):
					fileName = folderPath + file
					print 'compress '+ fileName
					os.system(os.getcwd()+'\\pngquant -f --ext .png --quality 50-80 ' + '\"' + fileName + '\"')
		return
folderEncytp(os.getcwd() + '\\'+resdst+'\\')

os.system("pause")
