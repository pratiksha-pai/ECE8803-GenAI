import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

# Load MNIST data and binarize
(train_images, _), _ = mnist.load_data()
train_images = (train_images > 127.5).astype(np.float32)

# Calculate MLE for theta (probability of pixel being white)
# theta_mle = np.mean(train_images, axis=0) / 255.0
theta_mle = np.mean(train_images, axis=0)


# Generate 10 samples using Bernoulli distribution
samples = np.random.binomial(n=1, p=theta_mle, size=(10, 28, 28))

# Visualize the generated samples
fig, axes = plt.subplots(1, 10, figsize=(20, 2))

for i in range(10):
    axes[i].imshow(samples[i], cmap='gray')
    axes[i].axis('off')

plt.show()
