"""


You are doing a survey where you are asking people(who just came out from a movie theatre hall), which movie(movie names are unique) they watched, and how much they want to rate it on a scale of 1 to 5. 1 is lowest and 5 is highest. Get all inputs dynamically. Display avarage rating of all movies surveyed. Format:- MovieName | Average Rating Superman Returns 4 Gotham City 3 The Black Spider 5 */ public class MovieRaterApp { }


"""
if __name__ == "__main__":
    #Use dictionary to store movie name as Key, value is movie object

    movieMap{}
    while True:
        entry = input ("Add move name and rating (A 5) or 'q' to quit: ")
        if entry.lower() == 'q':
            break
        

class Movie:

    #Movie has name and list of ratings
    def __init__(self,name):
        self.name = name 
        self.ratings = []

    #add rating
    def addRating(self, rating)
        self.ratings.append(rating)

    #get average
    def printAveragePerMovie
        if not self.ratings:
            return 0
        return sum (self.ratings) / len (self.ratings)

