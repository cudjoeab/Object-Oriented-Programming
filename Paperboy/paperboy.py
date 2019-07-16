class Paperboy:
    def __init__(self, name, experience = 0, earnings = 0):
        self.name = name
        self.experience = experience
        self.earnings = earnings
        
    
#String method 
    def __str__(self):
        return f"{self.name} has delivered {self.experience} papers and made ${self.earnings}."

#Quota method
    def quota(self): 
        quota = 50 + (self.experience /2)
        return f"{self.name} has to deliver {quota} papers today."

# #Deliver method 
    def deliver(self, start_address, end_address): 
        num_houses = start_address - end_address + 1
        quota = self.quota()

        self.experience += num_houses 

        daily_earnings = 0.0 

        if num_houses < quota: 
            daily_earnings = (num_houses * 0.25) - 2.00
        if num_houses > quota: 
            daily_earnings = (quota * 0.25) 
            bonus = (num_houses - quota) * 0.50
            daily_earnings = daily_earnings + bonus 
        return daily_earnings 


#print information about paperboy 
jack = Paperboy('Jack', 20, 25.00,)
les = Paperboy('Les', 20 , 6.25)
print(jack)
print(les)

# get daily quota 
print(jack.quota())







