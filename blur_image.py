import cv2

# Load one of your sample images
image = cv2.imread("images/sample1.jpg")

# Apply blur
blurred = cv2.GaussianBlur(image, (21, 21), 0)

# Save as new file
cv2.imwrite("images/sample1_blurry.jpg", blurred)

print("Blurry image saved as sample1_blurry.jpg")
