#!/usr/bin/env python3

from typing import List
from PIL import Image

def color_almost_eq(a: (int, int, int), b: (int, int, int)) -> bool:
    '''
    returns if two rgb colors are almost the same color
    no more than 5 difference between two same vals
    :a: first color value rgb format
    :b: second color value rgb format
    '''
    return abs(a[0] - b[0]) <= 5 and abs(a[1] - b[1]) <= 5 and abs(a[2] - b[2]) <= 5

def parse_grid(filename: str, grid_size: (int, int), offset: (int, int) = (0, 0)) -> str:
    '''
    parses an image and converts it into a grid of 'x' and '.'
    :filename: name of file to open
    :offset:
    :grid_size:
    '''
    img = Image.open(filename)
    cell_size = (
            img.size[0] / grid_size[0],
            img.size[1] / grid_size[1]
            )
    pixels = img.load()
    result = ''
    color1 = None
    color2 = None
    for i in range(grid_size[1]):
        for j in range(grid_size[0]):
            pixel = pixels[
                offset[0] + j * cell_size[0],
                offset[1] + i * cell_size[1]
                ]
            if color1 is None:
                color1 = pixel
                result += '.'
            elif color2 is None and not color_almost_eq(color1, pixel):
                color2 = pixel
                result += 'x'
            elif color_almost_eq(color1, pixel):
                result += '.'
            elif color_almost_eq(color2, pixel):
                result += 'x'
            else:
                raise ValueError('Third color detected')
        result += '\n'
    return result[:-1]

def main():
    '''driver code'''
    print(parse_grid('conway.png', (38 ,11), (7, 7)))

if __name__ == "__main__":
    main()
