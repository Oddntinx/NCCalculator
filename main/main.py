import math


def menuMain():
    print("A Simple Night Crows Profit Analyzer ")
    print("1 - Morion")
    print("2 - Papyrus")
    print("3 - Gear")
    print("4 - Promote")
    print("5 - Feather")
    print("6 - Tear")
    print("7 - Exit")
    userInput = input("Choose an Option: ")

    if userInput == '1':
        calculateMorion()
    elif userInput == '2':
        calculatePapyrus()
    elif userInput == '3':
        calculateGear()
    elif userInput == '4':
        calculatePromote()
    elif userInput == '5':
        calculateFeather()
    elif userInput == '6':
        calculateTear()
    elif userInput == '7':
        return
    else:
        print("Feature not Implemented Yet / Invalid Input")


def calculateMorion():
    print("\n\nMORION CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPMorion = float(input("MORION Buy Price: "))
    gamePMorion = float(input("Morion In-Game Price: "))

    resultMorion = userCrow / marketPMorion
    userACrow = math.floor(resultMorion) * marketPMorion
    gameAmtMorion = math.floor(resultMorion) * 10
    resultNCDiamond = gameAmtMorion * gamePMorion
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPCTProfit = ((resultMCDiamond - (userACrow * 84)) / resultMCDiamond) * 100
    resultPDiamond = resultMCDiamond - (userACrow * 84)
    resultPCrow = resultPDiamond / 84

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("MORION Token Amount:", math.floor(resultMorion))
    print("No Auction Fee Diamond:", resultNCDiamond, "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", resultMCDiamond, "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", resultPCTProfit, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("Choose an Option: ")

    if userInput == '1':
        calculateMorion()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return


def calculatePapyrus():
    print("\n\nPAPYRUS CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPPapyrus = float(input("PAPYRUS Buy Price: "))
    gamePPapyrus = float(input("Papyrus In-Game Price: "))

    resultPapyrus = userCrow / marketPPapyrus
    userACrow = math.floor(resultPapyrus) * marketPPapyrus
    gameAmtPapyrus = math.floor(resultPapyrus) * 10
    resultNCDiamond = gameAmtPapyrus * gamePPapyrus
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPCTProfit = ((resultMCDiamond - (userACrow * 84)) / resultMCDiamond) * 100
    resultPDiamond = resultMCDiamond - (userACrow * 84)
    resultPCrow = resultPDiamond / 84

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("PAPYRUS Token Amount:", math.floor(resultPapyrus))
    print("No Auction Fee Diamond:", resultNCDiamond, "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", resultMCDiamond, "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", resultPCTProfit, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("Choose an Option: ")

    if userInput == '1':
        calculatePapyrus()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return


def calculateGear():
    print("\n\nGEAR CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPGear = float(input("GEAR Buy Price: "))
    gamePGear = float(input("Meticulous Aircraft Component In-Game Price: "))

    resultGear = userCrow / marketPGear
    userACrow = math.floor(resultGear) * marketPGear
    gameAmtGear = math.floor(resultGear) * 1
    resultNCDiamond = gameAmtGear * gamePGear
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPCTProfit = ((resultMCDiamond - (userACrow * 84)) / resultMCDiamond) * 100
    resultPDiamond = resultMCDiamond - (userACrow * 84)
    resultPCrow = resultPDiamond / 84

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("GEAR Token Amount:", math.floor(resultGear))
    print("No Auction Fee Diamond:", resultNCDiamond, "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", resultMCDiamond, "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", resultPCTProfit, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("Choose an Option: ")

    if userInput == '1':
        calculateGear()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return


def calculatePromote():
    print("\n\nPROMOTE CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPPromote = float(input("PROMOTE Buy Price: "))
    gamePPromote = float(input("Higher Seal of Advancement In-Game Price: "))

    resultPromote = userCrow / marketPPromote
    userACrow = math.floor(resultPromote) * marketPPromote
    gameAmtPromote = math.floor(resultPromote) * 1
    resultNCDiamond = gameAmtPromote * gamePPromote
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPCTProfit = ((resultMCDiamond - (userACrow * 84)) / resultMCDiamond) * 100
    resultPDiamond = resultMCDiamond - (userACrow * 84)
    resultPCrow = resultPDiamond / 84

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("PROMOTE Token Amount:", math.floor(resultPromote))
    print("No Auction Fee Diamond:", resultNCDiamond, "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", resultMCDiamond, "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", resultPCTProfit, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("Choose an Option: ")

    if userInput == '1':
        calculatePromote()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return


def calculateFeather():
    print("\n\nFEATHER CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPFeather = float(input("FEATHER Buy Price: "))
    gamePFeather = float(input("Piece of the Sky In-Game Price: "))

    resultFeather = userCrow / marketPFeather
    userACrow = math.floor(resultFeather) * marketPFeather
    gameAmtFeather = math.floor(resultFeather) * 1
    resultNCDiamond = gameAmtFeather * gamePFeather
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPCTProfit = ((resultMCDiamond - (userACrow * 84)) / resultMCDiamond) * 100
    resultPDiamond = resultMCDiamond - (userACrow * 84)
    resultPCrow = resultPDiamond / 84

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("FEATHER Token Amount:", math.floor(resultFeather))
    print("No Auction Fee Diamond:", resultNCDiamond, "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", resultMCDiamond, "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", resultPCTProfit, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("Choose an Option: ")

    if userInput == '1':
        calculateFeather()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return


def calculateTear():
    print("\n\nTEAR CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPTear = float(input("TEAR Buy Price: "))
    gamePTear = float(input("Frozen Tear In-Game Price: "))

    resultTear = userCrow / marketPTear
    userACrow = math.floor(resultTear) * marketPTear
    gameAmtTear = math.floor(resultTear) * 1
    resultNCDiamond = gameAmtTear * gamePTear
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPCTProfit = ((resultMCDiamond - (userACrow * 84)) / resultMCDiamond) * 100
    resultPDiamond = resultMCDiamond - (userACrow * 84)
    resultPCrow = resultPDiamond / 84

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("TEAR Token Amount:", math.floor(resultTear))
    print("No Auction Fee Diamond:", resultNCDiamond, "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", resultMCDiamond, "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", resultPCTProfit, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("Choose an Option: ")

    if userInput == '1':
        calculateTear()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return


if __name__ == '__main__':
    menuMain()
    exit(0)
