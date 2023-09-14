
s=[]
number=0
for _ in range(10):
    x=int(input())
    s.append(x%42)

for i in s:
    cnt=s.count(i)
    if cnt==1:
        number+=1

print(number)
