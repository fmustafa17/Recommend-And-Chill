# Paakwesi Quansah & Farhana Mustafa
# Recommend and Chill

import sys
import spotipy
import spotipy.util as util
import pprint
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

##Setup the credentials for the plotly api
plotly.tools.set_credentials_file(username='fmustafa', api_key='GOONjTIIO6Ojdj2Ajwjq')
plotly.tools.set_config_file(world_readable=True,
                             sharing='public')

scope = 'user-top-read'

##Setup the credentials for the spotify api
SPOTIPY_CLIENT_ID = '20ade96a400f45db97710275c3ce7158'
SPOTIPY_CLIENT_SECRET = 'fd0a74f3ab6f47b9be375a6f1cf43f95'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

#sets the username for the user to be used
username = 'fmustafa17'

token = util.prompt_for_user_token(username, scope,SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)

##This function gets the artist id for the certain artist
def get_artist(name):
    sp = spotipy.Spotify(auth=token)
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

##Shows the song recommendations for a certain artist
def show_recommendations_for_artist(artist):
    sp = spotipy.Spotify(auth=token)
    albums = []
    songList = []
    trackName = []
    results = sp.recommendations(seed_artists = [artist['id']])
    for track in results['tracks']:
        print track['name'], '-', track['artists'][0]['name']
        songList.append(track['popularity'])
        trackName.append(track['name'])
    return songList,trackName

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name'])

dict = {}
list = []
#list = ['Drake','Kanye West', 'Future','Migos', 'Taylor Swift']
popNum = []
trackName = []
popNum2 = []
trackName2 = []
##flatPopNum = []
xAxis = range(1,101)
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ##sets the time range for the artist to long range
    results = sp.current_user_top_artists(time_range='long_term', limit=5)
    for i, item in enumerate(results['items']):
        list.append(item['name'])
    print list
    print
    for j in list:
        artist = get_artist(j)
        if artist:
            popNum, trackName = show_recommendations_for_artist(artist)
            popNum2.append(popNum)
            trackName2.append(trackName)
            
##    flatPopNum = [item for sublist in popNum for item in sublist]
    xVal = xAxis
    yVal = popNum2
    artistName = list
    songName = trackName2

    # Create a trace
    trace0 = go.Scatter(
        x = xAxis,
        y = yVal[0],
        mode = 'lines+markers',
        text = songName[0],
        name = artistName[0]
    )
    trace1 = go.Scatter(
        x = xAxis,
        y = yVal[1],
        mode = 'lines+markers',
        text = songName[1],
        name = artistName[1]
    )
    trace2 = go.Scatter(
        x = xAxis,
        y = yVal[2],
        mode = 'lines+markers',
        text = songName[2],
        name = artistName[2]
    )
    trace3 = go.Scatter(
        x = xAxis,
        y = yVal[3],
        mode = 'lines+markers',
        text = songName[3],
        name = artistName[3]
    )
    trace4 = go.Scatter(
        x = xAxis,
        y = yVal[4],
        mode = 'lines+markers',
        text = songName[4],
        name = artistName[4]
    )

    data = [trace0, trace1, trace2, trace3, trace4]

    layout = go.Layout(
        title='Music Taste of User Based on Top 5 Most Listened To Artists'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='hover-chart-basic')
##
##    plot_url = py.plot(data, filename='basic-line')
    
else:
    print("Can't get token for", username)
