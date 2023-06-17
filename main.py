import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
from time import sleep
import requests

def check_connection(timeout):
    try:
        requests.head("http://www.example.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    

scope = ['user-library-read', 'playlist-read-private', 'playlist-modify-private']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope, open_browser=False))

while True:
    internet_result = check_connection(1)
    if internet_result == True:
        #Get items currently in PLAYLIST
        tracks_playlist = sp.user_playlist_tracks(playlist_id=cred.new_playlist_url)

        tracks_playlist_items = []

        counter = 0
        for items in tracks_playlist['items']:
            counter = counter + 1
            tracks_playlist_items.append(tracks_playlist['items'][counter - 1]['track']['id'])

        #Get items currently in LIKES

        #First 50 tracks
        results = sp.current_user_saved_tracks(limit=50)
        liked_songs = results['items']

        # Keep requesting tracks until there are none left
        while results['next']:
            results = sp.next(results)
            liked_songs.extend(results['items'])

        # Extract the track names and IDs and add them to a list
        tracks_liked_items = []
        for track in liked_songs:
            tracks_liked_items.append((track['track']['id']))

        #Add items
        if tracks_liked_items != tracks_playlist_items:
            for item in tracks_playlist_items:
                if item not in tracks_liked_items:
                    sp.user_playlist_remove_all_occurrences_of_tracks(user=sp.current_user(), playlist_id=cred.new_playlist_url, tracks=[item])
            for item in tracks_liked_items:
                if item not in tracks_playlist_items:
                    sp.playlist_add_items(playlist_id=cred.new_playlist_url, items=[item], position=0)

    sleep(60)
