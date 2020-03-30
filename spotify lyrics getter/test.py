import sys
import requests
import spotipy
import spotipy.util as util
from config.config import USERNAME, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from bs4 import BeautifulSoup

scope = 'user-read-currently-playing'

token = util.prompt_for_user_token(USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

if token:
    # create am instance for our token
    sp = spotipy.Spotify(auth=token)
    # geting the current song playing from the instance
    current_song = sp.currently_playing()
    # getting the artist from the current song
    artist = current_song['item']['artists'][0]['name']
    # name of the current song
    song_name = current_song['item']['name']
    # getting the proper url using web scrapping
    song_url = '{}-{}-lyrics'.format(str(artist).strip().replace(' ', '-'), str(song_name).strip().replace(' ', '-'))
    print(song_url)
    # print('\nSong: {}\nArtist: {}'.format(song_name, artist))
    request = requests.get("https://genius.com/{}".format(song_url))

    if request.status_code == 200:
        # BeautifulSoup library return an html code
        html_code = BeautifulSoup(request.text, features="html.parser")
        # Extract lyrics from beautifulsoup response using the correct prefix {"class": "lyrics"}
        lyrics = html_code.find("div", {"class": "lyrics"}).get_text()
        print(lyrics)

    else:
        print("Sorry, I can't find the actual song")

    
else:
    print("Can't get token for", USERNAME)