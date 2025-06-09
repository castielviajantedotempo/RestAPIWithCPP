import json

def get_status():
    # Open and read the JSON file
    with open('ref.json', 'r') as file:
        local_file = json.load(file)
    file.close()
    #print(local_file["status"])
    return local_file["status"]
