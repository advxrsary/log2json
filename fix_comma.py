import sys
from termcolor import colored


# Read json, search for pattern and replace comma with \n
def fix_comma(thefile):
    print(colored('[*]', 'yellow'), "Fixing comma...")
    raw_out = []
    read_file = open(thefile, "r")
    text = read_file.read()
    x = text.replace('},]', '}\n]')
    return x
    
def write_file(thefile, text):
    with open(thefile, "w") as file:
        file.writelines(text)
    print(colored('[+]', 'green'), f"File {thefile} fixed!")
    
if __name__ == "__main__":
    # Check if file is specified
    try:
        file_name = sys.argv[1]
    except IndexError:
        print(colored('\n[#]', 'red'), "Specify log file!")
        sys.exit(1)

    # Self-execute
    x = fix_comma(file_name)
    write_file(file_name, x)
