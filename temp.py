# Calculator
# \sum_{i=0}^8C_8^i(\frac14)^i(\frac34)^{(8-i)}(\frac{8-i}4+i)

import math

def funcA(bot,top):
    times=1
    for i in range(top-bot+1,top+1):
        times*=i
    return times

def funcC(bot,top):
    return funcA(bot,top)/funcA(top,top)

def mypow(bot,top):
    times=1
    for i in range(1,top+1):
        times*=bot
    return times

sum=0
for i in range(0,8+1):
    sum+=math.comb(8,i)*pow(0.25,i)*pow(0.75,8-i)*((8-i)/4+i)
    print(math.comb(8,i))
print(sum)