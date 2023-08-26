import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import requests
import json

def check_connection(timeout):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


with open('config.json') as f:
    settings = json.load(f)

client_id = settings['CLIENT_ID']
client_secret = settings['CLIENT_SECRET']
redirect_uri = "https://hamster45105.github.io/Spotify-Liked-Songs-Converter/"
new_playlist_url = settings['NEW_PLAYLIST_URL']
sleep_interval = settings['SLEEP_INTERVAL']

if client_id == "" or client_secret == "" or redirect_uri == "" or new_playlist_url == "" or sleep_interval == "":
    print("Please fill out all fields in config.json")
    exit()

scope = ['user-library-read', 'playlist-read-private', 'playlist-modify-private']
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
        sleep(int(sleep_interval))

    except Exception as e:
        # Becuase the program goes on a loop, if an error occurs it will log and keep going in case it is just a once off connection error or something similar.
        print(f"An unknown error occurred: " + str(e))
        continue