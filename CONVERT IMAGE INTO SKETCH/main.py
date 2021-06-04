import cv2
img = cv2.imread("file.jpg")

# Convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert grayscale image
gray_image = cv2.bitwise_not(img)

# Blur inverted image
blurred = cv2.GaussianBlur(gray_image, (21, 21), 0)

# Invert blurred image
invert_blurred = cv2.bitwise_not(blurred)

# Final sketch
sketch_image = cv2.divide(img, invert_blurred, scale=250.0)
cv2.imwrite("file1.jpg", sketch_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
