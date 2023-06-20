from random import randint
from typing import List,Tuple
import json

cases = Tuple[int,int,List[int]]

# 预定义
nm=['万能','火','水','雷','冰','岩','风','草']


# function
# input
def myInput() -> cases:
    nd=[0]
    n=eval(input('总骰子数：'))
    print('接下来输入需要的骰子数：')
    for i in range(1,7+1):
        nm_ipt=eval(input(f'{nm[i]}:'))
        nd.append(nm_ipt)
    t=eval(input('投掷次数:'))
    ipt=(n,nd,t)
    return ipt

# 通用function
def throw(num:int) -> List:
    tznm=[0,0,0,0,0,0,0,0]
    for i in range(1,num+1):
        rd=randint(0,7)
        tznm[rd]+=1
    return tznm

# 统计学求解
def statisticFun(case:cases) -> None:
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            fre=json.load(file)['frequency']
    except:
        fre=10000
    sum_gap=0
    tianshouge=0
    for f in range(1,fre+1):
        num,need,times=case
        all_tznm=[0,0,0,0,0,0,0,0]
        tznm=[0,0,0,0,0,0,0,0]
        for t in range(1,times+1):
            tmp_tznm=throw(num)
            num=max(0,num-tmp_tznm[0])
            tznm[0]+=tmp_tznm[0]
            for i in range(1,7+1):
                if tznm[i]+tmp_tznm[i]<=need[i]:
                    tznm[i]+=tmp_tznm[i]
                    num=max(0,num-tmp_tznm[i])
                elif tznm[i]<need[i]:
                    num=max(0,num-(need[i]-tznm[i]))
                    tznm[i]=need[i]
            # 天守阁专用
            if t<times:
                all_tznm=tznm
            else:
                for i in range(0,7+1):
                    all_tznm[i]+=tmp_tznm[i]
            if(num==0):
                break
        sum_need=0
        sum_good=0
        for i in range(0,7+1):
            sum_need+=need[i]
            sum_good+=tznm[i]
        gap=max(0,sum_need-sum_good)
        sum_gap+=gap
        # 天守阁
        num_DiceType=all_tznm[0]
        for i in range(1,7+1):
            num_DiceType+=(all_tznm[i]>0)
        if num_DiceType>=5:
            tianshouge+=1
    avg_gap=sum_gap/fre
    print(f'烧牌数期望:{avg_gap}')
    print(f"天守阁触发:{tianshouge/fre}")
    return





# 解析求解
def singPiece():
    
    return 


def singTime(n:int,nd:List,t:int) -> None:

    return

while True:
    statisticFun(myInput())