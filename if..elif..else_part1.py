#if condition is True, execute statements in body of if

x = int(input("2 + 2 = "))
if x == 4:
    print("Basic arithmetic holds")
else:
    print("wrong answer..try again!")



"""#Prompts the user for a numerical grade and prints the appropriate letter grade. So first
- get user input of a numerical grade,
- convert the user input to an integer,
- test the range of the number using flow control,
and then print the appropriate letter grade. For example, if the user enters a number between 90 and 100, give them an A"""

#get user input of a numerical grade
grade = input("Enter your English marks: ")

#cast to an int
grade = int(grade)

#test the range of the number and print the appropriate letter grade
if grade >= 90:
    print ("you got an \'A'!")
elif grade >= 80:
    print ("you got an \'A2'!")
elif grade >= 70:
    print ("you got an \'B1'!")
elif grade >= 60:
    print ("you got an \'B2'!")
elif grade >= 50:
    print ("you got an \'C'!")
else:
    print ("you got an \'F'!")
           
           
           
           
