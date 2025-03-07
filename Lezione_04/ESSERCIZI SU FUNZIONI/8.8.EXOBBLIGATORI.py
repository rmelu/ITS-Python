def make_album(artist_name, album_title, num_tracks=None):
#COSTRUSCE UN DIZIONARIO CHE DESCRIVE UN ALBUM MUSICALE
    album = {
        'artist': artist_name,
        'title': album_title,
    }
    if num_tracks:
        album['traks'] = num_tracks
    return album

#CICLO WHILE PER L'INPUT DELL'UTENTE
while True:
    album:dict[str,str,int] = {}
    print("\nVuoi inserire le informazioni sull'album? sè si continua, altrimenti basta clicare no! ")
    artist = input("Nome dell'artista: ")
    if artist.lower() == 'no':
        break
    title = input("Titolo dell'album: ")
    if title.lower() == 'no':
        break
    tracks = input("Numero di brani (opzionale premi 'no' per saltare questo passaggio): ")
    
    #CREA IL DIZIONARIO DELL'ALBUM
    if tracks.lower() == 'no':
        album = make_album(artist, title)
        
    else:
        album = make_album(artist, title, int(tracks))

    #STAMPA IL DIZIONARIO
    print(album)