# Re-import necessary libraries and re-define components for the task
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete
from sklearn.neural_network import MLPRegressor

# Define dimensions and generate all possible images
width, height = 3, 3
total_pixels = width * height
all_images = [np.array([int(x) for x in format(i, '0' + str(total_pixels) + 'b')]).reshape(width, height) 
              for i in range(2 ** total_pixels)]

# Calculate probabilities proportional to the number of black pixels in each image
probs = [np.sum(image) for image in all_images]
probs = np.array(probs) / np.sum(probs)

# Create the original Categorical distribution
categorical_rv = rv_discrete(name='categorical', values=(np.arange(len(all_images)), probs))

# Sample 200 unique images from the original Categorical distribution
unique_samples_index = np.unique(categorical_rv.rvs(size=512), return_index=True)[1][:200]

# Extract the probabilities of these unique samples as labels
unique_probs = probs[unique_samples_index]
print('unique_probs', unique_probs.shape)
# Flatten the unique samples for training
flattened_samples = np.array([img.flatten() for img in np.array(all_images)[unique_samples_index]])
print('flattened_samples', flattened_samples.shape)
# Create and train the MLP model
mlp = MLPRegressor(hidden_layer_sizes=(50,), max_iter=500, random_state=42)
mlp.fit(flattened_samples, unique_probs)

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
