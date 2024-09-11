# import required libraries
import cv2
import numpy as np

# read input image as grayscale
img = cv2.imread('cornee.png', 0)

# convert the grayscale to float32
imf = np.float32(img) # float conversion

# find discrete cosine transform
dst = cv2.dct(imf, cv2.DCT_INVERSE)

# apply inverse discrete cosine transform
img1 = cv2.idct(dst)

# convert to uint8
img1 = np.uint8(img)

# display the images
cv2.imshow("DCT", dst)
cv2.waitKey(0)
cv2.imshow("IDCT back image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()