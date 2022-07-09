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
        # if first_dict['sessionid'] == second_dict['sessionid']:
        #     second_dict.pop('time')
        #     final_dict = first_dict | second_dict
        #     print(final_dict)
        dict2_sorted = {i: dict2[i] for i in dict1.keys()}
        keys = dict1.keys()
        values = zip(dict1.values(), dict2_sorted.values())
        final_dict = dict(zip(keys, values))

def write_json():
    jfile.write('[\n')
    for entry in data:
        jfile.writelines(json.dumps(entry, indent=4))
        jfile.write(",\n")
    jfile.write(']')

if __name__ == "__main__":
    create_cell()
    write_json()