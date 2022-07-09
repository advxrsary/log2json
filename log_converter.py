import json
from itertools import islice

file_name = 'email.txt'
json_file = 'email.json'
file = open(file_name, "r")
jfile = open(json_file, "w")
data = []
message_list = []
new_message_list = {}
final_dict = {}

def seq_pairs(li):
    return zip(li, islice(li, 1, None))

def process_data():
    for line in file.readlines():
        details = line.split("\t")
        details = [x.strip() for x in details]
        message_details = details[2].split("=")
        details[2] = details[2].split("=")[1]
        structure = {key: value for key, value in zip(
            ["time", "sessionid", message_details[0]], details)}
        data.append(structure)
    return data
        
def create_cell():
    for dict1, dict2 in seq_pairs(process_data()):
        if dict1['sessionid'] == dict2['sessionid']:
            dict2.pop('time')
            final_dict = dict1 | dict2
            print(final_dict)

def write_json():
    jfile.write('[\n')
    for entry in data:
        jfile.writelines(json.dumps(entry, indent=4))
        jfile.write(",\n")
    jfile.write(']')

if __name__ == "__main__":
    create_cell()
    write_json()