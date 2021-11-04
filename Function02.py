# Basic Function Program 2
# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount of the apples and oranges that you bought is ______.

applePrice = 20
orangePrice = 25

def getApple():
    appleQty = int(input("Quantity of apple: "))
    return appleQty

def getOrange():
    orangeQty = int(input("Quantity of orange: "))
    return orangeQty

def getTotalApple():
    totalApple = (apple * applePrice)
    return totalApple

def getTotalOrange():
    totalOrange = (orange * orangePrice)
    return totalOrange

def getTotal():
    total = (getTotalApple * getTotalOrange)
    return total

apple = getApple()
orange = getOrange()
getTotalApple = (apple * applePrice)
getTotalOrange = (orange * orangePrice)
total = (getTotalApple + getTotalOrange)

print("The total amount of the apples and oranges that you bought is" , total)