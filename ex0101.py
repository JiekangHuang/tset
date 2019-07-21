def fac(n,a):
    sum = 0
    if n==a:
        return n
    else:
        sum =  n + fac(n+1,a)
        print("n = {},a = {},sum = {}".format(n,a,sum))
        return sum

print(fac(1,10))