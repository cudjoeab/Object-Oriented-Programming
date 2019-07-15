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
            self.level_up(1)

#do battle
    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1 
            self.health_points = 10
        if self.lives == 0:
            self.player1(restart())
    
#restart game 
    def restart(self, gold_coins, health_points, lives):
        player1(__init__)


player1 = Player('Abigail')
print(player1)

# #calling level up instance method 
player1.level_up(1)
print(player1)

player1.collect_treasure(2)
print(player1)

