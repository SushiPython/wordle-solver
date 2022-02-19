from PIL import Image, ImageGrab
import time

time.sleep(1)

x = [718, 814, 911, 1020, 1120]
y = [376, 460, 550, 633, 722, 805]

for i in x: 
    for j in y:
        print(f'{i},{j}: {ImageGrab.grab().getpixel((i,j))}')