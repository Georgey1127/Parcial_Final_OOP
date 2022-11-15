"""
Movie Tickets: you have a single theater and want to sell movie tickets. 
You should be able to select the movie, the time, the seat position and the number of tickets you want to sell. 
There are two types of tickets, VIP and regular. You should keep track of how many seats are left. 
You need to allow multiple users. The users should be able to register and have an account with seat preference.
"""
from abc import ABC, abstractmethod

class Theater(ABC):
    """
    This is the abstract class.
    """
    @abstractmethod
    @property
    def movie(self, movies: list):
        pass

    @abstractmethod
    @property
    def time(self):
        pass

    @abstractmethod
    @property
    def selecttime(self, times: list):
        pass

    @abstractmethod
    @property
    def seats(self):
        pass

    @abstractmethod
    @property
    def tickets(self):
        pass
    

class SelectMovie(Theater):
 
    # overriding abstract method
    @property
    def movie(self, movies: list):
        self.movie = movies
 
class Time(Theater):
 
    # overriding abstract method
    @property
    def time(self):
        print("There are three times available for each Movie")
        print("6:20pm")
        print("8:30pm")
        print("11:40pm")
    
    @property
    def selecttime(self, times: list):
        self.movie_time = times
        


class Seats(Theater):
 
    # overriding abstract method
    @property
    def seats(self):
        print("All seats are available")
    
    @property
    def chooseseats(self):
        self.chooseseats = []


class Tickets(Theater):
 
    # overriding abstract method
    @property
    def tickets(self):
        print("How many tickets you want to buy?")
        self.tickets = 40