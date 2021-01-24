# Program to declare final result of Match

home_team = input("Home team name: ")
ht_score = int(input("Score: "))

away_team = input("Away team name: ")
at_score = int(input("Score: "))

# Determining winner logic
if ht_score == at_score:
    print("Draw")
elif ht_score > at_score:
    print("Winner is", home_team)
else:
    print("winner is", away_team)
