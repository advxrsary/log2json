import json

file_name = 'email.txt'
json_file = 'email.json'
file = open(file_name, "r")
jfile = open(json_file, "w")
data = []
order = ["time", "sessionid", "message"]
message_list = []
new_message_list = {}

def process_data():
    for line in file.readlines():
        details = line.split("\t")
        details = [x.strip() for x in details]
        message_details = details[2].split("=")
        details[2] = details[2].split("=")[1]
        structure = {key: value for key, value in zip(
            ["time", "sessionid", message_details[0]], details)}
        data.append(structure)
    print(data)
        
def create_cell():
    pass

def write_json():
    jfile.write('[\n')
    for entry in data:
        jfile.writelines(json.dumps(entry, indent=4))
        jfile.write(",\n")
    jfile.write(']')

if __name__ == "__main__":
    process_data()
    write_json()
    get_messages()