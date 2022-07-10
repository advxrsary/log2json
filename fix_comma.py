import sys
from termcolor import colored

try:
    file_name = sys.argv[1]
except IndexError:
    print(colored('\n[#]', 'red'), colored("Specify log file!"))
    sys.exit(1)

def fix_comma(thefile):
    print(colored('[*]', 'yellow'), "Fixing comma...")
    read_file = open(thefile, "r")
    text = read_file.read()
    x = text.replace('},]', '}\n]')
    with open(thefile, "w") as file:
        file.writelines(x)
    print(colored('[+]', 'green'), "File fixed!")

if __name__ == "__main__":
    fix_comma(file_name)
    

