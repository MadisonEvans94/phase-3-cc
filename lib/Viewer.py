class Viewer:
    def __init__(self, username):
        if len(username) <= 6 or len(username) >= 16: 
            raise Exception("Please enter a username that is proper length")
        self._username = username
        self._reviews = []
        self.reviewed_movies = []

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