for i in range(int(input())):
    a, b = map(int, input().split())
    l = list(map(int, input().split()))
    print(*l[len(l)-b%(len(l)):], *l[:len(l)-b%len(l)])
    print()
