import random
import name_lists as l

class Team:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.fullname = None
        self.type = None
        self.score = None
        self.wins = None
        self.losses = None
        self.games_played = None

    # Method to get team type
    def team_type(self):
        # Sub-method to get input, and so input can be requested again if invalid
        def tt_input():
            print("Which type of team name do you want?")
            print('Animal, flower, or insect? (A/F/I)')
            # No prompt in input request so input is on a new line
            t = str(input())
            match t:
                case "A" | "a":     self.type = "Animal"
                case "F" | "f":     self.type = "Flower"
                case "I" | "i":     self.type = "Insect"
                case _:             print("Input Error. Try again..."); tt_input()
            print(f"You have selected: {self.type}")
        tt_input()

    # Method for selecting team name. self.type attribute needs to exist
    def team_choices(self):
        # Sub-method to generate random team names
        def random_team(ln):
            cls
            # Create/clear list
            team_choices = []
            # Create lists of first and last names
            team_first = random.sample((l.city + l.state), k=5)
            team_last = random.sample(ln, k=5) 
            # Loop through selections and add to empty list with formatting
            for i in range(5):
                team_choices.append("The " + team_first[i] + " " + team_last[i])
            return team_choices, team_first, team_last

        # Sub-method to display team selection and get input
        def rt_input(tc_list, tc_first, tc_last):
            print("= = = = = = = = = = = = = = = = = = = = =")
            print("Here are your randomly generated team names:")
            for i in range(len(tc_list)):
                print(f"{i+1}: {tc_list[i]}")
            print("= = = = = = = = = = = = = = = = = = = = =")
            try:
                print("Choose your team (1-5)")
                print("Input 6 to regenerate team names")
                t_input = int(input())
                # If statement to handle input
                if t_input in range(1, 6):
                    self.fullname = tc_list[t_input-1]
                    self.firstname = tc_first[t_input-1]
                    self.lastname = tc_last[t_input-1]
                elif t_input == 6:
                    print("You chose to regenerate team names")
                    input("Press 'Enter' to continue...")
                    random_team(ln_list)
                else:
                    print("Invalid input. Try again...")
                    rt_input(tc_list, tc_first, tc_last)
            except Exception as e:
                print(f"Error is {e}. Try again..."); rt_input(tc_list, tc_first, tc_last)

        # Adjust type string to match list names
        attr = self.type.lower()
        ln_list = getattr(l, attr)
        # Call sub-methods
        rt_list_var = random_team(ln_list)
        rt_input_var = rt_input(rt_list_var[0], rt_list_var[1], rt_list_var[2])


'''
team1 = Team()
team1.team_type()
team1.team_choices()
print(f"You chose: {team1.fullname}")
'''
