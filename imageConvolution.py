import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = 1.0* plt.imread("al.jpg") #1.0 converts to double format
img = np.mean(img[:,:,:3], axis=2) #grayscale filter (averages pixels across rgb)

filt = np.array([[-0.125,-0.250, -0.125], [0,0,0], [0.125, 0.250, 0.125]]) 
#vertical edge filter

img_y = ndimage.convolve(img,filt,mode="reflect")
img_x = ndimage.convolve(img,filt.T,mode="reflect") 
#transpose swaps rows/columns. Horizontal filter
img_g = np.sqrt(img_y**2 + img_x**2) #combine both filters. diagonal equation for x&y

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(img_y, cmap="gray")
plt.subplot(1,3,2)
plt.imshow(img_x, cmap="gray")
plt.subplot(1,3,3)
plt.imshow(img_g, cmap="gray")
plt.show()