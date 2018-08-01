import json
import random
import os
from internetarchive import search_items

try:
    titles = search_items("collection:(softwarelibrary_msdos_games)", ["title"])
except Exception as e:
    print("Could not get most recent list of titles.")
    pass

if not titles:
    path_dir = os.path.dirname(os.path.realpath(__file__))
    file_dir = path_dir + "\msdoslib.json"
    with open(file_dir) as file:
        file_content = file.read().rstrip("\n")
        json_object = json.loads(file_content)
    titles = json_object['response']['docs']

chosen_game = str(random.choice(titles)) + ",\n"

with open(path_dir + "/done.txt", 'a+') as file:
    file.write(str(chosen_game))
