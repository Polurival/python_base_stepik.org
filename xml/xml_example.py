from xml.etree import ElementTree


def calc_scores(cubes, score):
    if score == 1:
        color_scores_map[cubes.attrib['color']] = score
    if len(cubes):
        score += 1
        for sub_cube in cubes:
            color_scores_map[sub_cube.attrib['color']] = color_scores_map[sub_cube.attrib['color']] + score
            calc_scores(sub_cube, score)

color_scores_map = {'blue': 0, 'red': 0, 'green': 0}

cubes_root = ElementTree.fromstring(input())
calc_scores(cubes_root, 1)

for color, score in reversed(sorted(color_scores_map.items())):
    print(score, end=' ')
