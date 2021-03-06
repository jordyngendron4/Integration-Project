# Jordyn Gendron
# Integration Project

def calcBA(hits, num_at_bat):
    batting_avg = round(hits / num_at_bat, 3)
    return batting_avg

def calcFP(chances, plays_made):
    field_per = round(plays_made / chances, 3)
    return field_per

def calcOBP(h, bb, hbp, ab, sf):
    obp = (h + bb + hbp)/(ab + bb + hbp + sf)
    return obp
def calcTB(h, d, t, hr):
    tb = h + d + 2*t + 3*hr
    return tb
def calcSP(tb, ab):
    sp = tb / ab
    return sp

def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    team = input("Enter the team you play for: ")
    print("We are going to be calculating your batting average.")
    total_hits = 0
    total_at_bats = 0
    times_at_bat = 0
    hits = 0
    total_batting_average = 0
    game = 1
    finished = False # flag
    while (not finished): # loop until finished asking for user input
        times_at_bat = int(input("How many at bats for game #" + str(game) + "? Enter 0 to quit: "))
        if times_at_bat == 0:
            finished = True
        else: 
            hits = int(input("How many hits? Enter 0 to quit: "))
            total_hits = total_hits + hits
            total_at_bats = total_at_bats + times_at_bat
            game_batting_average = calcBA(hits, times_at_bat)
            print("Your batting average for this game was ", '%.3f'%game_batting_average)
        game = game + 1
    if total_at_bats != 0:
        total_batting_average = calcBA(total_hits, total_at_bats)
    print("Your total batting average is ", '%.3f'%total_batting_average)

    position = input("Enter what position you play: ")
    print("Now we will be calculating your fielding percentage.")
    total_chances = 0
    total_plays_made = 0
    number_of_attempts = 0
    plays_made = 0
    total_fielding_percentage = 0
    game = 1
    finished = False
    while (not finished):
        number_of_attempts = int(input("How many attempts for game #" + str(game) + "? Enter 0 to quit: "))
        if number_of_attempts == 0:
            finished = True
        else:
            plays_made = int(input("How many plays did you make? Enter 0 to quit: "))
            total_plays_made = total_plays_made + plays_made
            total_chances = total_chances + number_of_attempts
            game_fielding_percentage = calcFP(number_of_attempts, plays_made)
            print("Your fielding percentage for this game was ", '%.3f'%game_fielding_percentage)
        game = game + 1
    if total_chances != 0:
        total_fielding_percentage = calcFP(total_chances, total_plays_made)

    lineup = input("Enter what number in the lineup you typically bat: ")
    print("In this next process your on base percentage (OBP) is going to be calculated")
    number_of_h = 0
    number_of_bb = 0
    number_of_hbp = 0
    number_of_ab = 0
    number_of_sf = 0
    total_of_h = 0
    total_of_bb = 0
    total_of_hbp = 0
    total_of_ab = 0
    total_of_sf = 0
    total_obp = 0
    finished = False
    while (not finished):
        number_of_ab = int(input("How many at bats did you have? Enter 0 to quit: "))
        total_of_ab = total_of_ab + number_of_ab
        if number_of_ab == 0:
            finished = True
        else:
            number_of_h = int(input("How many hits did you have? "))
            total_of_h = total_of_h + number_of_h
            number_of_bb = int(input("How many times did you walk? "))
            total_of_bb = total_of_bb + number_of_bb
            number_of_hbp = int(input("How many times did you get hit by pitch? "))
            total_of_hbp = total_of_hbp + number_of_hbp
            number_of_sf = int(input("How many sac flys did you have? "))
            total_of_sf = total_of_sf + number_of_sf
            game_obp = calcOBP(number_of_h, number_of_bb, number_of_hbp, number_of_ab, number_of_sf)
            print("Your on base percentage for this game was ", '%.3f'%game_obp)
    if total_of_ab != 0:
        total_obp = calcOBP(total_of_h, total_of_bb, total_of_hbp, total_of_ab, total_of_sf)
    print("Your total on base percentage is ", '%.3f'%total_obp)
    print("In this next process your slugging percentage (SP) is going to be calculated")
    number_of_h = 0  # number of hits
    number_of_d = 0  # number of doubles
    number_of_t = 0  # number of triples
    number_of_hr = 0  # number of home runs
    number_of_ab = 0
    game_tb = 0  #game total bases
    game_sp = 0  # game slugging percentage
    total_of_h = 0
    total_of_d= 0
    total_of_t = 0
    total_of_hr = 0
    total_of_ab = 0
    total_sp = 0  # total slugging percentage
    finished = False
    while (not finished):
        number_of_ab = int(input("How many at bats did you have? Enter 0 to quit: "))
        total_of_ab = total_of_ab + number_of_ab
        if number_of_ab == 0:
            finished = True
        else:
            number_of_h = int(input("How many hits did you have? "))
            total_of_h = total_of_h + number_of_h
            number_of_d = int(input("How many doubles did you hit? "))
            total_of_d = total_of_d + number_of_d
            number_of_t = int(input("How many triples did you hit? "))
            total_of_t = total_of_t + number_of_t
            number_of_hr = int(input("How many home runs did you hit? "))
            total_of_hr = total_of_hr + number_of_hr
            game_tb = calcTB(number_of_h, number_of_d, number_of_t, number_of_hr)
            game_sp = calcSP(game_tb, number_of_ab)
            print("Your slugging percentage for this game was ", '%.3f'%game_sp)
    if total_of_ab != 0:
        total_tb = calcTB(total_of_h, total_of_d, total_of_t, total_of_hr)
        total_sp = calcSP(total_tb, total_of_ab)
    print("Your total slugging percentage is ", '%.3f'%total_sp)
    
    print("Congratulations!")
    print("You have successfully calculated your stats.")
    print("Keep it up!")
    print("Have a great season!")
    print("You")
    print("Are")
    print("Awesome!")
    print("Hope to see you using this program soon!")
    print("Goodluck!")
main()
