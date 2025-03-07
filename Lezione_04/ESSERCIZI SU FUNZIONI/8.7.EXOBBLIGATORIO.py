def make_album(artist_name, album_title, num_traks=None):
#COSTRUSCE UN DIZIONARIO CHE DESCRIVE UN ALBUM MUSICALE
    album = {
        'artist': artist_name,
        'title': album_title,
    }
    if num_traks:
        album['traks'] = num_traks
    return album
#CREAZIONE DI TRE DIZIONARI CHE RAPPRESENTANO ALBUM
album1 = make_album("Artista1", "Album1")
album2 = make_album("Artista2", "Album2")
album3 = make_album("Artista3", "Album3", 12) #INCLUDE IL NUMERO DI BRANI
#STAMPA DEI DIZIONARI
print(album1)
print(album2)
print(album3)
