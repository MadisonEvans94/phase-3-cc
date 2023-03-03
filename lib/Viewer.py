class Viewer:
    def __init__(self, username):
        if len(username) <= 6 or len(username) >= 16: 
            raise Exception("Please enter a username that is proper length")
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
        pass

    def rate_movie(self, movie, rating):
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
        
    