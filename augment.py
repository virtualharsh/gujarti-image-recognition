import os
from PIL import Image

c = 123
for i in os.listdir('./temp/'):
    print(i)
    original_img = Image.open(f"./temp/{i}")
    horizaontal_img = original_img.rotate(10)
    horizaontal_img.save(f"./temp/{c}.jpg")
    c+=1
    horizaontal_img.close()
    original_img.close()

    