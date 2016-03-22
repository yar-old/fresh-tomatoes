# Fresh Tomatoes

"Fresh Tomatoes" is a movie trailer app made with Python. Based on the first project from the Full Stack Web Developer Nano-Degree course taught by Udacity. This is intended to be server-side code which will parse through a list of movies and serve the title, poster image, and trailer to the front-end.

## Quick Start

To get started quickly, first [download the source files](https://github.com/yramocan/fresh-tomatoes/archive/fresh_tomatoes_dist.zip).

* Unzip the source files archive to your desired directory.
* Add your desired movie to the file `entertainment_center.py`
  * Use the `media.Movie()` syntax to create new instances for the "Movie" class.
  * For example: `my_movie = media.Movie("My Movie", [insert movie poster url], [insert movie trailer url])`
* Open Terminal and call `python entertainment_center.py`
* `fresh_tomatoes.html` will render in the `/build` directory and `fresh_tomatoes.py` will automatically open your webpage.

## Structure

The project structure has three main files and one `/build` directory:
* `fresh_tomatoes.py` (Main Functions)
* `media.py` (Movie Class)
* `entertainment_center.py` (Driver)
* `/build`

The output files from this application render to the `/build` directory.
