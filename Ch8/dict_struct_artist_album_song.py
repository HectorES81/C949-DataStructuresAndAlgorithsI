music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

'''First, add a command that adds an artist name to the music dictionary.
Then add commands for adding albums and songs.
Take care to check that an artist exists in the dictionary before adding an album,
and that an album exists before adding a song'''

main_menu_prompt = "Select a number for options below:\n" \
                    "1. Print music db\n" \
                    "2. Add Artist\n" \
                    "3. Add Album\n" \
                    "4. Add Song\n" \
                    "5. Exit\n"
def add_artist():
    artist_name = input("Enter new Artist name: ")
    if(artist_name in music.keys()):
        print("The Artist already exists. Try adding an album for them.")
    else:
        music[artist_name] = {}

def add_album():
    artist_name = input("Enter Artist name: ")
    if(artist_name not in music.keys()):
        print("Artist doesn't exist. Opening menu to add artist...")
        add_artist()
    else:
        album_name = input("Enter album name: ")
        year = input("Enter album year: ")
        plat = bool(input("Enter True/False for Platinum: "))
        if(album_name in music[artist_name].keys()):
            print("Album already exist. Try adding songs to it.")
        else:
            music[artist_name][album_name] = {"songs":[], "year": year, "platinum": plat}

def add_song():
    artist_name = input("Enter Artist name: ")
    album_name = input("Enter Album name: ")
    song_name = input("Enter Song name: ")
    if((artist_name in music.keys()) and (album_name in music[artist_name].keys()) and (song_name not in music[artist_name][album_name]['songs'])):
        music[artist_name][album_name]['songs'].append(song_name)
        print("Addition successful. Songs list is now", music[artist_name][album_name]['songs'])
    else:
        print("Song was not added. One of the items doesnt exist.")


while True:
    user_option = input(main_menu_prompt)
    if(user_option == "1"):
        print(music)
    if(user_option == "2"):
        print("Entering new Artist menu...")
        add_artist()
    if(user_option == "3"):
        print("Entering Album for existing artist...")
        add_album()
    if(user_option == "4"):
        print("Entering new song in album for artist...")
        add_song()
    if(user_option == "5"):
        break
