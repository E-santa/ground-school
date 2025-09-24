## Week 3 Notes

1. What are some methods used for blob detection?

   a. Laplacian of Gaussian (does Gaussian Blur and then applies Laplacian filter on it)
   
   b. Convolution w/ a Kernel (applies a kernel to the image matrix in a way that changes it to something new, namely matrix dot product)

   c. OpenCV SimpleBlobDetector: convert RGB to Grayscale, then threshold to get binary image, then group white pixels into blobs

2. How can blob detection be used to find objects in a field? What are its benefits and limitations?

   a. Blob detection can be used to find where stuff is and isn't with blobs being revealed to be certain stuff, and it's lightweight but it isn't exactly the most sophisticated when it comes to differentiating between objects.

3. What are the underlying mechanics of the convolutional neural network used in the YOLO model?

   a. A neural network acts like a multilayer "linear" classifier, only with nonlinear behavior modeled through activation functions peppered in after each linear layer.
   
   b. During training, the weights and biases are updated through gradient descent in order to minimize the loss function (measure of error).
   
   c. The convolutional neural network used in the YOLO model includes a series of convolutions (and poolings just to reduce dimensionality and thus lessen overfitting and noise) before the rest of the neural network, and said convolutions' values are updated along with the weights and biases during training.

   d. YOLO is a one-shot CNN, which sacrifices some accuracy for speed.

   e. For training, we split our data in 3: training (actually changes weights), validation (for changing hyperparameters and deciding when to stop training to avoid overfitting), and test (actually evaluates how good model is). Usually, a 70/20/10 training/validation/test split is good.

4. How can our club leverage our manpower to label many images in a short amount of time on roboflow?

   a. Roboflow is a website to conveniently label images and deploy models.

5. What are some upsides and downsides to using YOLO for our competition vehicle?

   a. The upside to using YOLO as opposed to blob detection is that it is more accurate, and the upside to using YOLO as opposed to other object detection models like RCNN is that it is more compute-efficient.

   b. The downside to using YOLO as opposed to blob detection is that it is more compute-intensive, while the downside to using YOLO as opposed to other object detection models like RCNN is that it is less accurate.
   
7. What other techniques might there be for object detection?

   a. We can try other object detection models not from the YOLO family (might be more lightweight and/or accurate, SSD MobileNet and EfficientDet seem promising).

   b. We can try using color change boundaries to detect models (lightweight, but not very useful).
