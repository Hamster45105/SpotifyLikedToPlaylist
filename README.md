# Spotify Liked Songs Converter
Spotify for some reason does not allow you to download your liked songs to your Garmin device. This program is designed to fix that by converting your liked songs into an actual playlist periodically.



## Instructions
1. Clone repo

`git clone https://github.com/TheCodingHamster/Spotify-Liked-Songs-Converter.git`


2. Copy and rename `config.py.example` to `config.py`

`cp cred.py.example cred.py`


3. Update values in file

client_ID - Spotify API Client ID

client_SECRET - Spotify API Client Secret

new_playlist_url - Playlist to convert liked songs into

sleep_interval - Interval for running program (seconds)


4. Install `spotipy`

`pip install spotipy`


5. Run file!

`python3 main.py`