# main.py - Movie Night Planner
from models import Movie,Watchlist
def load_movies(filename):
    movies = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                try:
                    title, genre, rating, duration = parts
                    movies.append(Movie(title, genre, float(rating), int(duration)))
                except ValueError:
                    # wrong number of columns or letters in a number
                    print(f"Warning: skipped bad row -> {line.strip()}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return movies
#view all movies
def view_movies(movies):
    if not movies:
        print("No movies loaded.")
        return
    for number, movie in enumerate(movies, start=1):
        print(f"{number}. {movie}")
#movies by genre
def search_by_genre(movies):
    genre = input("Enter genre: ").strip().lower()
    found = [movie for movie in movies if movie.genre.lower() == genre]
    if not found:
        print("No movies found for that genre.")
    for movie in found:
        print(movie)
#find movies with rating of your own choice
def search_by_rating(movies):
    try:
        min_rating = float(input("Enter minimum rating: "))
    except ValueError:
        print("Invalid rating. Please enter a number.")
        return
    found = [movie for movie in movies if movie.rating >= min_rating]
    if not found:
        print("No movies found with that rating.")
    for movie in found:
        print(movie)
# add a movie by title
def add_to_watchlist(movies, watchlist):
    title = input("Enter the movie title to add: ").strip()
    for movie in movies:
        if movie.title.lower() == title.lower():
            if watchlist.add_movie(movie):
                print(f"{movie.title} added to watchlist.")
            else:
                print(f"{movie.title} is already in your watchlist.")
            return
    print("Movie not found in the library.")
# removing movie from the watchlist
def remove_from_watchlist(watchlist):
    title = input("Enter the movie title to remove: ").strip()
    if watchlist.remove_movie(title):
        print("Movie removed.")
    else:
        print("That movie is not in your watchlist.")
# show watchlist with analytics
def view_watchlist(watchlist):
    if not watchlist.movies:
        print("Your watchlist is empty.")
        return
    for movie in watchlist.movies:
        print(movie)
    print(f"\nTotal duration: {watchlist.total_duration()} minutes")
    print(f"Average rating: {watchlist.average_rating()}")
# error for invalid input
def error_handling():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

# main menu
def menu():
    movies = load_movies("data/movies.csv")
    watchlist = Watchlist()
    print(f"Loaded {len(movies)} movies.")
    while True:
        print("\nWelcome to Movie Night Planner!")
        print("1. View All Movies")
        print("2. Search by Genre")
        print("3. Search by Minimum Rating")
        print("4. Add to Watchlist")
        print("5. Remove from Watchlist")
        print("6. View Watchlist and Analytics")
        print("7. Exit")
        choice = error_handling()
        if choice == 1:
            view_movies(movies)
        elif choice == 2:
            search_by_genre(movies)
        elif choice == 3:
            search_by_rating(movies)
        elif choice == 4:
            add_to_watchlist(movies, watchlist)
        elif choice == 5:
            remove_from_watchlist(watchlist)
        elif choice == 6:
            view_watchlist(watchlist)
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()