import json
from itertools import islice
from datetime import datetime

time_val, session_val, start_val, dur_val, from_val, to_val, status_val, client_val, messageid_val = "", "", "", "", "", "", "", "", ""
file_name = 'email.txt'
json_file = 'output.json'
file = open(file_name, "r")
jfile = open(json_file, "w")
data, newdata, message_list, sidlist = [], [], [], []
new_message_list, final_dict = {}, {}
time = {"start": start_val, "duration": dur_val}
address = {"from", "to"}
message_outs = ["status", "client", "message-id"]
date_format = '%Y-%m-%d %H:%M:%S.%f'


def seq_pairs(li):
    return zip(li, islice(li, 1, None))

def find_sid(dictionary2look):
    for dict in dictionary2look:
        sidlist.append(dict['sessionid'])
    return(list(dict.fromkeys(sidlist)))

def process_data():
    for line in file.readlines():
        details = line.split("\t")
        details = [x.strip() for x in details]
        message_details = details[2].split("=")
        sessid = details[1]
        details[2] = details[2].split("=")[1]
        structure = {key: value for key, value in zip(
            ["start", "sessionid", message_details[0]], details)}
        data.append(structure)
    return data

def create_event():
    event = { "time":time, 
        "sessionid":session_val, 
        "client":client_val, 
        "messageid":messageid_val, 
        "address":address, 
        "status":status_val }
    
    etime = event['time']
    eadrs = event['address']
    datalist = process_data()
    divided_list = seq_pairs(datalist)
    found_sids = find_sid(datalist)
    iter_sids = iter(found_sids)
    
    for list1, list2 in divided_list:
        nextsid = iter_sids.__next__()
        start = datetime.strptime(list1['start'].replace("T", ' '), date_format)
        end = datetime.strptime(list2['start'].replace("T", ' '), date_format)
        if list1['sessionid'] == nextsid:
            print(list1['sessionid'])
        

def write_json():
    jfile.write('[\n')
    for entry in process_data():
        jfile.writelines(json.dumps(entry))
        jfile.write(",\n")
    jfile.write(']')
    print(entry)

if __name__ == "__main__":
    create_event()