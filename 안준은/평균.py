number=int(input())

score=list(map(int, input().split()))

score.sort(reverse=True)

high=score[0]

grades=[]
for a in score:
    grades.append(a/high*100)
sum=sum(grades)

result=sum/number

print(result)
