l = []
grades = {}
with open('dataset_3363_4.txt', "r", encoding='UTF8') as inf:
	for line in inf:
		l = line.strip().split(';')
		grades[l[0]] = l[1:4]
		averageGrade = (int(l[1]) + int(l[2]) + int(l[3])) / 3
		print(averageGrade)

mathAverageGrade = 0
physicsAverageGrade = 0
langAverageGrade = 0
for v in grades.values():
	mathAverageGrade += int(v[0])
	physicsAverageGrade += int(v[1])
	langAverageGrade += int(v[2])
print(mathAverageGrade / len(grades), end=' ')
print(physicsAverageGrade / len(grades), end=' ')
print(langAverageGrade / len(grades), end='')