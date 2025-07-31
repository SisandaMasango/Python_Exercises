rows_num = int(input("How many rows do you want? ")) + 1
pattern = "" #outisde the for loop to keep memory. New memory is created with each loop inside the loop.

#right angle triangle
for i in range(rows_num): 
    pattern += "*" #increment each loop with 1 
    print(pattern) #we print inside the loop to see each step
#print outside the loop to see final output which is the last row in this case

alph = 65
for i in range(1, rows_num):
    for j in range((rows_num - 1) - i): 
        print("~", end=" ") #This prints spaces 4,3,2,1
    for k in range(i): 
        print(chr(alph), end= " ")#This prints the first 1,2,3 stars
        alph += 1    
    for l in range(i - 1): #prints stars to make them odd
        print(chr(alph), end=" ")
        alph += 1    
    alph = 65 #begin from A again
    print()


for i in range(1, rows_num):
    for j in range((rows_num - 1) - i): 
        print("~") #This prints spaces 4,3,2,1
    for k in range(i): 
        print("*")#This prints the first 1,2,3 stars
         
    for l in range(i - 1):
        print("*")
    print()

for i in range(1, rows_num):
    for l in range(i - 1):
        print(" ", end = " ")
    for j in range(rows_num - i):
        print("*", end = " ")
    for k in range((rows_num - 1) - i ):
        print("*", end = " ")
    print()

for i in range(1,rows_num):
    for j in range(i):
        print("*", end=" ")
    print()
for k in range(2, rows_num):
    for l in range(rows_num - k):
        print("*", end=" ")
    print()

