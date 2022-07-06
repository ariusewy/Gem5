import os
import sys
import re
import pickle
import pandas as pd
 
 
file_dir = './m5out/Performance_result/tage'
file_dir_list = os.listdir(file_dir) 
file_dir_list.sort(key=lambda x:int(x.split('fft_')[1].split('.txt')[0])) 
file_list = {}
file_name_list=[]
get_result = []


for name in file_dir_list[:]:
    file_name = os.path.join(file_dir,name)  
    file_name_list.append(name)
    file_list[name] = []
# f.close()

print(file_name_list)
 
#print(file_list)
missrate = []
cpi = []
findex=open("index2.txt","w")
for name in file_name_list:
    file_name = os.path.join(file_dir,name)
    with open(file_name, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            a = line.split()
            if a !=[] and a[0] == 'system.cpu.branchPred.condPredicted':
                #print(a[0]+':'+a[1])
                file_list[name].append(int(a[1]))
            if a !=[] and a[0] == 'system.cpu.branchPred.condIncorrect':
                #print(a[0]+':'+a[1])
                file_list[name].append(int(a[1]))
            if a !=[] and a[0] == 'system.cpu.cpi':
                # print(a[0]+':'+a[1])
                file_list[name].append(float(a[1]))
    if file_list[name]!=[]:
        # print(name)
        # print(file_list[name])
        miss = float(file_list[name][2])
        total = float(file_list[name][1])
        missrate.append(miss/total)
        cpi.append(file_list[name][0])
    
    indexstring = name.split('fft_')[1].split('.txt')[0]
    temp = re.findall(".{1}",indexstring)
    index = " ".join(temp)
    file_list[name].append(index)
    findex.write(index+'\n')

findex.close()

for name in file_name_list:
    item = [name,file_list[name][3],float(file_list[name][2])/float(file_list[name][1]),file_list[name][0]]
    get_result.append(item)

print(missrate)
print(cpi)
#     strs = re.sub('[^\w]', '', data)   #[^\w]
 
#     #print(strs)
#     #print(file_name)
#     wordlist = []   
#     word = ''
#     #print(anls.extract_tags(strs, topK=5, withWeight=True))
#     keywords = anls.extract_tags(strs, topK=5, withWeight=True)
#     for keyword in keywords:
#         wordlist.append(keyword[0])
#     print(wordlist)
#     for w in wordlist:
#         word += w + ', '
#     print(word)
#     get_result.append([name, word])
# print(get_result)
 
namenew = ['name','index','missrate','cpi']
contents = pd.DataFrame(columns=namenew, data=get_result)
contents.to_csv('tagenew.csv')