import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

client_id = 'b19960c****437b9fb2e6dbb*****'
client_secret = '3819c29****e689b72b3612239***'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist_data(artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        #print(artist)
        top_tracks = sp.artist_top_tracks(artist['id'])['tracks']
 
        if top_tracks:
            most_popular_track = max(top_tracks, key=lambda track: track['popularity'])
            most_popular_song = most_popular_track['name']
            most_popular_song_popularity = most_popular_track['popularity']
        else:
            most_popular_song = None
            most_popular_song_popularity = None
           
        artist_data = {
            'Artist Name': artist['name'],
            'Followers': artist['followers']['total'],
            'Genres': artist['genres'],
            'Popularity': artist['popularity'],
            'Artist ID': artist['id'],
            'Most Popular Song': most_popular_song,
            'Most Popular Song Popularity': most_popular_song_popularity,

        }
        
        return artist_data
    else:
        return None

artist_names = ['Taylor Swift', 'Beyoncé', 'Selena Gomez', 'Ariana Grande', 'The Weekend', 'Sza', 'Doja Cat', 'Lisa', 'Blackpink', 'Olivia Rodrigo', 'Tyla', 'Rosalia', 'Ed Sheeran', 'Shawn Mendes', 'Shreya Goshal', 'Bella Poarch', 'Rihanna',  'Justin Bieber', 'Dua Lipa', 'Nicki Minaj', 'Cardi B', 'Lady Gaga', 'Zendaya', 'Sabrina Carpenter', 'Jennie', 'Jisoo', 'Britney Spears', 'Shakira', 'Tyga', 'DJ Snake', 'Somi', 'BTS', 'Alan Walker', 'Charlie Puth', 'Megan Thee Stallion', 'Ice Spice', 'One Direction', 'Harry Styles', 'Zayn', 'Miley Cyrus', 'Lizzo', 'Travis Scott', 'Madison Beer', 'Nick Jonas', 'Adele', 'Bruno Mars', 'Chris Brown', 'Akon', 'Arijit Singh', 'Katy Perry', 'Armaan Malik', 'Drake', 'Billie Eilish', 'Spice Girls']  

artist_data_list = []

for artist_name in artist_names:
    artist_data = get_artist_data(artist_name)
    if artist_data:
        artist_data_list.append(artist_data)

df = pd.DataFrame(artist_data_list)

df.to_csv('spotify_artist_data.csv', index=False)

# Print the DataFrame
print(df)
