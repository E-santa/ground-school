## Week 3 Notes

1. What are some methods used for blob detection?

   a. Laplacian of Gaussian (does Gaussian Blur and then applies Laplacian filter on it)
   
   b. Convolution w/ a Kernel (applies a kernel to the image matrix in a way that changes it to something new, namely matrix dot product)

   c. OpenCV SimpleBlobDetector: convert RGB to Grayscale, then threshold to get binary image, then group white pixels into blobs

3. How can blob detection be used to find objects in a field? What are its benefits and limitations?
4. What are the underlying mechanics of the convolutional neural network used in the YOLO model?
5. How can our club leverage our manpower to label many images in a short amount of time on roboflow?
6. What are some upsides and downsides to using YOLO for our competition vehicle?
7. What other techniques might there be for object detection?
