# Exercise 8-8: Albums
def make_album(artist, title, tracks=0):
    album = {
        "artist": artist.title(),
        "title": title.title()
        }
    if tracks:
        album["tracks"] = tracks
    return album

while True:
    artist = input("Enter artists name; Press 'q' to quit ")
    if artist == "q":
        break
    title = input("Enter album title; Press 'q' to quit ")
    if title == "q":
        break
    tracks = input("Enter number of tracks; Press 'q' to quit ")
    if tracks == "q":
        break

    print(make_album(artist, title, tracks))
