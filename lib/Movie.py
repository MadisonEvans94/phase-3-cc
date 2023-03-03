class Movie:
    
    def __init__(self, title):
        if type(title) != str: 
            raise Exception("Movie must be a string")
        if len(title) < 1: 
            raise Exception("Movie must be at least 1 character")
        self._title = title
        self._reviews = []
        self._reviewers = []

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
        sum_num = 0
        for t in self._reviews:
            sum_num = sum_num + t           
        if(len(self._reviews) > 0): 
            return (sum_num / len(self._reviews))
        return 0

    @classmethod
    def highest_rated(cls):
        pass

    @property 
    def reviews(self):
        return self._reviews
    
    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews
        
    @property 
    def reviewers(self):
        return self._reviewers
    
    @reviewers.setter
    def reviewers(self, viewers):
        self._reviewers = viewers
        
    def append_review(self, review): 
        self._reviews.append(review)