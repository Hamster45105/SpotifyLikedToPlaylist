# Spotify Liked Songs Converter

There are multiple reasons why you would want your liked songs converted into an actual playlist periodically. This program will do that for you.

A good idea would be to set this up on a server that you always have running (eg. Raspberry Pi) and have it automatically run every 5 minutes using cron.
## Instructions

### Spotify Developer Setup

1. Go to the [Spotify developer dashboard](https://developer.spotify.com/dashboard/create) and login
2. Fill in app name and description (can be anything).
3. Set “Redirect URI” to [https://hamster45105.github.io/spotipy] (Make sure there is NO slash at the end!)
4. Click save
5. Click “Settings”. Note down the “Client ID”, click “View client secret” and note that down as well. You need them for the next steps.

### Program Setup

1. Clone repo

`git clone https://github.com/TheCodingHamster/SpotifyLikedToPlaylist.git`

2. Copy and rename `.env.example` to `.env`

3. Update values in file

CLIENT_ID - Spotify API Client ID

CLIENT_SECRET - Spotify API Client Secret

NEW_PLAYLIST_URL - Playlist to convert liked songs into

4. Install PIP requirements

`pip install -r requirements.txt`

5. Run file!

`python3 main.py`

### Using Code
When you run the code for the first time, a message will appear telling you to go to a URL. 

GO TO THIS URL and grant the permissions. 

Then, you will be redirected you to a website with a textbox in the middle. Click the copy to clipboard button. Then, paste the URL into the program. You only have to do this once.
