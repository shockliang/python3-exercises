import random


playerHp = 260

enemyAttackLow = 60
enemyAttackHigh = 80

while playerHp > 0:
    damage = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHp -= damage

    if playerHp <= 30:
        playerHp = 30

    print("Enemy strike for", damage, "Current player hp is", playerHp)

    if playerHp == 30:
        print("You have low health. You've been teleported to the nearest inn.")
        break
