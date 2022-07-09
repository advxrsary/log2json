# "client", "messageid", "address", "status"
import json


file_name = 'email.txt'
json_file = 'email.json'
file = open(file_name, "r")
jfile = open(json_file, "w")
data = []
order = ["time", "sessionid", "message"]
newlist = []

for line in file.readlines():
    details = line.split("\t")
    details = [x.strip() for x in details]
    newlist.append(details[2].split('=')[1])
    structure = {key:value for key, value in zip(order, details)}
    data.append(structure)

def write_json():
    for entry in data:
        jfile.writelines(json.dumps(entry, indent=4))
        jfile.write(",\n")

if __name__ == "__main__":
    jfile.write('[\n')
    write_json()
    jfile.write(']')
    print(sorted(newlist))