from multiprocessing import Process
import os
import time,random
# 子进程要执行的代码



def run_proc(name,t):
    print('Child process %s (%s) run....' % (name, os.getpid()))
    time.sleep(t)
    print('Child process %s (%s) stop....' % (name, os.getpid()))
    return True

if __name__=='__main__':
    dt_list = []
    for i in range(100):
        dt_list.append(['test%d' % i, random.random() * 10])
    print(dt_list[:5])
    print('Parent process %s.' % os.getpid())

    n = 0
    proc_list=[]
    while dt_list.__len__()>0:
        while proc_list.__len__()<10 and dt_list.__len__()>0:
            t=dt_list.pop(0)
            p = Process(target=run_proc, args=(t[0],t[1],))
            p.start()
            proc_list.append(p)
            #for x in range(proc_list):
            #    print(x)
            #p.join()
            #time.sleep(3)
            #print(p)
        #每隔三秒判定一次进程是否完成
        time.sleep(3)
        for i in range(len(proc_list),0,-1):
            print(proc_list[i-1])
            if not proc_list[i-1].is_alive():
                proc_list.pop(i-1)