import sys
from termcolor import colored

# Read json, search for pattern and replace comma with \n
def fix_comma(thefile):
    print(colored('[*]', 'yellow'), "Fixing comma...")
    read_file = open(thefile, "r")
    text = read_file.read()
    x = text.replace('},]', '}\n]')
    with open(thefile, "w") as file:
        file.writelines(x)
    print(colored('[+]', 'green'), f"File {thefile} fixed!")

if __name__ == "__main__":
    # Check if file is specified
    try:
        file_name = sys.argv[1]
    except IndexError:
        print(colored('\n[#]', 'red'), "Specify log file!")
        sys.exit(1)

    # Self-execute
    fix_comma(file_name)