import os
for path, dirs, files in os.walk("./images"):
    c = 0
    for file in files:
        if file.endswith(".jpg"):
            c += 1
    print(f'{path}: {c} *.png')
