from time import sleep
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import re

def check_connection(timeout):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

def is_spotify_playlist_url(url):
    pattern = r'^https?://open\.spotify\.com/playlist/[a-zA-Z0-9?=]+$'
    return bool(re.match(pattern, url))

with open('config.json', encoding='utf-8') as f:
    settings = json.load(f)

with open('config_example.json', encoding='utf-8') as f:
    default_settings = json.load(f)

# Add any additional settings or remove any ones taken away

required_settings = []
deleted_settings = []

for item in default_settings:
    if item not in settings:
        required_settings.append(item)

if len(required_settings) > 0:
    for item in required_settings:
        settings.update({item: default_settings[item]})

for item in settings:
    if item not in default_settings:
        deleted_settings.append(item)

if len(deleted_settings) > 0:
    for item in deleted_settings:
        del settings[item]

with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(settings, f, indent=4)

client_id = settings['CLIENT_ID']
client_secret = settings['CLIENT_SECRET']
redirect_uri = "https://hamster45105.github.io/spotipy"
new_playlist_url = settings['NEW_PLAYLIST_URL']
sleep_interval = settings['SLEEP_INTERVAL']
playlist_private = settings['READ_PRIVATE']
playlist_collab = settings['READ_COLLABORATIVE']

# Settings check
stop = False

# Check if empty
for key, value in settings.items():
    if not value:
        print(f"The value for {key} is empty. Please fill in.")
        stop = True

# Check if valid
playlist_check = is_spotify_playlist_url(new_playlist_url)
if playlist_check == False:
    print("The playlist URL you entered is not valid. Please enter a valid playlist URL.")
    stop = True

try:
    sleep_interval = int(sleep_interval)
except ValueError:
    print("The sleep interval you entered is not valid. Please enter a valid integer.")
    stop = True

if playlist_private.lower() == "true":
    playlist_private = True
elif playlist_private.lower() == "false":
    playlist_private = False
else:
    print("The playlist private setting you entered is not valid. Please enter either True or False.")
    stop = True

if playlist_collab.lower() == "true":
    playlist_collab = True
elif playlist_collab.lower() == "false":
    playlist_collab = False
else:
    print("The playlist collaborative setting you entered is not valid. Please enter either True or False")
    stop = True

if stop == True:
    exit()

scope = ['user-library-read']

if playlist_private:
    scope.append('playlist-read-private')
    scope.append('playlist-modify-private')
if playlist_collab:
    scope.append('playlist-read-collaborative')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, open_browser=False))


while True:
    try:
        internet_result = check_connection(5)
        if internet_result == True:
            #Get items currently in PLAYLIST
            tracks_playlist = sp.user_playlist_tracks(playlist_id=new_playlist_url)

            tracks_playlist_items = []

            counter = 0
            for items in tracks_playlist['items']:
                counter = counter + 1
                tracks_playlist_items.append(tracks_playlist['items'][counter - 1]['track']['id'])

            #Get items currently in LIKES
            liked_songs = []
            offset = 0
            limit = 50

            while True:
                results = sp.current_user_saved_tracks(limit=limit, offset=offset)
                items = results['items']
                liked_songs.extend(items)
                if len(items) < limit:
                    break
                offset += limit

            tracks_liked_items = []

            for track in liked_songs:
                tracks_liked_items.append((track['track']['id']))

            #Add items
            if tracks_liked_items != tracks_playlist_items:
                for item in tracks_playlist_items:
                    if item not in tracks_liked_items:
                        sp.user_playlist_remove_all_occurrences_of_tracks(user=sp.current_user(), playlist_id=new_playlist_url, tracks=[item])
                for item in tracks_liked_items:
                    if item not in tracks_playlist_items:
                        sp.playlist_add_items(playlist_id=new_playlist_url, items=[item], position=0)
        sleep(sleep_interval)

    except Exception as e:
        # Becuase the program goes on a loop, if an error occurs it will log and keep going in case it is just a once off connection error or something similar.
        print("An unknown error occurred: " + str(e))
        continue
