import json
import re

file_name = 'email.txt'
json_file = 'email.json'
file = open(file_name, "r")
jfile = open(json_file, "w")
data = []
order = ["time", "sessionid", "message"]
message_list = []




def process_data():
    for line in file.readlines():
        details = line.split("\t") 
        details = [x.strip() for x in details]
        message_list.append(details[2])
        
                
        structure = {key:value for key, value in zip(order, details)}
        data.append(structure)
        
def get_messages():
    for item in message_list:
        if 'client=' in item:
            client_list = {'client': (item.replace('client=', ''))}
        if 'from=' in item:
            message_from = {'from': (item.replace('from=', ''))}
        if 'to=' in item:
            message_to = {'to': (item.replace('to=', ''))}
        if 'message-id=' in item:
            message_id = {'messageid': (item.replace('message-id=', ''))}
        if 'status=' in item:
            status = {'status': (item.replace('status=', ''))}
            

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
    # print(sorted(outputlist))