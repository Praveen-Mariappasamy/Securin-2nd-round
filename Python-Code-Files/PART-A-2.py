#Displaying the distribution of all possible combinations

def find_distribution(die_face):
    for i in range( 1 , die_face+1 , 1 ):
        for j in range( 1 , die_face+1 , 1 ): #As 2 dice are thrown 2 for loops are used
            combination=[]
            combination.append(i)
            combination.append(j)
            possible_sum = i + j
            print( combination , "=" , possible_sum , end="  " )
        print()
            
die_faces = 6
print("The distribution of all possible combinations is : ")
find_distribution(die_faces)