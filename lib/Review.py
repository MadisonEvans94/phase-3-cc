from lib.Viewer import Viewer
from lib.Movie import Movie

class Review:
    
    def __init__(self, viewer, movie, rating):
        if type(rating) != int: 
            raise Exception("Invalid rating. Must be int")
        if rating <=1 or rating >= 5: 
            raise Exception("Invalid rating. Must be between 1 and 5")
        if not isinstance(viewer, Viewer):
            raise Exception("Viewer must be Viewer")
        self._viewer = viewer
        self._movie = movie
        self._rating = rating
        
        
        
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating): 
        if type(rating) != int: 
            raise Exception("Invalid rating. Must be int")
        if rating <=1 or rating >= 5: 
            raise Exception("Invalid rating. Must be between 1 and 5")
        self._rating = rating

    # viewer property goes here!
    @property 
    def viewer(self):
        return self._viewer

    # movie property goes here!
