l = []
for i in range(int(input())):
    s = input()
    l.append(s)
    c = 0
    for j in l:
        if j < s:
            c += 1
    print(c)
