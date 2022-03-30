class Person:
    """A member of a family.
    
    Attributes:
        name (str): the person's name.
    """
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.spouse = None
        self.parents = set()
        self.children = set()

    def marry(self, other):
        self.spouse = other
        other.spouse = self
