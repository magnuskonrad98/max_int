lead_int = int(input("Enter lead: "))
secs_int = int(input("Enter seconds left: "))
team_with_ball = input("Which team has the ball: w (winning team) or l (losing team): ")

lead_int -= 3
if team_with_ball == "w":
    lead_int += 0.5
else:
    lead_int -= 0.5

if lead_int < 0:
    lead_int = 0

lead_int = lead_int ** 2

if lead_int > secs_int:
    print("The lead is safe")
else:
    print("The lead is NOÖt safe")