from PIL import Image
import numpy as np
original = Image.open('./images/azusachibi.jpg')
fft = Image.open('./images/azusachibi_fft.bmp')
original = np.array(original)
fft = np.array(fft)

diff = []
for row_ori, row_fft in zip(original, fft):
    diff.append([])
    for pixel_ori, pixel_fft in zip(row_ori, row_fft):
        diff[-1].append(int(pixel_ori[0]) - int(pixel_fft[0]))
open('./diff/azusachibi_fft_diff.txt', 'w+').write(str(diff))