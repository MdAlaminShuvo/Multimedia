import numpy as np
import matplotlib.pyplot as plt


def dct(image):
    # Apply DCT on the image
    transformed_image = np.zeros_like(image, dtype=float)
    rows, cols = image.shape

    for u in range(rows):
        for v in range(cols):
            sum_val = 0.0

            for x in range(rows):
                for y in range(cols):
                    cos_val = np.cos((2 * x + 1) * u * np.pi / (2 * rows)) * \
                        np.cos((2 * y + 1) * v * np.pi / (2 * cols))
                    sum_val += image[x, y] * cos_val

            alpha_u = 1 / np.sqrt(rows) if u == 0 else np.sqrt(2 / rows)
            alpha_v = 1 / np.sqrt(cols) if v == 0 else np.sqrt(2 / cols)

            transformed_image[u, v] = alpha_u * alpha_v * sum_val

    return transformed_image


def idct(transformed_image):
    # Apply IDCT on the transformed image
    rows, cols = transformed_image.shape
    reconstructed_image = np.zeros_like(transformed_image, dtype=float)

    for x in range(rows):
        for y in range(cols):
            sum_val = 0.0

            for u in range(rows):
                for v in range(cols):
                    cos_val = np.cos((2 * x + 1) * u * np.pi / (2 * rows)) * \
                        np.cos((2 * y + 1) * v * np.pi / (2 * cols))
                    alpha_u = 1 / \
                        np.sqrt(rows) if u == 0 else np.sqrt(2 / rows)
                    alpha_v = 1 / \
                        np.sqrt(cols) if v == 0 else np.sqrt(2 / cols)
                    sum_val += alpha_u * alpha_v * \
                        transformed_image[u, v] * cos_val

            reconstructed_image[x, y] = sum_val

    return reconstructed_image


# Create a grayscale image of size 16x16
image = np.random.randint(0, 256, (16, 16), dtype=np.uint8)

# Plot the reconstructed image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Apply DCT on the image
transformed_image = dct(image)

# Plot the transformed image
plt.subplot(1, 3, 2)
plt.imshow(transformed_image, cmap='gray')
plt.title('DCT Transformed Image')
plt.axis('off')

# Apply IDCT on the transformed image
reconstructed_image = idct(transformed_image)

# Plot the reconstructed image
plt.subplot(1, 3, 3)
plt.imshow(reconstructed_image, cmap='gray')
plt.title('IDCT Reconstructed Image')
plt.axis('off')

# Display the images
plt.tight_layout()
plt.show()
