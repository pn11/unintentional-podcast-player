import argparse
import json
import socket
import urllib.error
import urllib.request

import podcastparser


def parse(feed):
    parsed = podcastparser.parse(feed, urllib.request.urlopen(feed))
    episodes = parsed['episodes']
    return sorted(episodes, key=lambda x: x['published'])



def main(args=None):
    episodes = {}
    shows = json.load(open('shows.json'))
    for show in shows:
        try:
            parsed = podcastparser.parse(show['rss'], urllib.request.urlopen(show['rss'], timeout=1))
            episodes[show['id']] = {
                'rss': show['rss'],
                'episodes': parsed['episodes']
            }
        except socket.timeout:
            print('Timeout.', show)
        except podcastparser.FeedParseError:
            print('FeedParseError', show)
        except urllib.error.HTTPError:
            print('HTTPError', show)
        except urllib.error.URLError:
            print('HTTPError', show)

    json.dump(episodes, open('episodes.json', 'w'), ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()