import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
while True:
    player=input("enter thr number of players (1*4): ")
    if player.isdigit():
        player=int(player)
        if 1<=player<=4:
            
            break
        else:
            print("Must be between 2 - 4 players.")

    else:
        print("invalid,Try again")
max_score=50
player_score=[0 for _ in range(player)]
while max(player_score)<max_score:
    for player_idx in range(player):
        print("Player number",player_idx+1,"turn has just started !\n")
        print("Your total score is:",player_score[player_idx],"\n")

        current_score=0
        while True:
            should_roll=input("Would you like to roll(y)?")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                print("you rolled a 1! Turn done !")
                current_score=0
        
                break
            else:
                current_score += value
                print("You rolled a:",value)
    
            print("Your score id:", current_score)
        player_score[player_idx]+=current_score
        print("Your total score is :", player_score[player_idx])
max_score=max(player_score)
winning_idx=player_score.index(max.score)
print("player number",winning_idx+1,"is the winner with score of:",max_score)



