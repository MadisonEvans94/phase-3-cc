class Viewer:
    
    def __init__(self, username):
        if len(username) <= 6 or len(username) >= 16: 
            raise Exception("Please enter a username that is proper length")
        self._username = username

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