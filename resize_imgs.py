from PIL import Image
import os
import numpy as np

# making sub folders in resized folder
for i in os.listdir('./absolute_filtered/'):
    os.mkdir(f'{os.getcwd()}\\imgs\\{i}')

# resizing the images by loading them from renamed folder and resizing by 50x70 pixels and converting it into grayscale by img.convert("L")
c=1
for i in os.listdir('./absolute_filtered/'):
    for j in os.listdir(f'./absolute_filtered/{i}'):
        img_path = f'{os.getcwd()}/absolute_filtered/{i}/{j}'
        img = Image.open(img_path)
        img = img.resize((50,70))
        img.save(f'./imgs/{i}/{c}.jpg')
        c+=1
    c=1

# # verify the sizes
# for i in os.listdir(f'./resized/'):
#     for j in os.listdir(f'./resized\\{i}\\'):
#         # summarize some details about the image
#         image = Image.open(f'./resized\\{i}/{j}')
#         print(image.size)
