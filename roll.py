import random

def roll_dice(low, high, rolls):
    rolls_list = []
    for i in range(rolls):
        roll = random.randint(low, high)
        rolls_list.append(roll)
    return rolls_list

roll_dice(5, 10, 200)
