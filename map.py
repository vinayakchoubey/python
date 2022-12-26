def square(n):
    return n**2
L=[2,4,6,8,10,12,14,16,18,20]
result=map(square,L)
SL=list(result)
print(SL)



M=[1,3,5,7,9,11,13,15,17,19]
result=map(lambda x:x**2,M)
SM=list(result)
print(SM)


T1=(1,3,5,7,9)
T2=(2,4,6,8,10)
result=map(lambda x,y:x+y,T1,T2)
L=list(result)
print(L)