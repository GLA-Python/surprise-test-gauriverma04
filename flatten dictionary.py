def check(g):
    for i in range(len(g)):
        a= g[i]-g[i-1]
        b = g[i-1]-g[i-2]
        if a**2 > b**2:
            x = True
        else:
            x = False
    return x
j = list(map(int, input().split()))
k = check(j)
print(k)
