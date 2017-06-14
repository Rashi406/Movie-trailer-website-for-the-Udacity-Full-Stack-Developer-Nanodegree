import fresh_tomatoes2
import media

# Instances of class Movie
avatar = media.Movie(
    "Avatar", "Jake, a paraplegic marine, replaces his brother on the Na'vi"
    "inhabited Pandora for a corporate mission. He is accepted by the natives"
    "as one of their own but he must decide where his loyalties lie.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")


gww = media.Movie(
    "Gone With The Wind",
    "American classic in which a manipulative woman and a roguish man carry"
    "on a turbulent love affair in the American south during the Civil War"
    "and Reconstruction.",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Poster_-_Gone_With_the_Wind_01.jpg/330px-Poster_-_Gone_With_the_Wind_01.jpg",  # noqa
    "https://www.youtube.com/watch?v=0dTsfsr6-X8")

ratatouille = media.Movie(
    "Ratatouille",
    "Remy, a rat, aspires to become a renowned French chef. He doesn't realise"
    "that people despise rodents and will never enjoy a meal cooked by him.",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=e8GBfNo3IHY")

avengers = media.Movie(
    "The Avengers",
    "S.H.I.E.L.D. leader Nick Fury is compelled to launch the 'Avengers"
    "Initiative' when Loki poses a threat to planet Earth. Will Nick Fury's"
    "squad of superheroes prove themselves equal to the task?",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=NPoHPNeU9fc")

inception = media.Movie(
    "Inception",
    "Cobb steals information from his targets by entering their dreams. He"
    "is wanted for his alleged role in his wife's murder and his only chance"
    "at redemption is to perform the impossible, an inception.",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=YoHD9XEInc0")

aiw = media.Movie(
    "Alice in Wonderland",
    "Alice, now 19 years old, follows a rabbit in a blue coat to a magical"
    "wonderland from her dreams where she is reunited with her friends who"
    "make her realise her true destiny.",
    "https://upload.wikimedia.org/wikipedia/en/f/ff/Alice-In-Wonderland-Theatrical-Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=9POCgSRVvf0")

shutter_island = media.Movie(
    "Shutter Island",
    "Teddy Daniels and Chuck Aule, two US marshals, are sent to an asylum"
    "on a remote island in order to investigate the disappearance of a"
    "patient, but Teddy uncovers a shocking truth about the place.",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

narnia = media.Movie(
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
    "While playing, Lucy and her siblings find a wardrobe that lands them"
    "in a mystical place called Narnia. Here they realise that it was fated"
    "and they must now unite with Aslan to defeat an evil queen.",
    "https://upload.wikimedia.org/wikipedia/en/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg",  # noqa
    "https://www.youtube.com/watch?v=ppHpfXXFAts")

fight_club = media.Movie(
    "Fight Club",
    "Discontented with his capitalistic lifestyle, a white-collared"
    "insomniac forms an underground fight club with Tyler, a careless soap"
    "salesman. The project soon spirals down into something sinister.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=D3Yw9Yc1YmY")

# List of movies to be viewed on the website
movies = [
    avatar, gww, ratatouille, avengers, inception, aiw, shutter_island, narnia,
    fight_club
]

# Creates a website that shows the movies present in the list
fresh_tomatoes2.open_movies_page(movies)
