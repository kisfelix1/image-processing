# Used to load an image
from PIL import Image
# Used to create kernels for filtering
import numpy as np

from matplotlib_utility import MatPlotLibUtility

# Loads the image from the specified file
image = Image.open("spatial_filtering/resources/image.jpeg")

# Get the number of rows and columns in the image
rows, cols = image.size
# Creates values using a normal distribution with a mean of 0 and standard deviation of 15, the values are converted to unit8 which means the values are between 0 and 255
noise = np.random.normal(0,15,(rows,cols,3)).astype(np.uint8)
# Add the noise to the image
noisy_image = image + noise
# Creates a PIL Image from an array
noisy_image = Image.fromarray(noisy_image)
# Plots the original image and the image with noise using the function defined at the top
MatPlotLibUtility.plot_images(image, noisy_image, title_1="Orignal", title_2="Image Plus Noise")
print("halo")