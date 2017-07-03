s = input().strip()
t = input().strip()

count = 0
for i in range(len(s) - len(t) + 1):
    if s.startswith(t, i):
        count += 1
print(count)
