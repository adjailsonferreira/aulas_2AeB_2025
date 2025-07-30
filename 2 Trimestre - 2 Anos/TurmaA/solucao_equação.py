import random as r
import time as t
x=1
y=10001
tentativas = 0
while True:
    x=x+1#r.randint(2,10000)
    y=y-1#r.randint(2,10000)
    try:
        E1 = ((x/y)/(x*y))**2
        E2 = ((x*y)/(x**2))**2
        if E1>E2:
            print('E1 é maior que E2.',E1)
        elif E1==E2:
            print(f'E1={E1}, E2={E2}')
            print(f'x={x}, y={y}')
            break
        else:
            print('E2 é maior que E1.',E2)
        tentativas+=1
        
    except:
        continue
    t.sleep(1)
print('Número de tentativas=',tentativas)


