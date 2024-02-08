from matplotlib import pyplot as plt
from PIL import Image as i, ImageEnhance
import numpy as np

# Function to load an image from a file
def load_image(filename):
    image = i.open(filename)
    # Display the loaded image
    # image.show()
    return image

# Function to crop the image to a specific region
def crop_image(image):
    box = (50, 50, 200, 200)
    cropped_image = image.crop(box)
    # Display the cropped image
    cropped_image.show()

# Function to adjust the brightness of an image
def adjust_brightness(image):
    img1 = ImageEnhance.Brightness(image)
    bright_img = img1.enhance(1.5)
    # Save the adjusted image
    bright_img.save('bright', 'png')
    # Display the adjusted image
    bright_img.show()
    return True

# Function to adjust the sharpness of an image
def adjust_sharpness(image):
    img2 = ImageEnhance.Sharpness(image)
    sharp_image = img2.enhance(3)  # A factor of 3 sharpens the image
    # Display the sharpened image
    sharp_image.show()
    return True

# Function to adjust the saturation of an image
def adjust_saturation(image):
    converter = ImageEnhance.Color(image)
    img2 = converter.enhance(0.5)  # Reducing saturation
    # Display the desaturated image
    img2.show()

# Function to calculate histograms for each color channel
def Histogram_Analysis(image):
    r, g, b = image.split()
    return r.histogram(), g.histogram(), b.histogram()

# Function to display a line plot of histograms for each color channel
def display_histogram(r_hist, g_hist, b_hist):
    plt.figure()
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.plot(r_hist, color='red', label='Red')
    plt.plot(g_hist, color='green', label='Green')
    plt.plot(b_hist, color='blue', label='Blue')
    plt.legend()
    plt.show()

# Function to display a bar plot of histograms for each color channel
def bar_histogram(image):
    plt.figure()
    plt.title('Color Histogram (Separate Bars)')
    plt.xlabel('Color Value Ranges')
    plt.ylabel('Pixel Value')
    colors = ('b', 'g', 'r')
    bin = 25
    for i, col in enumerate(colors):
        color_values = np.array(image)[:, :, i].flatten()
        hist, _ = np.histogram(color_values, bins=range(0, 256, bin))
        x_values = np.arange(0, 256, bin)[:-1] + i * bin
        plt.bar(x_values, hist, width=bin, color=col, label=col)
    plt.legend()
    plt.show()

# Loading image and displaying it
filename = 'images.jpg'
image = load_image(filename)

# Changing image dimensions or cropping
crop_image(image)

# Adjusting brightness, contrast, or saturation
adjust_brightness(image)
adjust_sharpness(image)
adjust_saturation(image)

# Histogram Analysis
r_hist, g_hist, b_hist = Histogram_Analysis(image)
display_histogram(r_hist, g_hist, b_hist)
bar_histogram(image)
