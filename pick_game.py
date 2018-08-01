import json
import random
import os
from internetarchive import search_items


def main():
    chosen_game = None
    games_list_file = "msdoslib.json"
    games_done_file = "done.txt"

    try:
        titles = search_items("collection:(softwarelibrary_msdos_games)", ["title"])
        chosen_game = str(random.choice(titles)) + ",\n"
    except Exception as e:
        print("Could not get most recent list of titles.")
        print(e)
        pass

    if chosen_game is None:
        path_dir = os.path.dirname(os.path.realpath(__file__))
        file_dir = os.path.join(path_dir, games_list_file)
        with open(file_dir) as file:
            file_content = file.read().rstrip("\n")
            json_object = json.loads(file_content)
        titles = json_object['response']['docs']
        chosen_game = str(random.choice(titles)) + ",\n"

    file_path = os.path.join(path_dir,games_done_file)
    with open(file_path, 'a+') as file:
        file.write(str(chosen_game))
    print("Added new title to" + games_done_file)


if __name__ == "__main__":
    main()
