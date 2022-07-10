import json
from itertools import islice, groupby
from jsoncomment import JsonComment
from datetime import datetime

time_val, session_val, start_val, dur_val, from_val, to_val, status_val, client_val, messageid_val = "", "", "", "", "", "", "", "", ""
file_name = 'email.txt'
json_file = 'output.json'
file = open(file_name, "r")
jrfile = open(json_file, "r")
jwfile = open(json_file, "w")
data, sidlist = [], []
time = {"start": start_val, "duration": dur_val}
address = {"from": from_val, "to": to_val}
date_format = '%Y-%m-%d %H:%M:%S.%f'


def key_func(k):
    return k['sessionid']

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
    event = {"time": time,
             "sessionid": session_val,
             "client": client_val,
             "messageid": messageid_val,
             "address": address,
             "status": status_val}

    etime = event['time']
    eadrs = event['address']
    datalist = process_data()
    datalist = sorted(datalist, key=key_func)
    eventdict = []
    
    for key, value in groupby(datalist, key_func):
        sidlist.append(list(value))
    
    jwfile.write("[")
    for item in sidlist:
        jwfile.write('\n')
        for i in item:
            x =+ 1
            event['sessionid'] = i['sessionid']
            if 'client' in i:
                event['client'] = i['client']
            if 'status' in i:
                event['status'] = i['status']
            if 'from' in i:
                eadrs['from'] = i['from']
            if 'to' in i:
                eadrs['to'] = i['to']
            if 'message-id' in i:
                event['messageid'] = i['message-id']
        
        jwfile.write(json.dumps(event, indent=4))
        jwfile.write(",")
    jwfile.write("]")


if __name__ == "__main__":
    create_event()
    
    
