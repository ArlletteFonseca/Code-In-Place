"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.

https://web.stanford.edu/class/archive/cs/cs106ap/cs106ap.1198/handouts/h10_Image_Reference_Guide.pdf

replace each bright pixel in an image with its grayscale equivalent
pixel: color represented by 3 integers between 0 and 255 representing its rgb.
grayscale: set red, green and blue components to its average component
bright pixel: average component is greater than 153

SimpleImage
    self.height
    self.width
    ...
    self.show()

Pixel
    ...
    self.red
    self.green
    self.blue

PSEUDO CODE
instantiate SimpleImage
loop through all pixels
    if bright
        make greyscale
            get avg
            set avg
Show it

"""

from simpleimage import SimpleImage

BRIGHT_AVERAGE = 153


def main():
    image = SimpleImage('images/simba-sq.jpg')

    for pixel in image:
        avg_pixel = get_pixel_average_rgb(pixel)
        if avg_pixel >= BRIGHT_AVERAGE:
            pixel.red = avg_pixel
            pixel.green = avg_pixel
            pixel.blue = avg_pixel
    image.show()


def get_pixel_average_rgb(pixel) -> int:
    """
    Takes pixel object and returns the average of its color attributes.

    :pixel: Pixel object to be averaged
    :return: average of pixel's red, green, and blue values.
    """
    total_pixel = pixel.red + pixel.green + pixel.blue
    return total_pixel // 3


if __name__ == '__main__':
    main()
