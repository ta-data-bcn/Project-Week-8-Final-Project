import spotipy
import spotipy.util as util
# import simplejson as json
import pprint
import pandas as pd
username = 'nerken'
scope = 'user-follow-read,user-follow-modify,user-read-recently-played,user-top-read,user-library-read,user-library-modify,user-read-playback-state,user-read-currently-playing,user-modify-playback-state,playlist-read-collaborative,playlist-modify-private,playlist-modify-public,playlist-read-private,app-remote-control,user-read-email,user-read-private'

client_id = '22e782a724264812b124038bbf783396'
client_secret = '6219554f45764f2cbfe13306ec476f10'
token2 = util.oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
token = util.prompt_for_user_token(username, scope=scope, client_id='22e782a724264812b124038bbf783396', client_secret='6219554f45764f2cbfe13306ec476f10', redirect_uri='https://localhost:8080')

