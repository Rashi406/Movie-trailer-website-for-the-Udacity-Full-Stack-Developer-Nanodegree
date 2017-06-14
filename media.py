class Movie():
    """
    Representation of a movie.
    """

    def __init__(self, title, movie_storyline, poster_image, youtube_trailer):
        """
        Initialize a Movie instance,saves all parameters as attributes
        of the instance.

        title: Tiltle of the movie (a string)
        storyline: Synopsis of the movie (a string)
        poster_image_url: Link to the movie's poster image. (a string)
        trailer_youtube_url: Link to the movie's trailer
                             on YouTube. (a string)
        """
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
