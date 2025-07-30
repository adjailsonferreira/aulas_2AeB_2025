a=int(input())
b=int(input())
c=int(input())
delta = b**2-4*a*c
if delta > 0:
    x1=(-b+delta**(1/2)) / (2*a)
    x2=(-b-delta**0.5) / (2*a)
elif delta == 0:
    pass
else:pass   
print("x'=",x1,'x"=',x2)