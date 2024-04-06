#To Calculate the Probability of all Possible Sums occurring among the number of combinations

#Calculating frequency of all possible sums that occur
def find_combination_sum(die_face):
    dice_sum = {}
    for i in range( 1 , die_face+1 , 1 ):
        for j in range( 1 , die_face+1 , 1 ): #As 2 dice are thrown 2 for loops are used
            dice_sum[i+j] = dice_sum.get((i+j) , 0)+1
    return dice_sum

#Calculating Probability for the possible sum occuring
def getProbability( dice_sum , die_face ):
    tot_comb = die_face**2
    for possible_sum , freq in dice_sum.items():
        probability = freq/tot_comb
        print("Probability of sum={} : {:.3f}".format( possible_sum , probability ))

die_faces = 6
dice_sum = find_combination_sum( die_faces )
getProbability( dice_sum , die_faces )
