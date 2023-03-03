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
        
    def return_movie(self, movie):
        if self.reviewed_movie == False: 
            raise Exception("not found")
        
        for mov in self._reviewed_movies:
            if movie == mov:
                return mov

    def rate_movie(self, movie, rating):
        if self.reviewed_movie(movie) == False: 
            movie.reviews.append(rating)
            movie.reviewers.append(self)
        elif self.reviewed_movie(movie) == True:
            pass 
    
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
        
    