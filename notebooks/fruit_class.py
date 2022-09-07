from unicodedata import name
import sys

class Fruit:
    def __init__(self, name, clr):
                    self.name = name
                    self.colour = clr
    def details(self):
        print("This is an " + self.name + " and it is " + self.colour)

def main(): 
    apple = Fruit("apple", "red")
    orange = Fruit("orange", "orange")
    
    apple.details()
    orange.details()

if __name__ == '__main__':
    main() 