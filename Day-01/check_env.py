#Get the Enviromnment from the User and print it on the Screen
env = input("Enter the Environment: ") #taking input from the user (keyboard) in env variable
print("The Environment is:", env)

#Conditional Statement Simple - if -else
if env == "prod":
    print("Don't Deploy on Friday")
elif env == "stg":
    print("Take backup and test well before deploy")
elif env == "test":
    print("test it well")
else:
    print("Safe to Deploy any day") 


# Type Casting - Converstion of one data-type to another data-type
a= int (input("Enter first number: "))
b= int (input("Enter second number: "))
print(type(a))
print("Mutliplication of a & b is:", int(a)*int(b))
print("Addition of a & b is:", int(a)+int(b))
print("Subtraction of a & b is:", int(a)-int(b))
print("Division of a & b is:", a/b)
#This program takes the environment name as input from the user and prints it on the screen



#Example Input: stg
#Example Output: The Environment is: stg   
#Another Example Input: prod
#Another Example Output: The Environment is: prod
#Use of input() function to take input from the User
#Use of print() function to print the output on the Screen
#Use of Variables to store the input value
#env is the variable which stores the input value
#Use of Comments to explain the code
#Use of String to print the output on the Screen
#Use of Concatenation to combine strings and variables in the print function
#Use of : to separate the string and variable in the print function
#Use of = to assign the input value to the variable
#Use of () in the input and print functions
#Use of "" to define the string in the input and print functions
#Use of indentation to structure the code properly
#This is a simple program to demonstrate the use of input and print functions in Python
#This program can be run in any Python environment
#This program is written in Python 3.x version
#This program is a part of Python for DevOps - AI Edition course