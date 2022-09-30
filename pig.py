# Nina Perone

import random

# 1

def autoRollTo20(hold, p):
    total = 0
    while total < hold:
        roll = random.randint(1,6)
        if p == "p":
            print("Roll:", roll)
        if roll == 1:
            total = 0
            if p == "p":
                print("Turn total:", total)
            return total
        else:
            total += roll
    if p == "p":
        print("Turn total:", total)
    return total
#autoRollTo20(20, "p")
        




# 2              

def rollTo20Outcomes(numRuns, hold):
    outcomes = {}
    for _ in range(numRuns):
        score = autoRollTo20(hold, "n")
        if score not in outcomes:
            outcomes[score] = 1
        else:
            outcomes[score] += 1
    return outcomes

##numRuns = int(input("How many Hold-at-20 turn simulations?\n"))
##print("Score\t", "Estimated Probability")
##prob = rollTo20Outcomes(numRuns, 20)
##
##for i in prob:
##    prob[i] = prob[i]/numRuns
##
##for i in sorted(prob):
##    print(i, "\t", prob[i])




# 3     roll to 100, should have 99% chance of not scoring anything

##hold = int(input("Specify hold value: "))
##prob = rollTo20Outcomes(1, hold)
##print(prob[0]/hold)

 


# 4

def singleTurn(score, p):
    turn = 0
    while score < 100 and turn < 20:
        roll = random.randint(1,6)
        if p == "p":
            print("Roll:", roll)
        if roll == 1:
            turn = 0
            break
        turn += roll
    score += turn
    if p == "p":
        print("Turn total:", turn)
    #print("New score:", score)
    return score
##score = int(input("Score? "))
##print(singleTurn(score, "p"))




# 5

def game(p):
    score = 0
    turns = 0
    while score < 100:
        score += singleTurn(0,p)
        if p == "p":
            print("New score:", score)
        turns += 1
        #print(turns)
    return turns
#game("p")




# 6

def average(games):
    total = 0
    for i in range(games):
        turns = game("n")
        total += turns
    return total/games

##numGames = int(input("Games? "))
##print("Average turns:", average(numGames))



# 7

def twoPlay():
    score1 = 0
    score2 = 0
    turns = 1
    while score1 < 100 and score2 < 100:
        if turns % 2 != 0:
            print("It is player 1's turn.")
            roll = autoRollTo20(20, "p")
            score1 += roll
            print("Turn total:", roll)
            print("New score:", score1)
        else:
            print("It is player 2's turn.")
            roll = autoRollTo20(20, "p")
            score2 += roll
            print("Turn total:", roll)
            print("New score:", score2)
        print("Player 1 score:", score1)
        print("Player 2 score:", score2)
        turns += 1
#twoPlay()



# 8

def pigGame():
    score1 = 0
    score2 = 0
    turns = 1
    user = random.randint(1,2)

    if user == 1:
        print("You will be player 1.")
        print("Enter nothing to roll; enter anything to hold.")
        while score1 < 50 and score2 < 50:
            print("Player 1 score:", score1) # user
            print("Player 2 score:", score2) # comp
            if turns % 2 != 0: # user (player 1) turn
                print("It is player 1's turn.")
                total = 0
                hold = ""
                while hold == "" and total < 20 and score1 < 50:
                    roll = random.randint(1,6)
                    print("Roll:", roll)
                    if roll != 1:
                        total += roll
                    else:
                        total = 0
                        #print("Turn total:", total)
                        break
                    if score1 + total >= 50:
                        break
                    hold = input("Turn total: " + str(total) + " Roll/Hold? ")
                score1 += total
                print("New score:", score1)
                turns += 1
            else:
                print("It is player 2's turn.")
                #roll = autoRollTo20(20, "p")

                total = 0
                while total < 20:
                    roll = random.randint(1,6)
                    print("Roll:", roll)
                    if roll == 1:
                        total = 0
                        #print("Turn total:", total)
                        break
                    else:
                        total += roll
                        if total + score2 >= 50:
                            break
                score2 += total
                print("Turn total:", total)
                    
                #print("Turn total:", roll)
                print("New score:", score2)
                turns += 1

    else:
        print("You will be player 2.")
        print("Enter nothing to roll; enter anything to hold.")
        while score1 < 50 and score2 < 50:
            print("Player 1 score:", score1) # comp
            print("Player 2 score:", score2) # user
            if turns % 2 != 0: # comp (player 1) turn
                print("It is player 1's turn.")
                #roll = autoRollTo20(20, "p")

                total = 0
                while total < 20:
                    roll = random.randint(1,6)
                    print("Roll:", roll)
                    if roll == 1:
                        total = 0
                        #print("Turn total:", total)
                        break
                    else:
                        total += roll
                        if total + score1 >= 50:
                            break
                score1 += total
                print("Turn total:", total)
                    
                
                print("New score:", score1)
                turns += 1
            else:
                print("It is player 2's turn.")
                total = 0
                hold = ""
                while hold == "" and total < 20 and score2 < 50:
                    roll = random.randint(1,6)
                    print("Roll:", roll)
                    if roll != 1:
                        total += roll
                    else:
                        total = 0
                        #print("Turn total:", total)
                        break
                    if score2 + total >= 50:
                        break
                    hold = input("Turn total: " + str(total) + " Roll/Hold? ")
                score2 += total
                print("New score:", score2)
                turns += 1
pigGame()
    

