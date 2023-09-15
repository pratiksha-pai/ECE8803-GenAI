import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete

# Define the dimensions of the image
width, height = 3, 3

# Calculate the total number of pixels in the image
total_pixels = width * height

# Generate all possible binary images of size 3x3 (0 for white, 1 for black)
all_images = [np.array([int(x) for x in format(i, '0' + str(total_pixels) + 'b')]).reshape(width, height) 
              for i in range(2 ** total_pixels)]

# Calculate probabilities proportional to the number of black pixels in each image
probs = [np.sum(image) for image in all_images]
probs = np.array(probs) / np.sum(probs)
print(probs.shape)
print(sum(probs))
# Create a Categorical distribution using the calculated probabilities
categorical_rv = rv_discrete(name='categorical', values=(np.arange(len(all_images)), probs))

print(categorical_rv)

# Draw 5 samples from the Categorical distribution
samples = categorical_rv.rvs(size=5)

# Visualize the sampled images
fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for i, sample in enumerate(samples):
    axes[i].imshow(all_images[sample], cmap='gray')
    axes[i].axis('off')
plt.show()
