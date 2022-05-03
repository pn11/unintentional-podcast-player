import argparse
import json

import opml


def main(args=None):
    opml_name = 'shows.opml'
    json_name  = 'shows.json'
    outline = opml.parse(opml_name)
    shows = []
    for o in outline:
        shows.append({
            'id': o.title,
            'rss': o.xmlUrl
        })
    if json_name[-5:] != '.json':
        json_name += '.json'
    json.dump(shows, open(json_name, 'w'), ensure_ascii=False)
    

if __name__ == '__main__':
    main()