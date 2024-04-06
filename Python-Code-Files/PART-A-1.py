#Total Possible Combinations
#Used Mathematical approach to reduce complexity
def tot_combinations( number_of_faces , number_of_dice ):
    return number_of_faces**number_of_dice
die_faces = 6
number_of_dice = 2
print("The Total Possible Combination is : ",tot_combinations( die_faces , number_of_dice ))