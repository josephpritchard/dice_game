import random, name_lists

''' 
Example: roll_dice(1, 10, 5)
    This will return a list with 5 random numbers between 1 and 10
'''
def roll_dice(low, high, rolls):
    rolls_list = []
    for i in range(rolls):
        roll = random.randint(low, high)
        rolls_list.append(roll)
    return rolls_list

'''
Example: get_random_roll(1, 50, 5000)
    This will return one integer randomly selected from a list of 5000 random integers between 1 and 50
'''
def get_random_roll(low, high, rolls):
    random_roll = roll_dice(low, high, rolls)
    random_choice = random.randint(1,len(random_roll)-1)
    return random_roll[random_choice]

city = random.randrange(len(name_lists.cities))
animal = random.randrange(len(name_lists.animals))
print(f"Your team name is: The {name_lists.cities[city]} {name_lists.animals[animal]}")
