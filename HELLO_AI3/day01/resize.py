import cv2
import os
load_dir = "gana_en/"
write_dir = "gana_resize/"
files= os.listdir(load_dir)
print(files)
for f in files:
    image = cv2.imread(f"{load_dir}{f}")
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img_gray,(56,56))
    cv2.imwrite(f"{write_dir}{f}",img)
