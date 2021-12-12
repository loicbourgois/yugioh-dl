import os
import re
import requests
import sys
import time
decks = [
    # '2002-starter-deck-kaiba.py',
    # '2002-starter-deck-yugi.py',
    # '2003-starter-deck-joey.py',
    # '2003-starter-deck-pegasus.py',
    # '2004-starter-deck-yugi-evolution.py',
    '2004-starter-deck-kaiba-evolution.py'
]
replacements = {
     ' ': '%20',
    '&': '%26',
    ',': '%2C',
    '#': '%23',
}
for deck in decks:
    deck_short = deck.replace(".py", "")
    with open(f"decks/{deck}", "r") as file:
        os.system(f"mkdir -p ./images/{deck_short}")
        for x in file:
            name = x.strip()
            if name.startswith("#"):
                continue
            time.sleep(2)
            for k,v in replacements.items():
                x = x.replace(k,v)
            x = x.split(' (Updated from')[0]
            url = f"https://db.ygoprodeck.com/card/?search={x}"
            r = requests.get(url)
            assert r
            secure_urls = []
            for line in str(r.content).split("\\n"):
                if re.search("secure_url", line):
                    secure_urls.append( line.split('"')[3] )
            if len(secure_urls) != 1:
                print(f"[ error ] {name} invalid secure urls count")
                continue
            if 'card_db_twitter_Card2' in secure_urls[0]:
                print(f"[ error ] {name} {secure_urls[0]} {url}")
                continue
            r = requests.get(secure_urls[0])
            assert r
            file = open(f"images/{deck_short}/{name}.jpg", "wb")
            file.write(r.content)
            file.close()
            print(f"[success] {name} {secure_urls[0]}")
