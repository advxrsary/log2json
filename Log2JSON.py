import json, sys
from itertools import islice, groupby
from datetime import datetime

# Variables declaration 
time_val, session_val, start_val, dur_val, from_val, to_val, status_val, client_val, messageid_val = "", "", "", "", "", "", "", "", ""
data, sidlist = [], []
time = {"start": start_val, "duration": dur_val}
address = {"from": from_val, "to": to_val}
date_format = '%Y-%m-%d %H:%M:%S.%f'
#################################################

# Exception for unspecified files
def throw_unspecified_files():
    try:
        file_name = sys.argv[1]
        file = open(file_name, "r")
    except IndexError:
        print("You did not specify log file")
        sys.exit(1)
    try:
        json_file = sys.argv[2]
        jwfile = open(json_file, "w")
    except IndexError:
        print("You did not specify output file")
        sys.exit(1)
# Sort by sessionid key
def key_func(k):
    return k['sessionid']

# Data processor, takes each line of the log,
# from each line takes values from each row
# from the third row takes the part before sign
# of equality as a key and after as a value for this key.
# zips all values and creates list of dictionaries.
# returns the list
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

# The function to convert log to json
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

    # Sorts and groups the datalist by session id
    for key, value in groupby(datalist, key_func):
        sidlist.append(list(value))

    # Transforms processed data into serializable format
    # and writes it to .json file
    jwfile.write("[")
    for item in sidlist:
        jwfile.write('\n')
        for i in item:
            event['sessionid'] = i['sessionid']
            match i:
                case 'client':
                    event['client'] = i['client']
                case 'status':
                    event['status'] = i['status']
                case 'from':
                    eadrs['from'] = i['from']
                case 'to':
                    eadrs['to'] = i['to']
                case 'message-id':
                    event['messageid'] = i['message-id']

        jwfile.write(json.dumps(event, indent=4))
        jwfile.write(",")
    jwfile.write("]")

# Main func
if __name__ == "__main__":
    throw_unspecified_files()
    create_event()


