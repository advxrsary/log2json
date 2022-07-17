#!/usr/bin/env python3
__author__ = 'Sevastian Zare (@advxrsary)'
__date__ = '20220710'
__license__ = 'MIT'
__version__ = '1.01'
__description__ = """ Fixes comma in json file """
__manual__ = """To fix the file, run: python3 fix_comma.py [file-to-fix]"""


import sys
from termcolor import colored

# Read json, search for pattern and replace comma with \n
def fix_comma(thefile):
    print(colored('\n[‡]', 'blue'), "Fixing comma...")
    read_file = open(thefile, "r")
    text = read_file.read()
    x = text.replace('},]', '\t}\n]')
    return x

def fix_braces(thefile):
    print(colored('[‡]', 'blue'), "Fixing indents...")
    read_file = open(thefile, "r")
    text = read_file.read()
    x = text.replace('},\n\t{', '\t},\n\t{')
    return x

def write_file(thefile, text):
    with open(thefile, "w") as file:
        file.writelines(text)

if __name__ == "__main__":
    # Check if file is specified
    try:
        file_name = sys.argv[1]
    except IndexError:
        print(colored('\n[!]', 'yellow'), 'To fix the comma run:')
        print(colored('[›]', 'green'), 'python3 fix_comma.py [file-to-fix]')
        sys.exit(1)

    # Self-execute
    x = fix_comma(file_name)
    write_file(file_name, x)
    print(colored('[‡]', 'blue'), f"File {file_name} fixed!")
