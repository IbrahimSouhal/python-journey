import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage! Health: {self.health}")

class Enemy(Character):
    def attack_player(self, player):
        damage = random.randint(1, self.attack)
        player.take_damage(damage)

class Player(Character):
    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)

# Game
player = Player(input("Enter your name: "), 100, 20)
enemy = Enemy("Dark Robot", 50, 15)

print(f"\n⚔️ {player.name} vs {enemy.name}!")

while player.is_alive() and enemy.is_alive():
    input("\nPress Enter to attack...")
    player.attack_enemy(enemy)
    
    if enemy.is_alive():
        enemy.attack_player(player)

if player.is_alive():
    print(f"\n🏆 {player.name} wins!")
else:
    print(f"\n💀 {enemy.name} wins!")