def isAncestor(ancestor, heir):
    if heir in exceptions_map and ancestor in exceptions_map[heir]:
        if heir not in answers:
            answers.append(heir)
    else:
        if heir in exceptions_map:
            for anc in exceptions_map[heir]:
                isAncestor(anc, heir)


n = int(input())
exceptions_map = {}
for i in range(n):
    rawExceptions = input()
    if ':' in rawExceptions:
        exceptions = [c.strip() for c in rawExceptions.split(':')]
    else:
        exceptions = rawExceptions.strip()

    if len(exceptions) > 1:
        ancestors = [c.strip() for c in exceptions[1].split()]
    else:
        ancestors = []

    if exceptions[0] in exceptions_map:
        exceptions_map[exceptions[0]].extend(ancestors)
    else:
        exceptions_map[exceptions[0]] = ancestors

m = int(input())
exp_list = []
answers = []
for i in range(m):
    exp = input()
    if exp not in exp_list:
        exp_list.append(exp)
for i in range(len(exp_list)):
    if i == 0:
        continue
    else:
        for j in range(0, i):
            ancestor = exp_list[j]
            heir = exp_list[i]
            isAncestor(ancestor, heir)

for excess in answers:
    print(excess)
