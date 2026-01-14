# We will found a number is even or odd given by the user with the help of modulus operator %

num = int(input("Enter a number: ")) #take input from the user and convert it into integer and store it in num variable
if num % 2 == 0:   #checking the number is divisible by 2 or not
    print("The Given Value: Even")  #if the condition is true then print even   
else:
    print("The Given Value: Odd")   #if the condition is false then print odd   