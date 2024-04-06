#implementing the process of undooming the dice
def undoom( new_A , new_B , old_freq ,start , end):
    if len(new_B)==len(new_A):
        if calculate_freq( new_A , new_B )==old_freq:
            new_A.sort()
            new_B.sort()
            print("Undoomed dice A and B :")
            printResult( new_A , new_B )
        return
    for i in range( start , end+1 , 1):
        new_B.append(i)
        undoom( new_A , new_B , old_freq , i+1 , end)
        new_B.pop()
        
#reassigning A value with values only less than or equal to 4
def process_A( A ):
    l=[]
    for i in A:
        if i > 4: i-=3
        l.append(i)
    return l

#Calculating frequency #As frequency changes probability also changes
def calculate_freq( A , B ):    
    k = [0]*11  #sum is only from 2 to 12
    for i in A:
        for j in B:
            tot = i+j
            k[tot-2] += 1
    return k

#printing the results
def printResult( A , B ):
    print("A :",*A)
    print("B :",*B)
    
A=[1 , 2 , 3 , 4 , 5 , 6]
B=[1 , 2 , 3 , 4 , 5 , 6]
print("Original Dice A and B:")
printResult( A , B)

freq = calculate_freq( A , B )
new_A = process_A( A )
new_B=[]
start = 1
end = 8 #given in problem that end of b can be greater than 6 and as probability of sums should not change we use 8 as end to bring max sum as 8+4=12
new_B.append(1)
new_B.append(8)

undoom( new_A , new_B , freq , start+1 , end-1 )



