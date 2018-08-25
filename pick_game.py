import json
import random
import os
from internetarchive import search_items


class GamePicker:
    def old(self):
        games_list_file = "msdoslib.json"
        games_done_file = "done.txt"
        path_dir = os.path.dirname(os.path.realpath(__file__))

        titles = search_items("collection:(softwarelibrary_msdos_games)", ["title", "year"])

        chosen_game1 = self.pick_game(games_list_file, path_dir, titles)
        chosen_game2 = self.pick_game(games_list_file, path_dir, titles)
        chosen_game3 = self.pick_game(games_list_file, path_dir, titles)

        file_path = os.path.join(path_dir, games_done_file)

        with open(file_path, 'a+') as file:
            file.write(str(chosen_game1))
            file.write(str(chosen_game2))
            file.write(str(chosen_game3) + "\n")
        print("Added new title to " + games_done_file)

    def get_titles_from_archive(self):
        titles = search_items("collection:(softwarelibrary_msdos_games)", ["title","year"])
        return titles

    def pick_game(self, titles):
        try:
            chosen_game = str(random.choice(list(titles))) + ",\n"
        except Exception as e:
            print("Could not get most recent list of titles.")
            print(e)
            return None

        return chosen_game

    def pick_game_old(self, games_list_file, path_dir, titles):
        chosen_game = None

        try:
            chosen_game = str(random.choice(list(titles))) + ",\n"
        except Exception as e:
            print("Could not get most recent list of titles.")
            print(e)
            pass
        if chosen_game is None:
            file_dir = os.path.join(path_dir, games_list_file)
            with open(file_dir) as file:
                file_content = file.read().rstrip("\n")
                json_object = json.loads(file_content)
            titles = json_object['response']['docs']
            chosen_game = str(random.choice(titles)) + ",\n"

        return chosen_game


