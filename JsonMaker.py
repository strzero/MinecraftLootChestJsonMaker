import os
import re
filedir =os.getcwd()
filenames=os.listdir(filedir)
f=open('results.json','w')
f.writelines('{\n')
first=True
for filename in filenames:
    if re.search('json', filename):
        filepath = filedir+'/'+filename
        if first is False :
            f.writelines(',\n')
        else:
            first= False
        f.writelines('"'+re.sub(r'\..*$', "", filename)+'": ')
        for line in open(filepath):
            f.writelines(line)

filedir =os.getcwd()+'/village'
filenames=os.listdir(filedir)
for filename in filenames:
    if re.search('json', filename):
        filepath = filedir+'/'+filename
        f.writelines(',\n')
        f.writelines('"'+re.sub(r'\..*$', "", filename)+'": ')
        for line in open(filepath):
            f.writelines(line)

f.writelines('\n}')
f.close()
