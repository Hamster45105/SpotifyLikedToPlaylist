# Spotify Liked Songs Converter

There is multiple reasons why you would want your liked songs converted into an actual playlist periodically. This program is designed to help you with that.

## Instructions

### Spotify Developer Setup

1. Go to the [Spotify developer dashboard](https://developer.spotify.com/dashboard/create) and login


4. Fill in app name and description (can be anything). Then set “Redirect URI” to “http://localhost”


5. Click save


6. Click “Settings”. Note down the “Client ID”, click “View client secret” and note that down as well. You need them for the next steps.

### Program Setup

1. Clone repo

`git clone https://github.com/TheCodingHamster/Spotify-Liked-Songs-Converter.git`


2. Copy and rename `config.py.example` to `config.py`


3. Update values in file

client_ID - Spotify API Client ID

client_SECRET - Spotify API Client Secret

new_playlist_url - Playlist to convert liked songs into

sleep_interval - Interval for running program (seconds)


4. Install `spotipy`

`pip install spotipy`


5. Run file!

`python3 main.py`


### Using Code
After you run the code, the first time a message will appear telling you to go to a URL and enter the URL you are directed to. GO TO THIS URL and grant the permissions. Then, it will redirect you to a website that DOSEN’T EXIST, for example “https://localhost/callback/***”. Copy this URL and paste it into the correct spot in the program. Now the program will run. You do not have to do this step every time, only the first.