int(input())
l = list(map(int, input().split()))
answer = 1
for i in l:
    answer = (answer * i) % (10**9+7)
print(answer)
