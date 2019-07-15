# Create a class called 'cat'

class Cat: 

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return f"Please feed {self.name} some {self.preferred_food} at {self.meal_time}PM. "
    #instance method for meal time 
    def eats_at(self):
        if self.meal_time > 0 and self.meal_time < 12: 
            return str(f'Meal time is at {self.meal_time}AM.')
        if self.meal_time > 12 and self.meal_time < 24:
            self.meal_time -= 12 
            return str(f'Meal time is at {self.meal_time} PM.')
    
    


#two instances of Cat 
garfield = Cat('Garfield', 'lasagna', 17)
hugo = Cat('hugo', 'jerk chicken', 16)

print(garfield)
print(hugo)

garfield.eats_at()
print(garfield)


