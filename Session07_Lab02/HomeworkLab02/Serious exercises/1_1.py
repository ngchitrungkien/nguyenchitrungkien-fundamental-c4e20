import pyexcel

itunes_top_50_songs = [
    {
        "Artist": "Drake",
        "Song's name": "In My Feelings"
    },
    {
         "Artist": "Maroon 5",
        "Song's name": "Girls Like You (feat. Cardi B)"
    },
    {
         "Artist": "Kane Brown",
        "Song's name": "Weekend"
    },
    {
        "Artist": "Cardi B, Bad Bunny & J Balvin",
        "Song's name": "I Like It"
    },
    {
        "Artist": "5 Seconds of Summer",
        "Song's name": "Youngblood"
    },
    {
        "Artist": "Post Malone",
        "Song's name": "Better Now"
    },
    {
        "Artist": "Imagine Dragons",
        "Song's name": "Natural"
    },
    {
        "Artist": "Drake",
        "Song's name": "In My Feelings"
    },
    {
        "Artist": "Travis Scott",
        "Song's name": "SICKO MODE"
    },
    {
        "Artist": "Lauren Daigle",
        "Song's name": "You Say"
    },
    {
        "Artist": "Florida Georgia Line",
        "Song's name": "Simple"
    },
    {
        "Artist": "6ix9ine",
        "Song's name": "FEFE (feat. Nicki Minaj & Murda Beatz)"
    },
    {
        "Artist": "Brett Young",
        "Song's name": "Mercy"
    },
    {
        "Artist": "Bazzi",
        "Song's name": "Beautiful (feat. Camila Cabello)"
    },
    {
        "Artist": "Khalid & Normani",
        "Song's name": "Love Lies"
    },
    {
        "Artist": "Juice WRLD",
        "Song's name": "Lucid Dreams"
    },
    {
        "Artist": "Imagine Dragons",
        "Song's name": "Whatever It Takes"
    },
    {
        "Artist": "DJ Khaled",
        "Song's name": "No Brainer (feat. Justin Bieber, Chance the Rapper & Quavo)"
    },
    {
        "Artist": "Tyga",
        "Song's name": "Taste (feat. Offset)"
    },
    {
        "Artist": "Kenny Chesney",
        "Song's name": "Get Along"
    },
    {
        "Artist": "Jason Aldean",
        "Song's name": "Drowns the Whiskey (feat. Miranda Lambert)"
    },
    {
        "Artist": "Weezer",
        "Song's name": "Africa"
    },
    {
        "Artist": "Dan + Shay",
        "Song's name": "Tequila"
    },
    {
        "Artist": "Taylor Swift",
        "Song's name": "Delicate"
    },
    {
        "Artist": "Maroon 5",
        "Song's name": "Girls Like You (feat. Cardi B)"
    },
    {
        "Artist": "Selena Gomez",
        "Song's name": "Back to You"
    },
    {
        "Artist": "Bebe Rexha & Florida Georgia Line",
        "Song's name": "Meant to Be"
    },
    {
        "Artist": "Imagine Dragons",
        "Song's name": "Thunder"
    },
    {
        "Artist": "Cardi B, Bad Bunny & J Balvin",
        "Song's name": "I Like It"
    },
    {
        "Artist": "Twenty one pilots",
        "Song's name": "Levitate"
    },
    {
        "Artist": "Luke Bryan",
        "Song's name": "Sunrise, Sunburn, Sunset"
    },
    {
        "Artist": "Ariana Grande",
        "Song's name": "No tears left to cry"
    },
    {
        "Artist": "Post Malone",
        "Song's name": "Psycho (feat. Ty Dolla $ign)"
    },
    {
        "Artist": "Luke Combs",
        "Song's name": "Beautiful Crazy"
    },
    {
        "Artist": "Travis Scott",
        "Song's name": "STARGAZING"
    },
    {
        "Artist": "Zedd, Maren Morris & Grey",
        "Song's name": "The Middle"
    },
    {
        "Artist": "Ella Mai",
        "Song's name": "Trip"
    },
    {
        "Artist": "Ed Sheeran",
        "Song's name": "Perfect"
    },
    {
        "Artist": "Thomas Rhett",
        "Song's name": "Life Changes"
    },
    {
        "Artist": "Ella Mai",
        "Song's name": "Boo'd Up"
    },
    {
        "Artist": "Ariana Grande",
        "Song's name": "God is a woman"
    },
    {
        "Artist": "Foster the People",
        "Song's name": "Sit Next to Me"
    },
    {
        "Artist": "Mitchell Tenpenny",
        "Song's name": "Drunk Me"
    },
    {
        "Artist": "Camila Cabello",
        "Song's name": "Havana (feat. Young Thug)"
    },
    {
        "Artist": "Kane Brown",
        "Song's name": "Heaven"
    },
    {
        "Artist": "Jason Mraz",
        "Song's name": "Have It All"
    },
    {
        "Artist": "Panic! At the Disco",
        "Song's name": "High Hopes"
    },
    {
        "Artist": "Kane Brown",
        "Song's name": "Lose It"
    },
    {
        "Artist": "lovelytheband",
        "Song's name": "Broken"
    },
    {
        "Artist": "Calvin Harris, Dua Lipa",
        "Song's name": "One Kiss"
    }
]
pyexcel.save_as(records=itunes_top_50_songs, dest_file_name="itunes.xlsx")