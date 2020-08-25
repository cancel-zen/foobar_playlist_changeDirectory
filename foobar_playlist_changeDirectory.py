# -*- coding: utf-8 -*-



import os
path='d:\\1'
filelist=os.listdir(path)
print(filelist)

for playlist in filelist:
    file_data = ""
    with open(path+'\\'+playlist,'r',encoding="utf-8") as f:
        for line in f.readlines():
            if line[0]=='G':
                line=line.replace(line[0],"F")
            file_data += line
            
    with open(path+'\\'+playlist,'w',encoding="utf-8") as f:
        f.write(file_data)