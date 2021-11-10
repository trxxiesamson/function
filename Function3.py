# Basic Function Program 3
#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ₱___.

def getMoney():
    money = int(input("Enter your money: "))
    return money

def getApplePrice():
    applePrice = int(input("Enter apple price: "))
    return applePrice

def getAppleQty():
    qty = (getmoney / getapplePrice)
    return qty

def getconvertQty():
    convert = (qty * getapplePrice)
    return convert

def getChange():
    change = (appleQTY - getmoney) 
    return change

getmoney = getMoney()
getapplePrice = getApplePrice()
qty = int(getmoney / getapplePrice)
appleQTY = int(qty * getapplePrice)
change = int(appleQTY - getmoney)

print("You can buy ",appleQTY, "apples and your change is ₱",change,)