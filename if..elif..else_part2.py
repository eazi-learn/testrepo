'''
number = input("Please input an interger: ")

try:
    number = int(number)#try to cast the input
#catch the raised exception if there is an error - i.e it cant be casted
except ValueError as e:
    print("Yor input is not an integer.")
    print(e) #u can also access/print the exception's message
    #otherwisw, there is no error - i.e the input was casted
else:
    print(str(number) + "is indeed an integer!")
    
'''



n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #n define list of numbers


even_numbers = [] #to store lists of even numbers
even_count = 0

for number in n: #iterate over list
    if (number % 2 == 0):#test if number is even
        even_numbers.append(number)#append to even_numbers
print(even_numbers)
    
