# Spotify Liked Songs Converter

There is multiple reasons why you would want your liked songs converted into an actual playlist periodically. This program is designed to help you with that.

## Instructions

### Spotify Developer Setup

1. Go to the [Spotify developer dashboard](https://developer.spotify.com/dashboard/create) and login


4. Fill in app name and description (can be anything). Then set “Redirect URI” to “https://hamster45105.github.io/spotipy/”


5. Click save


6. Click “Settings”. Note down the “Client ID”, click “View client secret” and note that down as well. You need them for the next steps.

### Program Setup

1. Clone repo

`git clone https://github.com/TheCodingHamster/SpotifyLikedToPlaylist.git`


2. Copy and rename `config_example.json` to `config.json`


3. Update values in file

CLIENT_ID - Spotify API Client ID

CLIENT_SECRET - Spotify API Client Secret

NEW_PLAYLIST_URL - Playlist to convert liked songs into

SLEEP_INTERVAL - Interval for running program (seconds)


4. Install PIP requirements

`pip install -r requirements.txt`


5. Run file!

`python3 main.py`


### Using Code
After you run the code, the first time a message will appear telling you to go to a URL and enter the URL you are directed to. GO TO THIS URL and grant the permissions. Then, it will redirect you to a website with a textbox in the middle. Click the copy to clipboard button. Then, paste the URL into the correct spot in the program. Now the program will run. You do not have to do this step every time, only the first.