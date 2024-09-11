# DCT-DFT-and-DWT

This code applies the **Discrete Cosine Transform (DCT)** and its inverse on a grayscale image, but there are a couple of issues to address for it to function as intended. Let’s break down each part of the code and what it does, including necessary corrections.

### 1. **Importing the required libraries:**
```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
```
- **`cv2`** (OpenCV) is used for image processing.
- **`numpy`** is used for numerical operations, particularly for manipulating arrays.
- **`matplotlib.pyplot`** is imported, but not actually used in this script. It can be removed unless you plan to use it for plotting later.

### 2. **Reading the image in grayscale:**
```python
img = cv2.imread('cornee.png', 0)
```
- The image `'cornee.png'` is read in grayscale mode (`0` flag), meaning that pixel values will range from 0 to 255 for a single channel.

### 3. **Converting the image to `float32`:**
```python
imf = np.float32(img)
```
- The image is converted to `float32`, which is necessary for the **DCT** function. DCT operates in floating-point arithmetic to capture frequency components with higher precision.

### 4. **Applying the Discrete Cosine Transform (DCT):**
```python
dct = cv2.dct(imf, cv2.DCT_ROWS)
```
- **`cv2.dct(imf)`** computes the **2D DCT** on the input image. This breaks down the image into a series of frequency components. 
  - The `cv2.DCT_ROWS` flag applies the DCT **row-wise**, which might not be suitable if you want to apply it to the entire image (2D). To apply DCT in 2D, the default function call `cv2.dct(imf)` without any flag is typically preferred:
    ```python
    dct = cv2.dct(imf)
    ```

### 5. **Applying the Inverse Discrete Cosine Transform (IDCT):**
```python
img1 = cv2.idct(dct)
```
- **Inverse DCT** transforms the frequency domain data back into the spatial domain, reconstructing the original image.

### 6. **Converting the reconstructed image back to `uint8`:**
```python
img1 = np.uint8(img)
```
- Here’s a critical issue. This line mistakenly converts the **original image (`img`)** back to `uint8`, not the transformed image (`img1`). It should instead convert `img1` (the IDCT result) to `uint8`:
  ```python
  img1 = np.uint8(img1)
  ```

### 7. **Displaying the images using OpenCV:**
```python
cv2.imshow("DCT", dct)
cv2.waitKey(0)
cv2.imshow("IDCT back image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **`cv2.imshow()`** is used to display images. However, the **DCT result** (`dct`) will likely not display correctly because it contains floating-point values, some of which may fall outside the range `[0, 255]` required for image display.
  - Before displaying, you may want to normalize the DCT result to make it viewable. This can be done by scaling the values to the range `[0, 255]`:
    ```python
    dct_display = cv2.normalize(dct, None, 0, 255, cv2.NORM_MINMAX)
    dct_display = np.uint8(dct_display)
    ```
- **`cv2.waitKey(0)`** waits indefinitely until a key is pressed before continuing.

### What does this code do?
- **DCT**: The DCT breaks down the image into a set of cosine functions, representing the image in terms of its frequency components. DCT is often used in image compression techniques like JPEG because most of the essential information is concentrated in the low frequencies, allowing higher-frequency components to be discarded.
  
- **Inverse DCT (IDCT)**: Reverses the process by converting the frequency components back into the spatial domain to reconstruct the original image.

### Key Changes:
1. **Use proper `cv2.dct()` without the `cv2.DCT_ROWS` flag** for a full 2D DCT.
   ```python
   dct = cv2.dct(imf)
   ```

2. **Normalize the DCT output before displaying**:
   ```python
   dct_display = cv2.normalize(dct, None, 0, 255, cv2.NORM_MINMAX)
   dct_display = np.uint8(dct_display)
   cv2.imshow("DCT", dct_display)
   ```

3. **Convert the IDCT result to `uint8` before displaying**:
   ```python
   img1 = np.uint8(img1)
   ```

After these adjustments, the DCT and IDCT results will display properly.
