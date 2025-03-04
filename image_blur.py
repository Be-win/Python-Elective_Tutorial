from images import Image

def blur(image, radius):

    def average_color(pixels):
        r, g, b = zip(*pixels)
        return sum(r) // len(pixels), sum(g) // len(pixels), sum(b) // len(pixels)

    new_image = image.clone()
    width, height = image.getWidth(), image.getHeight()

    for y in range(radius, height - radius):
        for x in range(radius, width - radius):
            neighbors = [
                image.getPixel(x + dx, y + dy)
                for dx in range(-radius, radius + 1)
                for dy in range(-radius, radius + 1)
            ]
            new_pixel = average_color(neighbors)
            new_image.setPixel(x, y, new_pixel)

    new_image.draw()
    return new_image

image = Image(input("Enter image path: "))
blurred_image = blur(image, radius=3)
