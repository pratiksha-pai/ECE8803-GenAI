from PIL import ImageEnhance
import cv2
import pytesseract
from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
from PIL import Image

# Load the uploaded image to inspect the DAG
image_path = 'q3.png'
image = Image.open(image_path)
image.show()


# # Load the image using OpenCV
image_cv = cv2.imread(image_path)

# # Convert the image to grayscale
gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

# # Use Tesseract to extract text
extracted_text = pytesseract.image_to_string(gray_image)

# # Show extracted text
print(extracted_text)


# # Enhance the image for better graph extraction
# enhancer = ImageEnhance.Contrast(Image.fromarray(gray_image))
# enhanced_image = enhancer.enhance(2.0)

# # Convert the enhanced image to array
# enhanced_image_array = np.array(enhanced_image)

# # Detect edges in the image using Canny detector
# edges = cv2.Canny(enhanced_image_array, threshold1=30, threshold2=100)

# # Detect points that form a line
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=10, maxLineGap=250)

# # Draw lines on the image
# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     cv2.line(image_cv, (x1, y1), (x2, y2), (0, 255, 0), 3)

# # Display the image with lines
# plt.imshow(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))
# plt.title('Lines detected')
# plt.show()