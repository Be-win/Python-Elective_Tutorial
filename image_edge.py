from images import Image


def detect_edges(image, threshold=30):
    def grayscale(pixel):
        r, g, b = pixel
        return (r + g + b) // 3

    new_image = image.clone()
    width, height = image.getWidth(), image.getHeight()

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            center = grayscale(image.getPixel(x, y))
            right = grayscale(image.getPixel(x + 1, y))
            below = grayscale(image.getPixel(x, y + 1))

            edge_intensity = abs(center - right) + abs(center - below)

            color = (255, 255, 255) if edge_intensity > threshold else (0, 0, 0)
            new_image.setPixel(x, y, color)

    new_image.draw()
    return new_image

image = Image(input("Enter image path: "))
edged_image = detect_edges(image, threshold=30)
