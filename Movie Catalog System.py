import os

class Movie_Catalog:
    def __init__(self, filename):
        self.filename = filename
        self.title = None
        self.studio = None
        self.date_released = None
        self.genre = None

    def add_movie(self):
        self.title = input("Enter the title: ").title()
        self.studio = input("Enter the studio: ").title()
        self.date_released = input("Enter the release date (YYYY-MM-DD): ")
        self.genre = input("Enter the genre: ").title()

        with open(self.filename, "a") as file:  # Open the file in append mode
            file.write(f"{self.title}, {self.studio}, {self.date_released}, {self.genre}\n")  # Write movie details to the file

        print("Movie added successfully!")  # Print success message

    def view_movies(self):
        if not os.path.exists(self.filename):  # Check if file exists
            print("No movies in the catalog yet.")  # Print message if file doesn't exist
            return  # Exit function

        movies = {}  # Create a dictionary to store movies by genre

        with open(self.filename, "r") as file:  # Open the file in read mode
            for line in file:  # Iterate through each line in the file
                title, studio, date, genre = line.strip().split(", ")  # Split line into components

                if genre in movies:  # Check if genre already exists in movies
                    movies[genre].append((title, studio, date))  # Add movie to existing genre list
                else:
                    movies[genre] = [(title, studio, date)]  # Create new genre entry with the movie

        print("\nAll movies:")  # Print header for movies summary

        for genre, movie_list in movies.items():  # Iterate through the genres and their movie lists
            print(f"\nGenre: {genre}")  # Print the genre
            for title, studio, date in movie_list:  # Iterate through each movie in the genre
                print(f"\tTITLE: {title}"
                      f"\n\t\tSTUDIO: {studio}"
                      f"\n\t\tRELEASE DATE: {date}")  # Print movie details

    def display_movies_by_genre(self):
        if not os.path.exists(self.filename):  # Check if file exists
            print("No movies in this genre yet.")  # Print message if file doesn't exist
            return

        movies = {}  # Create a dictionary to store movies by genre

        with open(self.filename, "r") as file:  # Open the file in read mode
            for line in file:  # Iterate through each line in the file
                title, studio, date, genre = line.strip().split(", ")  # Split line into components

                if genre in movies:  # Check if genre already exists in movies
                    movies[genre].append((title, studio, date))  # Add movie to existing genre list
                else:
                    movies[genre] = [(title, studio, date)]  # Create new genre entry with the movie

        genre = input("Enter the genre you want to view: ").title()  # Get user input for genre
        filtered_movies = movies.get(genre, [])  # Get movies for the specified genre

        if not filtered_movies:
            print(f"No movies found in the genre: {genre}\n")
        else:
            print(f"\nMovies in the genre: {genre}")
            for title, studio, date in filtered_movies:
                print(f"\tTITLE: {title}"
                      f"\n\t\tSTUDIO: {studio}"
                      f"\n\t\tRELEASE DATE: {date}")
            print()

    def remove_movie(self, title_to_remove, date_to_remove):
        if not os.path.exists(self.filename):  # Check if file exists
            print("No movies in the catalog yet.")  # Print message if file doesn't exist
            return

        movies = []  # Create a list to store movies

        with open(self.filename, "r") as file:  # Open the file in read mode
            for line in file:  # Iterate through each line in the file
                title, studio, date, genre = line.strip().split(", ")  # Split line into components
                movies.append((title, studio, date, genre))  # Add movie to the list

        # Check if the movie to remove exists in the list
        movie_found = False
        for movie in movies:
            if movie[0].title() == title_to_remove.title() and movie[2] == date_to_remove:  # Compare titles and dates
                movies.remove(movie)
                movie_found = True
                break

        if not movie_found:
            print("Movie not found.")
            return

        # Write the updated list back to the file
        with open(self.filename, "w") as file:
            for title, studio, date, genre in movies:
                file.write(f"{title}, {studio}, {date}, {genre}\n")

        print("Movie deleted successfully!")

def main():
    filename = "movie_catalog.txt"  # Set filename
    catalog = Movie_Catalog(filename)  # Create an instance of Movie_Catalog

    while True:  # Start an infinite loop
        print("\n1. Add movie"
              "\n2. Remove movie"
              "\n3. View all movies"
              "\n4. View movies by genre"
              "\n5. Exit")  # Display menu options
        choice = input("Enter your choice: ")  # Prompt user for choice

        if choice == '1':  # If user chooses to add movie
            catalog.add_movie()  # Call add_movie method
        elif choice == '2':  # If user chooses to remove movie
            title_to_remove = input("Enter the title of the movie to remove: ").title()
            date_to_remove = input("Enter the release date of the movie to remove (YYYY-MM-DD): ")
            catalog.remove_movie(title_to_remove, date_to_remove)  # Call remove_movie method with title and date
        elif choice == '3':  # If user chooses to view all movies
            catalog.view_movies()  # Call view_movies method
        elif choice == '4':  # If user chooses to view movies by genre
            catalog.display_movies_by_genre()  # Call display_movies_by_genre method
        elif choice == '5':  # If user chooses to exit
            print("Exiting the program.")  # Print exit message
            break  # Break out of the loop
        else:
            print("Invalid choice. Please try again.")  # Print message for invalid input

if __name__ == "__main__":  # Check if script is being run directly
    main()  # Call main function to start the program
