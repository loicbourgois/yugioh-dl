import os
from PIL import Image
import numpy as np
for path, dirs, files in os.walk("./images"):
    for file in files:
        if file.endswith(".jpg"):
            dest_path = path.replace('images', 'images-rotated')
            print(f"{path}/{file} -> {dest_path}/{file}")
            os.system(f'mkdir -p {dest_path}')
            input_image = np.array(Image.open(f"{path}/{file}"))
            Image.fromarray(np.rot90(input_image)).save(f"{dest_path}/{file}")
