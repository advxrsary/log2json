#!/usr/bin/env python3
__author__ = 'Sevastian Zare (@advxrsary)'
__date__ = '20220710'
__license__ = 'MIT'
__version__ = '1.00'
__description__ = """
                  Processes data from a log file and converts it to 
                  json serialized file. 
                  """


import json, sys
from itertools import islice, groupby
from datetime import datetime
from termcolor import colored

# Global variables declaration 
time_val, session_val, start_val, dur_val, from_val, to_val, status_val, client_val, messageid_val = "", "", "", "", "", "", "", "", ""
data, sidlist, datelist = [], [], []
time = {"start": start_val, "duration": dur_val}
address = {"from": from_val, "to": to_val}

# Divide one list into two, the second is ahead of the first 
# by one step
def seq_pairs(li):
    return zip(li, islice(li, 1, None))

# Processes each row; from the third row takes <key>=<value>
# returns a datalist
def process_data(file2process):
    print(colored('\n[*]', 'yellow'), "Processing data...")
    file = open(file2process, "r")
    for line in file.readlines():
        details = line.split("\t")
        details = [x.strip() for x in details]
        message_details = details[2].split("=")
        details[2] = details[2].split("=")[1]
        structure = {key: value for key, value in zip(
            ["start", "sessionid", message_details[0]], details)}
        data.append(structure)
    return data


# Calculates duration of a single event
def calc_duration(data2calc):
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    data_old = seq_pairs(data2calc)
    new_data = []
    for list1, list2 in data_old:
        start = datetime.strptime(list1['start'].replace("T", ' '), date_format)
        end = datetime.strptime(list2['start'].replace("T", ' '), date_format)
        duration = str(end - start)
        list1['duration'] = duration
        new_data.append(list1)
    return(new_data)


# Sorts and groups the datalist by session id
def sort_by_sid(data2sort):
    sorted_data = sorted(data2sort, key=key_func)
    for key, value in groupby(sorted_data, key_func):
        sidlist.append(list(value))
    return sidlist
# Return sessionid val from dict
def key_func(k):
    return k['sessionid']

# Transforms processed data into serializable format
# and writes it to .json file
def write_file(file):
    processed_data = process_data(file) 
    sorted_data = sort_by_sid(calc_duration(processed_data))
    event = {"time": time,
             "sessionid": session_val,
             "client": client_val,
             "messageid": messageid_val,
             "address": address,
             "status": status_val}
    etime = event['time']
    eadrs = event['address']
    print(colored('[*]', 'yellow'), "Creating event...")

    # Write the file
    jwfile = open(json_file, "w")
    jwfile.write("[")
    for item in sorted_data:
        jwfile.write('\n')
        for i in item:
            event['sessionid'] = i['sessionid']
            etime['start'] = i['start']
            etime['duration'] = i['duration']
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
        jwfile.write(f"{json.dumps(event, indent=4)},")
    jwfile.write("]")


# Self-execution
if __name__ == "__main__":
    # Exception
    print('''  _             ____   _                 
 | | ___   __ _|___ \ (_)___  ___  _ __  
 | |/ _ \ / _` | __) || / __|/ _ \| '_ \ 
 | | (_) | (_| |/ __/ | \__ \ (_) | | | |
 |_|\___/ \__, |_____|/ |___/\___/|_| |_|
          |___/     |__/     by advxrs4ry''')
    try:
        file_name = sys.argv[1]
    except IndexError:
        print(colored('\n[#]', 'red'), "Specify log file!")
        print(colored('[#]', 'red'), "Specify output file!")
        sys.exit(1)
    try:
        json_file = sys.argv[2]
    except IndexError:
        print(colored('\n[#]', 'red'), "Specify output file!")
        sys.exit(1)

    # Main func
    write_file(file_name)

    # Fancy output
    
    print(colored('[+]', 'green'), "Done!")
    print(colored('[+]', 'green'), f"Results: {json_file}")
    print(colored('[:]', 'white'),
          colored('To fix the comma run:', 'white'))
    print(colored('[:]', 'white'),
          colored(f'python3 fix_comma.py {json_file}', 'cyan'))