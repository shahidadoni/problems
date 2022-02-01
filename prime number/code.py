t=int(input())

for i in range(t):
    count=0
    n = int(input())
    for j in range(2,n):
        if n%j == 0:
            count+=1
            break
    if count==0:
        print("prime")
    else:
        print("not prime")