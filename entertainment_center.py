import media
from fresh_tomatoes import open_movies_page #

spirited_away = media.Movie(
    "Spirited Away", "http://www.nausicaa.net/miyazaki/sen/poster_images/USA_full.jpg", "https://www.youtube.com/watch?v=ByXuk9QqQkk"
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

movies = [ spirited_away, mad_max, zootopia ]
open_movies_page(movies)
