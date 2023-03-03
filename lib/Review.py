
from lib.Movie import Movie
from lib.Viewer import Viewer
class Review:
    
    def __init__(self, viewer, movie, rating):
        if type(rating) != int: 
            raise Exception("Invalid rating. Must be int")
        if rating <1 or rating > 5: 
            raise Exception("Invalid rating. Must be between 1 and 5")
        if not isinstance(viewer, Viewer):
            raise Exception("Viewer must be Viewer")
        if not isinstance(movie, Movie):
            raise Exception("Movie must be Movie")
        self._viewer = viewer
        self._movie = movie
        self._rating = rating
        
        self._viewer.append_review(self)
        self._movie.append_review(self)
        self._movie.reviewers.append(self._viewer)
        
        
        
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating): 
        if type(rating) != int: 
            raise Exception("Invalid rating. Must be int")
        if rating <1 or rating > 5: 
            raise Exception("Invalid rating. Must be between 1 and 5")
        self._rating = rating

    # viewer property goes here!
    @property 
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer): 
        if not isinstance(viewer, Viewer):
            raise Exception("Viewer must be Viewer")
        self._viewer = viewer

    # movie property goes here!
    @property 
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if not isinstance(movie, Movie):
            raise Exception("Movie must be Movie")
        self._movie = movie
