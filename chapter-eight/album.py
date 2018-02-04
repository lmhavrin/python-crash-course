# Exercise 8-7: Album

def make_album(artist, title, tracks=0):
    album = {
        "artist": artist.title(),
        "title": title.title()
        }
    if tracks:
        album["tracks"] = tracks
    return album

album_one = make_album("Johnny Cash", "At Folsom Prison")
album_two = make_album("Jeff Buckley", "Grace")
album_three = make_album("Elvis Presley", "Elvis the King", tracks=51)

print(album_one)
print(album_two)
print(album_three)
