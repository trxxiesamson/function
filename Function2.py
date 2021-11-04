applePrice = 20
orangePrice = 25

def getApple():
    apple_qty = int(input("Quantity of apple: "))
    return apple_qty

def getOrange():
    orange_qty = int(input("Quantity of orange: "))
    return orange_qty

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

print("The total amount is " , total)