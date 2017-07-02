result = 'No'


def isSubclass(ancestor, heir):
    global result
    if ancestor == heir:
        result = 'Yes'
    if heir in classes_map:
        for c in classes_map[heir]:
            if ancestor == c:
                result = 'Yes'
            else:
                if result == 'No':
                    result = isSubclass(ancestor, c)
    return result


n = int(input())
classes_map = {}
for i in range(n):
    rawClasses = input()
    if ':' in rawClasses:
        classes = [c.strip() for c in rawClasses.split(':')]
    else:
        classes = rawClasses.strip()

    if len(classes) > 1:
        subclasses = [c.strip() for c in classes[1].split()]
    else:
        subclasses = []

    if classes[0] in classes_map:
        classes_map[classes[0]].extend(subclasses)
    else:
        classes_map[classes[0]] = subclasses

q = int(input())
for i in range(q):
    classes = [c for c in input().split()]
    ancestor = classes[0]
    heir = classes[1]
    print(isSubclass(ancestor, heir))
    result = 'No'
