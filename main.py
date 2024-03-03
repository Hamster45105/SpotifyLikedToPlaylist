import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
import requests
import dotenv
import os

def check_connection(timeout):
    try:
        requests.head("https://github.com/", timeout=timeout)
        return True

    except requests.ConnectionError:
        return False

def is_spotify_playlist_url(url):
    pattern = r'^https?://open\.spotify\.com/playlist/[a-zA-Z0-9?=]+$'
    return bool(re.match(pattern, url))

# Load settings using DOTenv
dotenv.load_dotenv(".env")

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = "https://hamster45105.github.io/spotipy"
new_playlist_url = os.getenv("NEW_PLAYLIST_URL")

# Check if playlist valid
playlist_check = is_spotify_playlist_url(new_playlist_url)
if playlist_check == False:
    print("The playlist URL you entered is not valid. Please enter a valid playlist URL.")
    exit()

scope = ['user-library-read', 'playlist-read-private', 'playlist-modify-private', 'playlist-read-collaborative' ]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, open_browser=False))

try:
    internet_result = check_connection(5)
    if internet_result == False:
        raise Exception("Internet connection check failed")
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

except Exception as e:
    print("An error occurred: " + str(e))
