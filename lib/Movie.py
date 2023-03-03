class Movie:
    
    def __init__(self, title):
        self._title = title

    @property
    def title(self): 
        return self._title
    
    @title.setter
    def title(self, title): 
        self._title = title

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
