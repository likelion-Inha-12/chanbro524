import math
def geun(a,b,c):
    d=b**2-4*a*c
    if d>0:
        print(-b+d**(0.5)/2*a)
        print(-b-d**(0.5)/2*a)
    elif d==0:
        print("중근을 갖습니다")
        print(-b/2*a)
    else:
        print("근이 존재하지 않습니다")
geun(1,2,1)