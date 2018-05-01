import os,sys

list = os.listdir('/Users/duli/Programme/zhilian_ocr/pic')


for i in range(0,74):
    cmd = ''
    cmd = 'convert '+ list[i] +  ' %d'%i + '.tif'
    os.system(cmd)