a, b, n = map(int, input().split())
x = min(b-1, n)
ans = int((a*x)/b) - a*int(x/b)
print(ans)
