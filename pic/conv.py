import os,sys

list = os.listdir('/Users/duli/Programme/zhilian_ocr/pic')

print(list)

for i in range(0,100):
    cmd = ''
    cmd = 'convert '+ list[i] +  ' %d'%i + '.tif'
    os.system(cmd)