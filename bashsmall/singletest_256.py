from cmd import Cmd
import os
import math
import numpy as np
import random
import re
import pickle
import pandas as pd


flag = 'run'
#os.system("bash qsort.sh")
# App = ['bitcount','qsort','stringsearch','rijndael','sha','fft','susan','dijkstra']
App =  ['fft']
app = 'fft'
l1i_size = '32kB'
l1i_assoc = '2'
l1d_size = '64kB'
l1d_assoc = '2'
l2_size = '128kB'
l2_assoc = '8'
instruction_queue_entries = '32'
reorder_buffer_entries = '96'
issue_width = '4'
# i = random.randint(3,10)
# j = random.randint(i,i+2)
# k = random.randint(j,j+2)
# h = random.randint(k,k+2)
# i1 = random.randint(5,15)
# b = random.randint(5,15)
# # j1 = random.randint(i,i+2)
# # k1 = random.randint(j,j+2)
# # h1 = random.randint(k,k+2)
# tagTableTagWidths = '0 '+str(i)+' '+str(j)+' '+str(k)+' '+str(h)
# # tagTableTagWidths = '0 7 7 8 8'
# logTagTableSizes = str(b)+' '+str(i1)+' '+str(i1)+' '+str(i1)+' '+str(i1)
os.environ["APP"]=app
os.environ["L1ISIZE"]=l1i_size
os.environ["L1IASSOC"]=l1i_assoc
os.environ["L1DSIZE"]=l1d_size
os.environ["L1DASSOC"]=l1d_assoc
os.environ["L2SIZE"]=l2_size
os.environ["L2ASSOC"]=l2_assoc
# os.environ["BSIZE"]=branch_history_size
os.environ["IQSIZE"]=instruction_queue_entries
os.environ["ROBSIZE"] = reorder_buffer_entries
#os.environ["MSHR"] = misshr
os.environ["ISSUEWIDTH"] = issue_width
for time1 in range(5):
    b = random.randint(5,15)
    for time2 in range(6):
        i1 = random.randint(5,15)
        for time3 in range(5):
            i = random.randint(3,10)
            j = random.randint(i,i+2)
            k = random.randint(j,j+2)
            h = random.randint(k,k+2)
            tag = str(b)+'_'+str(i1)+'_'+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(h)+'_512'

    # j1 = random.randint(i,i+2)
    # k1 = random.randint(j,j+2)
    # h1 = random.randint(k,k+2)
            tagTableTagWidths = '0 '+str(i)+' '+str(j)+' '+str(k)+' '+str(h)
            # tagTableTagWidths = '0 7 7 8 8'
            logTagTableSizes = str(b)+' '+str(i1)+' '+str(i1)+' '+str(i1)+' '+str(i1)
            os.environ["BNUM"]=tag
            os.environ["TAGWIDTH"] = tagTableTagWidths
            os.environ["LOGSIZE"] = logTagTableSizes
            os.system("echo $APP $TAGWIDTH $LOGSIZE")
            cmd = 'bash '+app+'_256.sh'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            cmd = 'mv ~/gem5/gem5/path/out/'+app+'_'+str(tag)+'/stats.txt ~/gem5/gem5/bashsmall/m5out/Performance_result/tagenew/'+app+'_'+str(tag)+'.txt'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            cmd = 'mv ~/gem5/gem5/path/out/'+app+'_'+str(tag)+'/config.ini ~/gem5/gem5/bashsmall/m5out/Performance_config/tagenew/'+app+'_'+str(tag)+'.ini'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            cmd = 'mv ~/gem5/gem5/path/out/'+app+'_'+str(tag)+'/config.json ~/gem5/gem5/bashsmall/m5out/Performance_config/tagenew/'+app+'_'+str(tag)+'.json'
            print(cmd)
            if flag == 'run':
                os.system(cmd)

            







