# Digital image processing

## Introduction

### Digital image

An image may be defined as a two-dimensional function, $f(x,y)$, where $x$ and $y$ are spatial coordinates, and the amplitude of $f$ at any pair of coordinates $(x,y)$ is called the intensity or gray level of the image at that point. When $x$, $y$, and the intensity values of $f$ are all finite, discrete quantities, the image is called a digital image.

## Image acquisition and representation

### Sampling and quantization

Digital image acquisition equipment is essentially concerned with the generation of a two-dimensional array of integer values representing the reflectance function of the actual scene at discrete spatial intervals. This is accomplished by the processes of sampling and quantization.

## Fundamentals of digital image processing

Image processing operators map pixel values from one image to another image. There are three distinct classes of operations: point operations, neighborhood operations, and geometric operations.

### Point operations

A point operation is an operation in which each pixel in the output image is a function of the gray level of the pixel at the corresponding position in the input image, and only of that pixel. Point operations are also referred to as gray scale manipulation operations. They can not alter the spatial relationships of the image. Typical uses of point operations include photometric decalibration, to remove the effects of spatial variations in the sensitivity of the camera system, contrast stretching, and thresholding.

#### Contrast stretching

Contrast stretching or normalization is a simple image enhancement technique that attempts to improve the contrast in an image by stretching the range of intensity values it contains to span a desired range of values. It differs from the more sophisticated histogram equalization in that it can only apply a linear scaling function to the image pixel values. Most implementations accept a gray 1 image as input and produce another gray level image as output.

Before stretching can be performed, it is necessary to specify the upper pixel value limit, $l_{max}$, and lower pixel value limit, $l_{min}$ over which the image is to be normalized. Often these limits are simply the minimum and maximum pixel values that the image type allows.

The simplest type of normalization then scans the image to find the lowest pixel value, $v_{min}$, and highest pixel value, $v_{max}$, currently present in the image. Then each pixel, $P_{in}$, is scaled using the following function:

$$
P_{out} = (P_{in} - v_{min}) \times \frac{(l_{max} - l_{min})}{(v_{max} - v_{min})} + l_{min}
$$

- The term $(P_{in} - v_{min})$ aligns the minimum pixel value in the input image with the starting value of the output pixel value range, making it easier to stretch the contrast while preserving the relative differences between pixel values.
- Multiplication by $\frac{(l_{max} - l_{min})}{(v_{max} - v_{min})}$ spreads out the pixel values over the desired output range, effectively increasing the contrast. The term represents the scale factor needed.
- Addition of the term $l_{min}$ is used as an offset or bias by determining the lower bound of the output pixel values. It essentially shifts the entire stretched range of pixel values as desired, thereby allowing to adjust the brightness or darkness of the output image.
- Values below $0$ are set to $0$, and values above $255$ are set to $255$.

#### Thresholding

Thresholding is an image segmentation technique in which pixel values are reassigned to either black or white depending on a threshold value. In the simplest implementation, the output of thresholding is a binary image representing the segmentation. In a single pass, each pixel in the image is compared with the intensity threshold. If the pixel value is higher than the threshold, the pixel is set to white, whereas, if the pixel value is less than the threshold, it is set to black.

However, not all images can be neatly segmented into foreground and background using thresholding. Whether an image can be correctly segmented using thresholding can be determined by the intensity histogram of the image. If there is a distinct peak corresponding to the foreground objects, then the intensity of pixels within the foreground objects must be distinctly different from the intensity of pixels within the background. In such a case, it is possible to separate out the foreground from the background by choosing a threshold to isolate the peak. If such a peak does not exist, then it is unlikely that simple thresholding will produce a good segmentation.

```python
for x in range(columns):
    for y in range(rows):
        if image[x,y] > threshold:
            image[x,y] = 255
        else:
            image[x,y] = 0
```

#### Adaptive thresholding



