from random import randint
from typing import List,Tuple

def need_decide(tznm,need): # 根据需求留骰子，不留多 
    for i in range(1,7+1):
        tznm[i]=min(tznm[i],need[i])
    return tznm

def tianshouge_judge(tznm)->int:
    a=tznm[0]
    for i in range(1,7+1):
        if tznm[i]>0:
            a+=1
    if a>5:
        return 1
    return 0

def throw(num:int) -> List:
    tznm=[0,0,0,0,0,0,0,0]
    for i in range(1,num+1):
        rd=randint(0,7)
        tznm[rd]+=1
    return tznm

def num_gap(num_dive,tznm): # 计算重投数量
    for i in range(0,7+1):
        num_dive-=tznm[i]
    return num_dive

def merge_tznm(tznma,tznmb): # 合并骰子
    tznm=[0,0,0,0,0,0,0,0]
    for i in range(0,7+1):
        tznm[i]=tznma[i]+tznmb[i]
    return tznm

num_dive=8
fre=10000
times=2
tznm=[0,0,0,0,0,0,0,0]
need=[0,0,8,8,0,0,0,0]
ext_dive=[0,0,0,0,0,0,0,1]

goal=0
for f in range(1,fre+1):
    tznm=[0,0,0,0,0,0,0,0]
    for i in range(1,times):
        tznm=merge_tznm(tznm,throw(num_gap(num_dive,tznm)))
        tznm=need_decide(tznm,need)
    tznm=merge_tznm(tznm,throw(num_gap(num_dive,tznm)))
    tznm=merge_tznm(tznm,ext_dive)
    goal+=tianshouge_judge(tznm)
print(goal/fre)

