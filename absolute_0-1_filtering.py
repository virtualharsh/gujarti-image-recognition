from PIL import Image
import os
import numpy as np


# # making sub folders in resized folder
# for i in os.listdir('imgs/'):
#     os.mkdir(f'{os.getcwd()}\\absolute_filtered\\{i}')


# c=1
# for i in os.listdir(f'./rem/'):
#     print(i)
#     for j in os.listdir(f'./resized\\{i}\\'):
#         processed_absolute_image =  Image.open(f'./resized/{i}/{j}')
#         thresh = 130
#         fn = lambda x : 255 if x > thresh else 0
#         r = processed_absolute_image.convert('L').point(fn, mode='1')
#         r.save(f'./absolute_filtered/{i}/{c}.jpg')
#         c+=1
#     c=1


c=211
var = 8
for i in os.listdir(f'./rem/{var}/'):
    processed_absolute_image =  Image.open(f'./rem/{var}/{i}')
    thresh = 130
    fn = lambda x : 255 if x > thresh else 0
    r = processed_absolute_image.convert('L').point(fn, mode='1')
    r.save(f'./rem/{var}/{c}.jpg')
    c+=1

c=1000
for i in os.listdir(f'./rem/{var}/'):
    img_path = f'./rem/{var}/{i}'
    img = Image.open(img_path)
    img = img.resize((50,70))
    img.save(f'{c}.jpg')
    c+=1