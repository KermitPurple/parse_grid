#!/usr/bin/env python3

from typing import List
from PIL import Image

def write_str_list(lines: List[str], filename: str):
    '''
    puts the contents of a list of strings into a file
    seperated by newline characters
    :lines: a list of lines to be put into the file
    :filename: the name of the file
    '''
    write_str('\n'.join(lines), filename)

def write_str(text: str, filename: str):
    '''
    puts the contents of a string into a file
    :text: the text to write a file
    :filename: the name of the file
    '''
    with open(filename, 'w') as f:
        f.write(text)

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
    for i in range(grid_size[1]):
        for j in range(grid_size[0]):
            pixel = pixels[
                offset[0] + j * cell_size[0],
                offset[1] + i * cell_size[1]
                ]
            if pixel[0] == 255:
                result += '.'
            else:
                result += 'x'
        result += '\n'
    return result[:-1]

def main():
    '''driver code'''
    print(parse_grid('conway.png', (38 ,11), (7, 7)))

if __name__ == "__main__":
    main()
