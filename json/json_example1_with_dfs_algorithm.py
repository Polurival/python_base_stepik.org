import json
'''
3.5
Вам дано описание наследования классов в формате JSON. 
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. 
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, 
которое содержит список имен прямых предков.
Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
'''


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        if next in graph:
            dfs(graph, next, visited)
        else:
            visited.add(next)
    return visited

# [{"name": "G", "parents": ["F"]},{"name": "A", "parents": []},{"name": "B", "parents": ["A"]},{"name": "C", "parents": ["A"]},{"name": "D", "parents": ["B", "C"]},{"name": "E", "parents": ["D"]},{"name": "F", "parents": ["D"]},{"name": "X", "parents": []},{"name": "Y", "parents": ["X", "A"]},{"name": "Z", "parents": ["X"]},{"name": "V", "parents": ["Z", "Y"]},{"name": "W", "parents": ["V"]}]
# [{"name": "kvrwxkmqfy", "parents": ["zemrehxvuo", "qzntzflodp", "pjvisgmdrw"]}, {"name": "ogqoyccgkn", "parents": ["ppcmlxqgmn", "titthqeskb"]}, {"name": "uhfdrfrhzx", "parents": ["ogqoyccgkn", "ppcmlxqgmn", "wubwjzolrx", "pjvisgmdrw", "titthqeskb"]}, {"name": "zemrehxvuo", "parents": ["uhfdrfrhzx", "wubwjzolrx", "pjvisgmdrw", "titthqeskb"]}, {"name": "ppcmlxqgmn", "parents": ["pjvisgmdrw", "thceozowkb"]}, {"name": "qzntzflodp", "parents": ["wubwjzolrx", "titthqeskb", "thceozowkb"]}, {"name": "wubwjzolrx", "parents": []}, {"name": "pjvisgmdrw", "parents": []}, {"name": "titthqeskb", "parents": ["wubwjzolrx", "pjvisgmdrw"]}, {"name": "thceozowkb", "parents": ["pjvisgmdrw", "titthqeskb"]}]
raw_classes = input()
classes_object = json.loads(raw_classes)

map_child_parents = {}
for c in classes_object:
    map_child_parents[c['name']] = c['parents']

map_parent_children = {}
for child,parents in map_child_parents.items():
    for parent in parents:
        if parent in map_parent_children:
            map_parent_children[parent].add(child)
        else:
            map_parent_children[parent] = {child}
    if child not in map_parent_children:
        map_parent_children[child] = set()

for c in sorted(map_parent_children):
    visited = dfs(map_parent_children, c)
    print(c, ':', len(visited))
