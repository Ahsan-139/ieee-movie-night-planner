# class to store one movie
class Movie:
    def __init__(self, title, genre, rating, duration):
        self.title = title
        self.genre = genre
        self.rating = rating     
        self.duration = duration 

    # to return to mvoie
    def __str__(self):
        return (f"{self.title} | {self.genre} | Rating: {self.rating} | {self.duration} min")

# class to manage the personal watchlist
class Watchlist:
    def __init__(self):
        self.movies = []
        self.titles = set()   #stopping duplication

    # add a movie returns false if it is already in the list
    def add_movie(self, movie):
        if movie.title.lower() in self.titles:
            return False
        self.movies.append(movie)
        self.titles.add(movie.title.lower())
        return True

    # remove a movie by title returns False if not found
    def remove_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                self.movies.remove(movie)
                self.titles.discard(movie.title.lower())
                return True
        return False
    # sum of all durations in mins
    def total_duration(self):
        return sum(movie.duration for movie in self.movies)
    # average of ratings
    def average_rating(self):
        if not self.movies:
            return 0
        return sum(movie.rating for movie in self.movies) / len(self.movies)