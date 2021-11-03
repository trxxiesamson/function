# Basic function program 1
# Create a program that will ask for first name,last name, age, and address
# Display those details in the following format.
# Hello! My name is _________. I am currently _______ years old and I am residing at ___________.

def getFirstName():
    nameFunc = input("First Name: ")
    return nameFunc

def getLastName():
    LnameFunc = input("Last Name: ")
    return LnameFunc

def getAge():
    ageFunc = input("Age: ")
    return ageFunc

def getAddress():
    addFunc = input("Address: ")
    return addFunc

def displayOutput(LnameF,nameF, ageF, addressF):
    print(f"Hello! My name is {LnameF},{nameF}. I am currently {ageF} years old and I am residing at {addressF}.")

# Steps
# 1. Ask for first name and then save to variable.
name = getFirstName()
# 2. Ask for last name and then save to variable.
Lname = getLastName()
# 3. Ask for age and then save to variable.
age = getAge()
# 4. Ask for address and then save to variable.
address = getAddress()
# 5. Display first name, last name, age, and address.
displayOutput( Lname, name, age, address)
