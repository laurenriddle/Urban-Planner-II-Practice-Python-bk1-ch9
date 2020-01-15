import datetime

# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.


class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, name):
        self.owner = name

