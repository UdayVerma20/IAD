import cv2
import numpy as np
from matplotlib import pyplot as plt

def grayscale_threshold_and_count(image_path, threshold):
    """
    Converts an image to grayscale, applies a threshold to create a black and white image,
    and counts the number of white and black pixels.

    Args:
        image_path: The path to the image file.
        threshold: The threshold value for converting grayscale pixels to black or white.

    Returns:
        A tuple containing the number of white pixels and black pixels.
    """

    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the threshold
    _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    plt.imshow(thresh, interpolation='nearest')
    plt.show()
    # Count the number of white and black pixels
    white_pixels = np.count_nonzero(thresh == 255)
    black_pixels = np.count_nonzero(thresh == 0)

    return white_pixels, black_pixels

# Example usage
image_path = r"C:\Users\Asus\Desktop\TDR\iad_photo.jpeg"  # Replace with the actual path to your image
threshold_value = 220  # Adjust the threshold value as needed

white_count, black_count = grayscale_threshold_and_count(image_path, threshold_value)
print("Number of white pixels:", white_count)
print("Number of black pixels:", black_count)
ratio = white_count / (white_count + black_count) * 100
print("Ratio" , ratio)