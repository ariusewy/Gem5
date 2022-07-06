from cmd import Cmd
import os
import math

#os.system("bash qsort.sh")
# App = ['bitcount','qsort','stringsearch','rijndael','sha','fft','susan','dijkstra']
App = ['fft']
l1i_size = '16kB'
l1i_assoc = '256'
l1d_size = '32kB'
l1d_assoc = '512'
cacheline_size = '64'
l2_size = '128kB'
l2_assoc = '8'
bnum = 'small'
branch_history_size = '4096'
# totally matched SEU's master paper 2022.05.08 
for app in App:
    os.environ["APP"]=app
    os.system("echo $APP")
    os.environ["L1ISIZE"]=l1i_size
    os.environ["L1IASSOC"]=l1i_assoc
    os.environ["L1DSIZE"]=l1d_size
    os.environ["L1DASSOC"]=l1d_assoc
    os.environ["CACHELINE"]=cacheline_size
    os.environ["L2SIZE"]=l2_size
    os.environ["L2ASSOC"]=l2_assoc
    os.environ["BNUM"]=bnum
    os.environ["BSIZE"]=branch_history_size
    os.system("echo $L1ISIZE $L1IASSOC $L1DSIZE $L1DASSOC $CACHELINE $L2SIZE $L2ASSOC $BNUM $BSIZE")
    cmd = 'bash '+app+'.sh'
    print(cmd)
    os.system(cmd)
    cmd = 'mv m5out/'+app+'_'+str(bnum)+'.txt' + ' m5out/Performance_result/'
    print(cmd)
    os.system(cmd)
    cmd = 'mv m5out/'+app+'_'+str(bnum)+'.ini' + ' m5out/Performance_config/'
    print(cmd)
    os.system(cmd)
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