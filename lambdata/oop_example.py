"""Object Oriented Programming Examples - Sprint 1 - Module 2 """

import pandas as pd 


class MyDataFrame(pd.Dataframe):
    def num_cells(self):
        return self.shape[0] * self.shape[1] #number of cells of df
    
    






class BareMinimumClass:
    pass

class Complex:
    def __init__(self, real_part, imag_part):
        """
        Constructor for Complex Numbers.
        Complex numbers have a real part and imaginary part.
        """
        self.r = real_part
        self.i = imag_part
        
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i
        
    def __repr__(self):
        return "({}, {})".format(self.r, self.i)
    

class SocialMediaUser:
    def __init__(self, name, location, upvotes="0"):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)
    
    def receive_upvotes(self, num_upvotes="1"):
        self.upvotes += num_upvotes
    
    def is_popular(self):
        return self.upvotes >100


class Animal:
    """General Representaion of Animals"""
    
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type
        
    def run(self):
        return "Vroom, Vroom, I go quick"
    
    def eat(self, food):
        return "Huge fan of that" + food
    
if __name__ == "__main__":
    num1 = Complex(3, -5)  # num1.r = 3, num1.i = -5
    num2 = Complex(2, 6)  # num2.r = 2, num2.i = 6
    num1.add(num2)
    print("num1.r: {}, num1.i: {}".format(num1.r, num1.i))
    
    user1 = SocialMediaUser("John", "LA", 500)
    user2 = SocialMediaUser("Jennifer", "VA", 0)
    user3 = SocialMediaUser("Carl", "Mississippi")
    user4 = SocialMediaUser("George Washington", "Montpelior", 4000)
    user5 = SocialMediaUser("Carlos", "Argentina", 5)
    
    print(user1.is_popular())
    print(user2.is_popular())
    user2.receive_upvotes(101)
    print(user2.is_popular())