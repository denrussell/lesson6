'''
User Input Data Processor
Objective: The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator

Write a script that asks for and checks the length of 
the user's first name and last name. 
Both should be at least 2 characters long. If not, print an error message.

'''

def user_name(first_name, last_name):
    if len(first_name) < 2:
        print("Please enter at least two characters or more for first name.")
        return False
    
    if len(last_name) < 2:
        print("Please enter at least two characters or more for last name.")
        return False    
    
    return True



while True:
    first_name = input("Please enter your first name: ")
    
    last_name = input("Please enter your last name: ")
    
    if user_name(first_name, last_name):
        break   

print(f"Your name: {first_name} {last_name}")


