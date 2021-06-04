Packages Used:
OpenCV: OpenCV is a cross-platform library using which we can develop real-time computer vision applications. It mainly focuses on image processing, video capture and analysis including features like face detection and object detection.
Use "import cv2" command to import the module

Approach:
1) Find an image that we want to convert into a pencil sketch.
2) Read in the Red, Blue, Green (RBG) image and then convert it to a gray scale image. This effectively makes the image a classic “black and white” photo. This will be our “gray scale image”.
3) We are going to invert the “gray scaled image” also known as getting the image negative, this will be our “inverted gray scale image”. Inversion can be used to enhance details. The Logical NOT or invert is an operator which takes a binary or gray level image as input and produces its photographic negative, i.e. dark areas in the input image become light and light areas become dark.
4)  Use a Gaussian function to blur the image. In image processing, a Gaussian blur (also known as Gaussian smoothing) is the result of blurring an image by a Gaussian function (named after mathematician and scientist Carl Friedrich Gauss). It is a widely used effect in graphics software, typically to reduce image noise and reduce detail.
5) Invert the newly created “blurred image”, this will be called the “inverted blurred image”.
6) Now we are going to create the pencil sketch image by blending the “gray scale image” with the “inverted blurred image”. This can be done by dividing the “gray scale image” by the “inverted blurred image”. Since images are just arrays we can easily do this in programming by using the divide function from the cv2 library. 