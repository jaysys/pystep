# mymod01.py
""" mymodule
"""

maker = 'ROBOT'

def calc(a,b):
    """ calc
    """
    return a+b

class human:
    """ human class
    """
    def __init__(self, name, age):
        """ init function
        """
        self.name = name
        self.age = age

    def hello(self):
        """ hello function
        """
        print('Hi there')

    def info(self):
        """ display info
        """
        print("My name is "+ self.name +".")
        print("I'm " + str(self.age) + " years old")


