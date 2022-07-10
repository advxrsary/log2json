import sys
from termcolor import colored

# Chech if file is specified
try:
    file_name = sys.argv[1]
except IndexError:
    print(colored('\n[#]', 'red'), colored("Specify log file!"))
    sys.exit(1)

# Read json, search for pattern and replace comma with \n
def fix_comma(thefile):
    print(colored('[*]', 'yellow'), "Fixing comma...")
    read_file = open(thefile, "r")
    text = read_file.read()
    x = text.replace('},]', '}\n]')
    with open(thefile, "w") as file:
        file.writelines(x)
    print(colored('[+]', 'green'), "File fixed!")