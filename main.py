from PIL import Image

def stylize(offset, image):
    image_name = image
    image = Image.open(image)

    if image.mode != "RGB":
        image = image.convert("RGB")

    red, green, blue = image.split()
    red = red.crop((offset, 0, red.width, red.height))
    blue = blue.crop((0, 0, blue.width - offset, blue.height))
    green = green.crop((offset / 2, 0, green.width - offset / 2, green.height))

    stylize_image = Image.merge("RGB", (red, green, blue))
    stylize_image.save("{}_avatar.jpg".format(image_name.split('.')[0]))

if __name__ == "__main__":
    stylize(50, 'monro.jpg')