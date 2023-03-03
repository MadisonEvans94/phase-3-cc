class Viewer:
    
    def __init__(self, username):
        if len(username) <= 6 or len(username) >= 16: 
            raise Exception("Please enter a username that is proper length")
        self.username = username

    @property
    def username(self): 
        return self.username

    @username.setter
    def username(self, username):
        if len(username) <= 6 or len(username) >= 16: 
            raise Exception("Please enter a username that is proper length")
        self.username = username
        
    def reviewed_movie(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass