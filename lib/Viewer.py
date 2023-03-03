class Viewer:
    usernames = []
    def __init__(self, username):
        if len(username) <= 6 or len(username) >= 16: 
            raise Exception("Please enter a username that is proper length")
        if username in Viewer.usernames:
            raise Exception("Please enter a username that is unique")
        Viewer.usernames.append(username)
        self._username = username
        self._reviews = []
        self._reviewed_movies = []
        

    @property
    def username(self): 
        return self._username

    @username.setter
    def username(self, username):
        if len(username) <= 6 or len(username) >= 16: 
            raise Exception("Please enter a username that is proper length")
        self._username = username
        
    def reviewed_movie(self, movie):
        if movie in self._reviewed_movies:
            return True
        else: 
            return False
    
    def append_review(self, review): 
        self.reviews.append(review)    

    def rate_movie(self, movie, rating):
        if self.reviewed_movie(movie) == True: 
            for review in self.reviews: 
                if review.movie == movie: 
                    review.rating = rating
        elif self.reviewed_movie(movie) == False:
            from lib.Review import Review
            Review(self, movie, rating)
            
    # ^ this should work, idk why it isnt :(
        
    
    @property 
    def reviews(self): 
        return self._reviews
    
    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews
        
        
    @property 
    def reviewed_movies(self): 
        return self._reviewed_movies
    
    def append_review(self, review): 
        self._reviews.append(review)
        
    