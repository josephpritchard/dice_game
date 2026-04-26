import random
import name_lists as l

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

state = random.randrange(len(l.state))
city = random.randrange(len(l.city))
animal = random.randrange(len(l.animal))
flower = random.randrange(len(l.flower))
insect = random.randrange(len(l.insect))


def get_team_name(input):
    print(input)

class Team:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.fullname = None
        self.type = None

    def get_type(self):
        def get_input():
            t = input(str('Animal, flower, or insect? (A/F/I)'))
            match t:
                case "A" | "a":     self.type = "Animal"
                case "F" | "f":     self.type = "Flower"
                case "I" | "i":     self.type = "Insect"
                case _:             print("Input Error. Try again..."); get_input()
            print(f"You have selected: {self.type}")
        print("Which type of team name do you want?")
        get_input()

    def get_team_choice(self):
        attr = self.type.lower()
        team_list = getattr(l, attr)
        team_last = random.sample(team_list, k=5) 
        team_first = random.sample((l.city + l.state), k=5)
        team_choices = []
        for i in range(5):
            team_choices.append("The " + team_first[i] + " " + team_last[i])
        print("= = = = = = = = = = = = = = = = = = = = =")
        print("Pick one of these team names:")
        for i in range(len(team_choices)):
            print(f"{i+1}: {team_choices[i]}")
        print("= = = = = = = = = = = = = = = = = = = = =")
        def get_input():
            try:
                return int(input('Choose your team (1-5) '))
            except Exception as e:
                print(f"Error is {e}. Try again..."); get_input()
        team_input = get_input()
        self.fullname = team_choices[team_input-1]
        self.firstname = team_first[team_input-1]
        self.lastname = team_last[team_input-1]

'''
    def get_team_name(self):
        def get_first(type):
            for i in range(5):
'''

team1 = Team()
team1.get_type()
team1.get_team_choice()
print(f"You chose: {team1.fullname}")



'''
        match self.type:
            case "Animal":          random.choice(l.type1)
            case "Flower":          get_first("flowers")
            case "Insect":          get_first("insects")
            case _:                 print("Team type error."); exit
            '''