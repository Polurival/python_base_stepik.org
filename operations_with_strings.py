s = input()
a = input()
b = input()

if a in b and a in s:
    print('Impossible')
else:
    i = 0
    while True:
        old = s
        s = s.replace(a, b)
        if old != s:
            i += 1
        else:
            print(i)
            break
