import os

pypaths = []
for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if os.path.splitext(file)[-1].lower() == '.py' and current_dir not in pypaths:
            pypaths.append(current_dir)
print(pypaths)

with open('pypaths.txt', 'w') as out:
    out.write('\n'.join(pypaths))