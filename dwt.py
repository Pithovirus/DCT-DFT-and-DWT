import cv2
import numpy as np
import pywt
import matplotlib.pyplot as plt


# Load a CT scan image (as grayscale)
img = cv2.imread('ct_scan.png', 0)

# Apply 2D Discrete Wavelet Transform (DWT)
coeffs2 = pywt.dwt2(img, 'haar')

# coeffs2 contains four sub-bands (LL, LH, HL, HH)
LL, (LH, HL, HH) = coeffs2

# Display the sub-bands
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(LL, cmap='gray')
plt.title('Approximation (LL)')

plt.subplot(2, 2, 2)
plt.imshow(LH, cmap='gray')
plt.title('Horizontal Detail (LH)')

plt.subplot(2, 2, 3)
plt.imshow(HL, cmap='gray')
plt.title('Vertical Detail (HL)')

plt.subplot(2, 2, 4)
plt.imshow(HH, cmap='gray')
plt.title('Diagonal Detail (HH)')

plt.show()
