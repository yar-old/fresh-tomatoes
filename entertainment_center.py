# Include media.py to use "Movie" class
import media

# Include open_movies_page() from fresh_tomatoes.py
from fresh_tomatoes import open_movies_page

# Add movies here
spirited_away = media.Movie(
    "Spirited Away", # Title
    "http://www.nausicaa.net/miyazaki/sen/poster_images/USA_full.jpg", # Image
    "https://www.youtube.com/watch?v=ByXuk9QqQkk" # Trailer
)

mad_max = media.Movie(
    "Mad Max: Fury Road",
    "https://www.movieposter.com/posters/archive/main/201/MPW-100532",
    "https://www.youtube.com/watch?v=hEJnMQG9ev8"
)

zootopia = media.Movie(
    "Zootopia",
    "http://cdn3-www.comingsoon.net/assets/uploads/gallery/zootopia/c55463169023e916571b0361c592cd6c0f630904.jpg",
    "https://www.youtube.com/watch?v=bY73vFGhSVk"
)

#############################################

movies = [ spirited_away, mad_max, zootopia ] # Add list of movies to array
open_movies_page(movies) # Open the application web page
