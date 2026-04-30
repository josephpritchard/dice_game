import os
from team_name import Team

# Function to clear screen
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    os.system("clear")

# Create player team
team1 = Team(True)
team1.team_type()
team1.team_choices()
clear_screen()
print(f"Your team is... {team1.fullname}!")

# Get opponent team name and type
team2 = Team(False)
team2.get_opponent_team(team1.type)
team2.team_choices()
print(f"The opposing team is... {team2.fullname}!")
