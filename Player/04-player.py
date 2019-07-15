class Player: 
    
    def __init__(self, name, gold_coins = 0, health_points = 10, lives = 5): 
        self.name = name 
        self.gold_coins = gold_coins
        self.health_points = health_points 
        self.lives = lives 

    def __str__(self):
        return f'{self.name} has {self.gold_coins} gold coins, {self.health_points} health points, and {self.lives} lives.'
#level up 
    def level_up(self, lvl_up):
        self.lives += lvl_up

 #collect coins and level up   
    def collect_treasure(self, coins):
        self.gold_coins += 1 
        if self.gold_coins % 10 == True:
            player1.level_up(1)


player1 = Player('Abigail')
print(player1)

# #calling level up instance method 
player1.level_up(1)
print(player1)