#!/usr/bin/env python3

from typing import List

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

def main():
    '''driver code'''

if __name__ == "__main__":
    main()
