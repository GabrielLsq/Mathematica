"""
for循环100求和

sum=0
for i in range(101):
    sum+=i
print("1-100的和为%d+%d"%(sum,i))

偶数和
sum=0
for i in range(101):
    if i%2==0:
        sum+=i
print("1-100的偶数和为%d，1-100的奇数和为%d"%(sum,5050-sum))

猜数

import random

ans=random.randint(1,100)
count=0
while True:
    count+=1
    number=int(input('enter an integer:'))
    if number<ans:
        print('小了')
    elif number>ans:
        print('大了')
    else:
        print('Right')
        break

print('你总共猜了%d次'%count)

if count>7:
    print('放弃吧')

乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

判断素数


from math import sqrt

num=int(input('输入一个整数:'))
end=int(sqrt(num))

is_Prime=True
for i in range(2,end+1):
    if num%i==0:
        is_Prime=False
        break

if is_Prime and num!=1:
    print("%d是素数" %num)

else:
    print("%d不是素数"%num)
    for i in range(2,end+1):
        if num%i==0:
            print(i)

水仙花数

for num in range(100,1000):
    a=int(num/100)
    b=int((num-100*a)/10)
    c=(num-100*a-10*b)

    if a**3+b**3+c**3==num:
        print('%d^3+%d^3+%d^3=%d'%(a,b,c,num),end='\t')

for i in range(0,21):
    for j in range(0,34):
        for k in range(0,334):
            if 5*i+3*j+k*(1/3)==100 and i+j+k==100:
                print(i,j,k)
 
完美数

from math import sqrt
import numpy as npy
from operator import mul
arr=[]
num=int(input('输入一个正整数：'))
for i in range(1,num):
    if num%i==0:
        arr.append(i)

result=1
for i in range(1,len(arr)):
    result=result*arr[i]

if(num==npy.sum(arr)):
    print("%d是完美数"%num,arr)
else:
    print("%d不是完美数"%num,arr)

完全平方数之和

import numpy as npy
from math import sqrt



num=0
for i in range(101):
    if int(sqrt(i))==sqrt(i):
        num+=i
        print(i)

print(num)

有物不知数

for i in range(1000):
    if i%3==2 and i%5==3 and i%7==2:
        print(i)


import random
import numpy as npy
arr=[]
for i in range(100):
    a=random.randint(1,10)
    arr.append(a)
    

b=npy.sum(arr)
c=b/100
print(arr)
print(b)
"""

def  factorial(num):
    result=1
    for n in range(1,num+1):
        result*=n
    return result

m=4
n=5
print(factorial(m),factorial(n))