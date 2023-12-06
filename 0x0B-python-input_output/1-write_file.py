#!/usr/bin/python3
"""write_file: write_file()"""

def number_of_lines(filename=""):
    """my function"""
    cont = 0
    with open(filename, 'r') as f:
        for li in f:
            cont += 1
    return cont
