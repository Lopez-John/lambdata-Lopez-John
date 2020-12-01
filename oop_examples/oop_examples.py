"""A collection of classes"""

import pandas as pd

class MyDataFrame(pd.DataFrame):
    """Custom methods on top of the pd.DataFrame class"""
    def num_cells(self):
        return self.shape[0] * self.shape[1] # number of cells

class BareMinimumClass: # upper camel case
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for Complex Numbers
        Complex numbers have a real and imaginary part
        """
        self.r=realpart
        self.i=imagpart
        
    def add(self, other_complex):
        """Adds complex Numbers"""
        self.r += other_complex.r
        self.i += other_complex.i

class SocialMediaClass:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = str(location)
        self.upvotes = int(upvotes)
    
    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self): # starting with "is" mean it should return a boolean
        return self.upvotes > 100

class Animal:# parent class
    """General representation of animals"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return "Vroom, vroom, I go quick"

    def eat(self, food):
        return 'Huge fan of that '+ str(food)


class Sloth(Animal): # child class: inheriting the attributes from the parent class Animals
    """General representation of Sloth"""
    def __init__(self, name, weight, diet_type, num_naps=100):
        super().__init__(name, weight, diet_type) # uses the same attributes as parent class
        self.num_naps = num_naps

    def say_something(self):
        return 'This is a Sloth of typing'

    def run(self):
        return 'I am slow guy, I work at the DMV'



if __name__ =="__main__":
    #num1 =Complex(3,-5)
    #num2 = Complex(2,6)
    #num1.add(num2)
    #print(num1.r,num1.i)
    user1=SocialMediaClass('Carl', "Nepal")
    user2=SocialMediaClass('Carlton', 'Jamaica', upvotes=10)
    user3=SocialMediaClass('Carlos', 'Argentina', upvotes=10000000000)
    user4=SocialMediaClass('Andrew Jackson', location='Dijibouti',upvotes=6)
    print(user2.is_popular())
    user2.receive_upvotes(100)
    print(user2.is_popular())

    df = MyDataFrame({"a": [1,0,2]})
    df.num_cells()