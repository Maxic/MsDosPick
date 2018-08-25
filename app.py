from flask import Flask
from pick_game import GamePicker
from googleapiclient.discovery import build
import json

app = Flask(__name__)


@app.route('/')
def index():

    gp = GamePicker()
    titles = gp.get_titles_from_archive()
    gaem = gp.pick_game(titles)
    modifiedgame = gaem.replace("'", "\"");
    print(modifiedgame)
    game = json.loads(modifiedgame[:len(modifiedgame) - 2])
    query = '\"{}\" {} {}'.format(game['title'], game['year'], "game cover")
    service = build("customsearch", "v1",
                    developerKey="AIzaSyArXnQm_HHdWeuoDGGZWAa4gKVgYWr8Etk")

    res = service.cse().list(
        q=query,
        cx='010406097889422522816:gjtxeosnjrw',
        searchType='image',
        num=1,
        fileType='png',
        safe='off'
    ).execute()

    if not 'items' in res:
        print('No result !!\nres is: {}'.format(res))
    else:
        for item in res['items']:
            img = item['link']
            print('{}:\n\t{}'.format(item['title'], item['link']))

    return "{}\n<img src='{}'>".format(gaem, img)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
