wkd, fname = str(__file__).rsplit('/', 1) 

def main():
    
    print(problem1())
    print(problem2())

    return

# Alright so we have to determine what my score will be after a rigorous, absurdly long series of Rock-Paper-Scissors (R-P-S) matches
# in which we have a strategy guide with godlike power that knows my opponent's every move in every round. Free will out the window.
# The guide also tells me what move I ought to play so that I don't win all the time (too sus), but enough to score well.
# A-B-C represents the opponent's choice of R-P-S respectively, and X-Y-Z represents mine (we're to assume)
# So what's my score if I follow the guide book under this premise? 
def problem1():
    score = 0
    guide_doc = open(wkd + '/guide.txt', 'r')
    
    # loop through each round of the game, using each line of the provided guide_doc (.txt) as our indexer
    for line in guide_doc:
        opponent_move, move = line.strip().split(' ')                   # break up each line into two variables: the opponent's move, and mine 
        score += get_value(move)                                        # add the value of my move to my score

        win = round_won(get_value(move), get_value(opponent_move))      # check the outcome of the round

        if win == True:
            score += 6  # win is worth 6 pts
        elif win == None:
            score += 3  # draw still gives us 3 pts 

    return score 


# Lmao tricked you, XYZ actually represents the *outcome* as desired by the guide (Lose, Draw, Win), 
# rather than the move you were supposed to play... why tf would you make assumptions silly goose
# Now you have to treat XYZ differently, and figure out which move to play yourself.
# What's your total game score this time? Do it bitch
def problem2():
    score = 0
    guide_doc = open(wkd + '/guide.txt', 'r')
    
    for line in guide_doc:
        round_score = 0
        opponent_move, round_result = line.strip().split(' ')           # start out the same, just need to use 2nd input differently
        score += run_round(get_value(opponent_move), round_result)      # play out the round to figure out my score 

    return score

# Assume val and opponent_val can have valid values of the integers 1, 2, or 3 (representing the choices of R-P-S respectively)
def round_won(val, opponent_val):
    if val == opponent_val: 
        return None # if values are the same, it's a draw
    if val == (opponent_val % 3) + 1: 
        return True # This is the crux of everything. The pattern of R-P-S is even easier to work with in numeric form 
                    # Scissors beats Paper beats Rock. 3 beats 2 beats 1. 3 > 2 > 1
                    # But... it loops around on itself, because Rock beats Scissors (1 > 3 ...?)
                    # Solution: Use modulo. For values 1 and 2, it has no effect. 
                    #                       For 3, it converts it to 0, 
                    #                       Then in all cases you add your +1, and you always have the winning hand

    return False    # if the other two conditions were false, well...

# Convert the XYZ/ABC shorthand for 'R-P-S' into their numerical values for ease of use 
def get_value(move):
    match move:
        case 'X'|'A':
            return 1
        case 'Y'|'B':
            return 2
        case 'Z'|'C':
            return 3

    # if we reach here, probably means we're using bad input data 
    print('get_value() was used incorrectly')
    return -1

# We 'simulate' playing out a round, figure out what we need to play based on the desired outcome and the opponent's pre-selected hand
def run_round(opponent_val, round_result):
    bonus = 0                           # bonus points for win/draw scenarios
    possible_picks = [1,2,3]            # only used in case we are required to lose this round
    my_pick = opponent_val              # can i copy your answer? thanks...
    
    match round_result:                 # 'XYZ': "X= Lose, Y= Draw, Z= Win
        case 'Y':
            bonus = 3                   # we just copied the opponent's answer, so take my bonus, no other change
        case 'Z':
            my_pick = (my_pick % 3) + 1 # using the same formula we figured out in round_won() 
            bonus = 6
        case 'X':                       # losing the round is tougher, I can't figure out a way to use modulo in a similar, yet reverse fashion, 
            for p in possible_picks:    # so we'll just loop over all three possible options using round_won() func until it returns False
                if round_won(p, opponent_val) == False:
                    my_pick = p         # still fairly optimized, 1-3 arithmetic operations per line, instead of exactly 1
                    break               # feels kinda gross though ngl, happy to be one-upped here :)


    return my_pick + bonus              # round concludes, my score is just the sum of the numeric value of my play, plus any win/draw bonus

if __name__ == "__main__":
    main()