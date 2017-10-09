class Dog():
    """an easy trial to sim a dog"""
    def __init__(self, name, age):
        """init attribute name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """sim a dog to sit down"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """sim a dog to roll over"""
        print(self.name.title() + " rolled over!")