class Movie:
    
    def __init__(self, title):
        if type(title) != str: 
            raise Exception("Movie must be a string")
        if len(title) < 1: 
            raise Exception("Movie must be at least 1 character")
        self._title = title
        self.reviews = []

    @property
    def title(self): 
        return self._title
    
    @title.setter
    def title(self, title): 
        if type(title) != str: 
            raise Exception("Movie must be a string")
        if len(title) < 1: 
            raise Exception("Movie must be at least 1 character")
        self._title = title

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
