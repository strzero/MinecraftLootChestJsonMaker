import os
import re
filedir =os.getcwd()
filenames=os.listdir(filedir)
f=open('result.json','w')
doc=open('structureList.txt','w')
f.writelines('{\n')
first=True
for filename in filenames:
    if re.search('json', filename):
        filepath = filedir+'/'+filename
        struname = re.sub(r'\..*$', "", filename)
        doc.writelines(struname+'\n')
        if first is False :
            f.writelines(',\n')
        else:
            first= False
        f.writelines('"'+struname+'": ')
        for line in open(filepath):
            f.writelines(line)

filedir =os.getcwd()+'/village'
filenames=os.listdir(filedir)
for filename in filenames:
    if re.search('json', filename):
        filepath = filedir+'/'+filename
        struname = re.sub(r'\..*$', "", filename)
        doc.writelines(struname+'\n')
        f.writelines(',\n')
        f.writelines('"'+struname+'": ')
        for line in open(filepath):
            f.writelines(line)

f.writelines('\n}')
f.close()
