import numpy as np
from sklearn.neural_network import MLPRegressor
from scipy.stats import rv_discrete
import matplotlib.pyplot as plt

# Define dimensions
width, height = 28, 28
total_pixels = width * height

# Sample 200 random images (Each pixel can be either 0 or 1)
# Note: We're not sampling from a categorical distribution here as per your scenario
random_samples = np.random.choice([0, 1], size=(200, width, height))

# Flatten the random samples for training
flattened_random_samples = random_samples.reshape(200, -1)

# Assume some arbitrary labels (probabilities) for the purpose of this example
# In a real-world scenario, these would be the probabilities of generating each image
random_labels = np.random.rand(200)

# Create and train the MLP model
mlp = MLPRegressor(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
mlp.fit(flattened_random_samples, random_labels)


# Predict probabilities for all possible images
predicted_probs = mlp.predict(np.array([img.flatten() for img in all_images]))
print('predicted_probs: ', predicted_probs.shape)
# Normalize the predicted probabilities
normalized_predicted_probs = np.maximum(predicted_probs, 0)
normalized_predicted_probs /= np.sum(normalized_predicted_probs)

# Create a new Categorical distribution based on the predicted probabilities
new_categorical_rv = rv_discrete(name='new_categorical', values=(np.arange(len(all_images)), normalized_predicted_probs))

# Draw 5 samples from the new Categorical distribution
new_samples = new_categorical_rv.rvs(size=5)

# Visualize the sampled images
fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for i, sample in enumerate(new_samples):
    axes[i].imshow(all_images[sample], cmap='gray')
    axes[i].axis('off')
plt.show()
