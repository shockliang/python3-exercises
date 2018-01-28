import random

class Enemy:
    attackLow = 60
    attackHigh = 80

    def getAttackPower(self):
        print("Attack power range. Low:", self.attackLow, "High:",self.attackHigh)

enemy1 = Enemy()
enemy1.getAttackPower()

enemy2 = Enemy()
enemy2 = enemy2.getAttackPower()

playerHp = 260

enemyAttackLow = 60
enemyAttackHigh = 80

while playerHp > 0:
    damage = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHp -= damage

    if playerHp <= 30:
        playerHp = 30

    print("Enemy strike for", damage, "Current player hp is", playerHp)

    if playerHp > 30:
        continue

    print("You have low health. You've been teleported to the nearest inn.")
    break