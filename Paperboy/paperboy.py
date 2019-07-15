class Paperboy:
    def __init__(self, name, experience, earnings):
        self.name = name
        self.experience = experience
        self.earnings = earnings
    
#String method 
    def __str__(self):
        return f"{self.name} has delivered {self.experience} papers and made ${self.earnings}."




#print information about paperboy 
jack = Paperboy('Jack', 100, 25.00)
les = Paperboy('Les', 50, 6.25)
print(jack)
print(les)


