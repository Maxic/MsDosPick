import json
import random
from internetarchive import search_items


def main():
    games_done_file = "done.json"

    with open(games_done_file, "r+") as file:
        games_done_data = json.load(file)
        chosen_games = pick_game(3, games_done_data)
        for game in chosen_games:
            game['link'] = "https://archive.org/details/" + game['identifier']
            del game['identifier']
            games_done_data['games'].append(game)
        file.seek(0)
        file.truncate()
        file.write(json.dumps(games_done_data))


def is_duplicate(game_done_data, new_game):
    for game in game_done_data['games']:
        if game['title'] == new_game['title']:
            return True
    return False


def pick_game(game_amount, game_done_data):
    chosen_games = []

    try:
        # get all (filtered) msdos titles from archive.org
        titles = list(search_items("collection:(softwarelibrary_msdos_games) AND"
                                   " -identifier:(agi_*) AND -identifier:(agt_*) AND"
                                   " -identifier:(sci_*) AND -identifier:(gamemaker_*) AND"
                                   " -identifier:(game-maker_*)",
                                   ["title", "identifier"]))
        for _ in range(game_amount):
            new_game = random.choice(titles)
            while is_duplicate(game_done_data, new_game):
                new_game = random.choice(titles)
            chosen_games.append(new_game)
            print("Added game: " + new_game['title'] + " to the file")
    except Exception as e:
        print("Something went wrong: " + e)
    return chosen_games


if __name__ == "__main__":
    main()
