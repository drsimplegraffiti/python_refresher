import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# run in terminal > python app.py Pokedex/ new/

print(image_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    img.save(f"{output_folder}{filename}", "png")
    print("all done")