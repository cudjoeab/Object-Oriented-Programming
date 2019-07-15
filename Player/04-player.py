class Player: 
    
    def __init__(self, name, gold_coins = 0, health_points = 10, lives = 5): 
        self.name = name 
        self.gold_coins = gold_coins
        self.health_points = health_points 
        self.lives = lives 

    def __str__(self):
        return f'{self.name} has {self.gold_coins} gold coins, {self.health_points} health points, and {self.lives} lives.'

player1 = Player('Abigail')
print(player1)