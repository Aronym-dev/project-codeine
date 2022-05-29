# JSON
import json

# Local libraries
import uuid, os
from os import walk

def read_token():
    file = open('utils/config/data.json')
    file = json.load(file)
    for value in file['Authorization'].values():
        return value

        
def read_owners():
    file = open('utils/config/data.json')
    file = json.load(file)
    ids = []
    for value in file['Members'].values():
        ids.append(value)
    return ids


def input_owners(user_id, multiple_owners):
    try:
        file = open('utils/config/data.json')
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        print('Critical error: Config file doesnt exist, please install again the repo from Github')


    if multiple_owners:
        file = open('utils/config/data.json', 'w')
        for owners in range(multiple_owners):
            owner_id = int(input('Insert the owner id: '))
            data['owners'][str(uuid.uuid1())] = owner_id
        json.dump(data, file, indent=4)
        file.close()
        return True
    else:
        file = open('utils/config/data.json', 'w')
        data['Members'][str(uuid.uuid1())] = user_id # User id must to be an int
        json.dump(data, file, indent=4)
        return True
    

def input_token(token):
    try:
        file = open('utils/config/data.json', 'r')
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        print('Critical error: Config file doesnt exist, please install again the repo from Github')

    file = open('utils/config/data.json', 'w')
    data['Authorization']['token'] = token # Token must to be a str
    json.dump(data, file, indent=4)
    return True


def input_data(elements):
    try:
        file = open('utils/config/data.json', 'r')
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        print('Critical error: Config file doesnt exist, please install again the repo from Github')

    file = open('utils/config/data.json', 'w')
    data['Data']['guild_name'] = elements[0]
    data['Data']['channel_name'] = elements[1]
    data['Data']['category_name'] = elements[2]
    data['Data']['emojis_name'] = elements[3]
    data['Data']['admin_name'] = elements[4]
    data['Data']['direct_message_name'] = elements[5]
    data['Data']['nick_name'] = elements[6]
    data['Data']['role_name'] = elements[7]
    data['Data']['spam_message'] = elements[8]
    json.dump(data,file, indent=4)
    file.close()
    return True


def get_data(element):
    path = os.getcwd()
    try:
        file = open('utils/config/data.json', 'r')
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        print('Critical error: Config file doesnt exist, please install again the repo from Github')
        
    return data['Data'][element]
