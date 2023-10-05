"""
Create a Python file named lab_4-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Prompt the user to enter their first name and store it with an appropriate variable.
Prompt the user to enter their last name and store it with an appropriate variable.
Create a new variable for the user's full name and set it equal to the first name variable plus the last name variable. What is the result?
Is there an issue with this output? How could we fix that?

"""
# Author: Andrew Tkacs

#Prompt the user to enter their first name and store it in a variable.
first_name = input("Enter your first name: ")

#Prompt the user to enter their last name and store it in a variable.
last_name = input("Enter your last name: ")

#Create a new variable for the user's full name.
full_name = first_name + " " + last_name

#Print the user's full name.
print("User's full name:", full_name)

#I found no issues with the code, At first, when printing the full name, the name was combined but I fixed that by simply adding a space.  
