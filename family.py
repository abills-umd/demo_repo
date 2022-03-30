class Person:
    """A member of a family.
    
    Attributes:
        name (str): the person's name.
        age (int): the person's age.
        gender (str): the person's gender.
        spouse (Person or None): who the person is married to (if anyone).
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
