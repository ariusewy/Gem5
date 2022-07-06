from cmd import Cmd
import os
import math
import numpy as np
import random
import re
import pickle
import pandas as pd

# file_dir = './m5out/Performance_result/'
# file_dir_list = os.listdir(file_dir)  
# indexstring = []

# for name in file_dir_list[:]:
#     indexolditem = name.split('fft_')[1].split('.txt')[0]
#     #print(indexitem)
#     indexstring.append(indexolditem)
# print(indexstring)
indexstring=[]

flag = 'run'
#os.system("bash qsort.sh")
# App = ['bitcount','qsort','stringsearch','rijndael','sha','fft','susan','dijkstra']
App =  ['fft']
l1i_size_area =  ['1kB','2kB', '4kB', '8kB', '16kB', '32kB','64kB']#7
l1i_assoc_area =['2','4','8','16','16','16','16']
#l1d_size_area = ['2kB', '4kB', '8kB', '16kB', '32kB', '64kB','128kB']
#l1d_assoc_area =['4','8','16','32','64','64','64']
cacheline_size = '64'
l2_size_area = ['4kB', '8kB', '16kB', '32kB', '64kB', '128kB','256kB']
l2_assoc = '8'
# bnum = 'small_'
branch_history_size_area=['512','1024','2048','4096','8192','16384']
#MSHR_area=[2,4.6,8,10]
issue_width_area = [2,4,6,8]
instruction_queue_entries_area = ['32','64']
# reorder_buffer_entries = '96'
reorder_buffer_entries_area = [16, 24, 32, 48, 64, 96, 128, 150]

i = random.randint(0,6)
d = random.randint(i,6)
l2 = random.randint(d,6)
ghr = random.randint(0,5)
#mshr = random.randint(0,5)
iss = random.randint(0,4)
iq = random.randint(0,1)
rob = random.randint(0,7)
for app in App:
    for time in range(100):
        i = random.randint(0,6)
        d = i
        l2 = random.randint(0,6)
        ghr = random.randint(0,5)
        #mshr = random.randint(0,5)
        iss = random.randint(0,3)
        iq = random.randint(0,1)
        rob = random.randint(0,7)
        bnum = str(i)+str(d)+str(l2)+str(ghr)+str(iss)+str(iq)+str(rob)
        if bnum in indexstring:
            pass
        else:
            indexstring.append(bnum)
            #indexitem = [i,d,l2,ghr,iss,iq,rob]
            #print(indexitem)
            #index.append(indexitem)
            l1i_size = l1i_size_area[i]
            l1i_assoc = l1i_assoc_area[i]
            l1d_size = l1i_size_area[i]
            l1d_assoc = l1i_assoc_area[i]
            l2_size = l2_size_area[l2]
            branch_history_size = branch_history_size_area[ghr]
            #misshr = MSHR_area[mshr]
            issue_width = str(issue_width_area[iss])
            instruction_queue_entries = instruction_queue_entries_area[iq]
            reorder_buffer_entries = str(reorder_buffer_entries_area[rob])
            #bnum = str(i)+str(d)+str(l2)+str(ghr)+str(iss)+str(iq)+str(rob)
            # indexstring.append(bnum)
            os.environ["APP"]=app
            os.environ["L1ISIZE"]=l1i_size
            os.environ["L1IASSOC"]=l1i_assoc
            os.environ["L1DSIZE"]=l1d_size
            os.environ["L1DASSOC"]=l1d_assoc
            os.environ["CACHELINE"]=cacheline_size
            os.environ["L2SIZE"]=l2_size
            os.environ["L2ASSOC"]=l2_assoc
            os.environ["BNUM"]=bnum
            os.environ["BSIZE"]=branch_history_size
            os.environ["IQSIZE"]=instruction_queue_entries
            os.environ["ROBSIZE"] = reorder_buffer_entries
            #os.environ["MSHR"] = misshr
            os.environ["ISSUEWIDTH"] = issue_width
            os.system("echo $APP $L1ISIZE $L1IASSOC $L1DSIZE $L1DASSOC $CACHELINE $L2SIZE $L2ASSOC $BNUM $BSIZE $ROBSIZE $IQSIZE $ISSUEWIDTH")
            print(indexstring)
            cmd = 'bash '+app+'_small.sh'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            cmd = 'bash mcpat.sh'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            cmd = 'mv ~/gem5/gem5/path/out/'+app+'_'+str(bnum)+'/mcpat.log'+ ' ~/gem5/gem5/bashsmall/mcpat_out/'+app+'_'+str(bnum)+'.log'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            cmd = 'mv ~/gem5/gem5/path/out/'+app+'_'+str(bnum)+'/stats.txt ~/gem5/gem5/bashsmall/m5out/Performance_result/DSE/'+app+'_'+str(bnum)+'.txt'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            cmd = 'mv ~/gem5/gem5/path/out/'+app+'_'+str(bnum)+'/config.ini ~/gem5/gem5/bashsmall/m5out/Performance_config/DSE/'+app+'_'+str(bnum)+'.ini'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            cmd = 'mv ~/gem5/gem5/path/out/'+app+'_'+str(bnum)+'/config.json ~/gem5/gem5/bashsmall/m5out/Performance_config/DSE/'+app+'_'+str(bnum)+'.json'
            print(cmd)
            if flag == 'run':
                os.system(cmd)
            # print(cmd)
            # if flag == 'run':
            #     os.system(cmd)
            # cmd = 'mv ../m5out/'+app+'_'+str(bnum)+'.ini' + ' ./m5out/Performance_config/'+app+'_'+str(bnum)+'.ini'
            # print(cmd)
            # if flag == 'run':
            #     os.system(cmd)
            # cmd = 'mcpat -infile ./m5out/Performance_result/'+app+'_'+str(bnum)+'.txt' + ' -print_level 2 > ' + app+'_'+str(bnum)+'.out'  
            # print(cmd)
            # if flag == 'run':
            #     os.system(cmd)
            







# for app in App:
#     os.environ["APP"]=app
#     os.system("echo $APP")
#     os.environ["L1ISIZE"]=l1i_size
#     os.environ["L1IASSOC"]=l1i_assoc
#    # os.environ["L1DSIZE"]=l1d_size
#    # os.environ["L1DASSOC"]=l1d_assoc
#     os.environ["CACHELINE"]=cacheline_size
#     os.environ["L2SIZE"]=l2_size
#     os.environ["L2ASSOC"]=l2_assoc
#     os.environ["BNUM"]=bnum
#     os.environ["BSIZE"]=branch_history_size
#     os.environ["IQSIZE"]=instruction_queue_entries
#     os.environ["ROBSIZE"] = reorder_buffer_entries
#     for i in range(7):
#         os.environ["L1DSIZE"]=l1d_size_area[i]
#         os.environ["L1DASSOC"]=l1d_assoc_area[i]
#         os.system("echo $L1ISIZE $L1IASSOC $L1DSIZE $L1DASSOC $CACHELINE $L2SIZE $L2ASSOC $BNUM $BSIZE $ROBSIZE $IQSIZE")
#         cmd = 'bash '+app+'_small.sh'
#         print(cmd)
#         if flag == 'run':
#             os.system(cmd)
#         cmd = 'mv ../m5out/'+app+'_'+str(bnum)+'.txt' + ' ../m5out/Performance_result/FC_'+app+'_'+str(bnum)+l1d_size_area[i]+'.txt'
#         print(cmd)
#         if flag == 'run':
#             os.system(cmd)
#         cmd = 'mv ../m5out/'+app+'_'+str(bnum)+'.ini' + ' ../m5out/Performance_config/FC_'+app+'_'+str(bnum)+l1d_size_area[i]+'.ini'
#         print(cmd)
#         if flag == 'run':
#             os.system(cmd)



    # for rob in reorder_buffer_entries_area:
    #     os.environ["ROBSIZE"]=str(rob)
    #     os.system("echo $L1ISIZE $L1IASSOC $L1DSIZE $L1DASSOC $CACHELINE $L2SIZE $L2ASSOC $BNUM $BSIZE $ROBSIZE $IQSIZE")
    #     cmd = 'bash '+app+'_small.sh'
    #     print(cmd)
    #     os.system(cmd)
    #     cmd = 'mv ../m5out/'+app+'_'+str(bnum)+'.txt' + ' ../m5out/Performance_result/FC_'+app+'_'+str(bnum)+str(rob)+'.txt'
    #     print(cmd)
    #     os.system(cmd)
    #     cmd = 'mv ../m5out/'+app+'_'+str(bnum)+'.ini' + ' ../m5out/Performance_config/FC_'+app+'_'+str(bnum)+str(rob)+'.ini'
    #     print(cmd)
    #     os.system(cmd)
# def branch(limit):
#     branch_history_size = []
#     i = 3
#     while i < limit:
#         branch_history_size.append(pow(2,i))
#         i = i + 1
#     return branch_history_size

# branch_history_size = branch(32)
# print(branch_history_size)
# table = 3
# for x in branch_history_size:
#     os.environ["BSIZE"]=str(x)
#     os.environ["BNUM"]=str(table)
#     os.system("echo $BSIZE")
#     os.system("echo $BNUM")
#     cmd = 'bash '+App+'.sh'
#     print(cmd)
#     os.system(cmd)
#     cmd = 'mv m5out/'+App+'_'+str(table)+'.txt' + ' m5out/'+App+'/result/'
#     print(cmd)
#     os.system(cmd)
#     cmd = 'mv m5out/'+App+'_'+str(table)+'.ini' + ' m5out/'+App+'/config/'
#     print(cmd)
#     os.system(cmd)
#     table = table + 1






# path = 'build/RISCV/gem5.opt '
# filename = 'configs/example/se.py '
# respath = './result/'


# APP = 'qsort'
# history_size = 1
# outconfig = '--stats-file='+ APP + str(history_size)+'.txt'
# dumpconfig = '--dump-config='+ APP + str(history_size)+'.ini'

# def clk():
#     clk = '--clk='
#     clk_area = ['0.5GHz','1GHz','2GHz','3GHz']
#     for x in clk_area:
#         cmd = path + filename + clk + str(x)
#         os.system(cmd)
#         res = respath + "Clk_" + str(x) + ".txt"
#         cmd = "cp m5out/stats.txt " + res
#         os.system(cmd)

# def L1I():
#     l1i_size = '--l1i_size='
#     l1i_size_area = ['2kB', '4kB', '8kB', '16kB', '32kB', '64kB']
#     for x in l1i_size_area:
#         cmd = path + filename + l1i_size + str(x)
#         os.system(cmd)
#         res = respath + "L1I_"+ str(x) + ".txt"
#         cmd = "cp m5out/stats.txt " + res
#         os.system(cmd)

# def L1D():
#     l1d_size = '--l1d_size='
#     l1d_size_area = ['2kB', '4kB', '8kB', '16kB', '32kB', '64kB', '128kB', '256kB']
#     for x in l1d_size_area:
#         cmd = path + filename + l1d_size + str(x)
#         os.system(cmd)
#         res = respath + "L1D_"+ x + ".txt"
#         cmd = "cp m5out/stats.txt " + res
#         os.system(cmd)

# def L2():
#     l2_size = '--l2_size='
#     l2_size_area = ['128kB', '256kB', '512kB', '1024kB', '2048kB', '4096kB']
#     for x in l2_size_area:
#         cmd = path + filename + l2_size + str(x)
#         os.system(cmd)
#         res = respath + "L2_"+ str(x) + ".txt"
#         cmd = "cp m5out/stats.txt " + res
#         os.system(cmd)

# def cache_block():
#     cache_block = '--cache_block='
#     cache_block_area = [8, 16, 32, 64, 128, 256]
#     for x in cache_block_area:
#         cmd = path + filename + cache_block + str(x)
#         os.system(cmd)
#         res = respath + "cache_block_"+ str(x) + "B.txt"
#         cmd = "cp m5out/stats.txt " + res
#         os.system(cmd)

# def main():
#     clk()
#     L1I()
#     L1D()
#     L2()
#     cache_block()

# if __name__ == '__main__':
#     main()