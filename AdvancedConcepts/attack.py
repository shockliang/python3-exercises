import random

class Enemy:

    def __init__(self, attackLow, attackHigh):
        self.attackLow = attackLow
        self.attackHigh = attackHigh

    def getAttackPower(self):
        print("Attack power range. Low:", self.attackLow, "High:",self.attackHigh)

enemy1 = Enemy(60, 80)
enemy1.getAttackPower()

enemy2 = Enemy(50, 100)
enemy2 = enemy2.getAttackPower()

'''
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
'''