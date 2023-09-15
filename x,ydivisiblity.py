t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    ans = []
    for a in range(1,10**18):
        if (a+x)%y==0 and (a+y)%x == 0 :
            ans.append(a)
    print(ans[0])       