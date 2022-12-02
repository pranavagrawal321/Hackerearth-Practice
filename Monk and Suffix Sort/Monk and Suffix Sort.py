a, b = input().split()
b = int(b)
ans = []
for i in range(len(a)):
    ans.append(a[-i:])
print(sorted(ans)[b-1])
