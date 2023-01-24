import azapi

API = azapi.AZlyrics('google', accuracy=0.5)


def song():
    song_name = input("Enter a song name: ")
    return song_name


def singer():
    singer_name = input("Enter a singer name: ")
    return singer_name


API.artist = singer()
API.title = song()

API.getLyrics(save=True, ext='lrc')

print(API.lyrics)
print(API.title, API.artist)
