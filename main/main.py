import math
import os


def menuMain():
    os.system("cls")
    print("A Simple Night Crows Profit Analyzer by Xhenoa ")
    print("\n\n1 - Morion")
    print("2 - Papyrus")
    print("3 - Gear")
    print("4 - Promote")
    print("5 - Feather")
    print("6 - Tear")
    print("7 - Exit")
    userInput = input("\nChoose an Option: ")

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
        menuMain()


def calculateMorion():
    os.system("cls")
    print("MORION CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPMorion = float(input("MORION Buy Price: "))
    gamePMorion = float(input("Morion In-Game Price: "))

    resultMorion = userCrow / marketPMorion
    userACrow = math.floor(resultMorion) * marketPMorion
    gameAmtMorion = math.floor(resultMorion) * 10
    resultNCDiamond = gameAmtMorion * gamePMorion
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPDiamond = resultMCDiamond - (userCrow * 84)
    resultPCrow = resultPDiamond / 84
    resultPCTProfit = (resultPCrow / userACrow) * 100

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("MORION Token Amount:", math.floor(resultMorion))
    print("No Auction Fee Diamond:", math.floor(resultNCDiamond), "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", math.floor(resultMCDiamond), "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", math.floor(resultPCTProfit * 100) / 100.0, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("\nChoose an Option: ")

    if userInput == '1':
        calculateMorion()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return
    else:
        menuMain()


def calculatePapyrus():
    os.system("cls")
    print("PAPYRUS CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPPapyrus = float(input("PAPYRUS Buy Price: "))
    gamePPapyrus = float(input("Papyrus In-Game Price: "))

    resultPapyrus = userCrow / marketPPapyrus
    userACrow = math.floor(resultPapyrus) * marketPPapyrus
    gameAmtPapyrus = math.floor(resultPapyrus) * 10
    resultNCDiamond = gameAmtPapyrus * gamePPapyrus
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPDiamond = resultMCDiamond - (userCrow * 84)
    resultPCrow = resultPDiamond / 84
    resultPCTProfit = (resultPCrow / userACrow) * 100

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("PAPYRUS Token Amount:", math.floor(resultPapyrus))
    print("No Auction Fee Diamond:", math.floor(resultNCDiamond), "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", math.floor(resultMCDiamond), "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", math.floor(resultPCTProfit * 100) / 100.0, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("\nChoose an Option: ")

    if userInput == '1':
        calculatePapyrus()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return
    else:
        menuMain()


def calculateGear():
    os.system("cls")
    print("GEAR CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPGear = float(input("GEAR Buy Price: "))
    gamePGear = float(input("Meticulous Aircraft Component In-Game Price: "))

    resultGear = userCrow / marketPGear
    userACrow = math.floor(resultGear) * marketPGear
    gameAmtGear = math.floor(resultGear) * 1
    resultNCDiamond = gameAmtGear * gamePGear
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPDiamond = resultMCDiamond - (userCrow * 84)
    resultPCrow = resultPDiamond / 84
    resultPCTProfit = (resultPCrow / userACrow) * 100

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("GEAR Token Amount:", math.floor(resultGear))
    print("No Auction Fee Diamond:", math.floor(resultNCDiamond), "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", math.floor(resultMCDiamond), "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", math.floor(resultPCTProfit * 100) / 100.0, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("\nChoose an Option: ")

    if userInput == '1':
        calculateGear()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return
    else:
        menuMain()


def calculatePromote():
    os.system("cls")
    print("PROMOTE CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPPromote = float(input("PROMOTE Buy Price: "))
    gamePPromote = float(input("Higher Seal of Advancement In-Game Price: "))

    resultPromote = userCrow / marketPPromote
    userACrow = math.floor(resultPromote) * marketPPromote
    gameAmtPromote = math.floor(resultPromote) * 1
    resultNCDiamond = gameAmtPromote * gamePPromote
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPDiamond = resultMCDiamond - (userCrow * 84)
    resultPCrow = resultPDiamond / 84
    resultPCTProfit = (resultPCrow / userACrow) * 100

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("PROMOTE Token Amount:", math.floor(resultPromote))
    print("No Auction Fee Diamond:", math.floor(resultNCDiamond), "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", math.floor(resultMCDiamond), "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", math.floor(resultPCTProfit * 100) / 100.0, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("\nChoose an Option: ")

    if userInput == '1':
        calculatePromote()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return
    else:
        menuMain()


def calculateFeather():
    os.system("cls")
    print("FEATHER CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPFeather = float(input("FEATHER Buy Price: "))
    gamePFeather = float(input("Piece of the Sky In-Game Price: "))

    resultFeather = userCrow / marketPFeather
    userACrow = math.floor(resultFeather) * marketPFeather
    gameAmtFeather = math.floor(resultFeather) * 1
    resultNCDiamond = gameAmtFeather * gamePFeather
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPDiamond = resultMCDiamond - (userCrow * 84)
    resultPCrow = resultPDiamond / 84
    resultPCTProfit = (resultPCrow / userACrow) * 100

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("FEATHER Token Amount:", math.floor(resultFeather))
    print("No Auction Fee Diamond:", math.floor(resultNCDiamond), "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", math.floor(resultMCDiamond), "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", math.floor(resultPCTProfit * 100) / 100.0, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("\nChoose an Option: ")

    if userInput == '1':
        calculateFeather()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return
    else:
        menuMain()


def calculateTear():
    os.system("cls")
    print("TEAR CALCULATOR")
    userCrow = float(input("\n\nYour CROW Token: "))
    marketPTear = float(input("TEAR Buy Price: "))
    gamePTear = float(input("Frozen Tear In-Game Price: "))

    resultTear = userCrow / marketPTear
    userACrow = math.floor(resultTear) * marketPTear
    gameAmtTear = math.floor(resultTear) * 1
    resultNCDiamond = gameAmtTear * gamePTear
    gameCDiamond = math.floor(resultNCDiamond * 0.05)
    resultMCDiamond = resultNCDiamond - math.floor(resultNCDiamond * 0.05)
    resultPDiamond = resultMCDiamond - (userCrow * 84)
    resultPCrow = resultPDiamond / 84
    resultPCTProfit = (resultPCrow / userACrow) * 100

    print("\nTrue CROW Amount to Spend:", userACrow)
    print("TEAR Token Amount:", math.floor(resultTear))
    print("No Auction Fee Diamond:", math.floor(resultNCDiamond), "Diamond")
    print("5% Auction Fee:", gameCDiamond, "Diamond")
    print("Diamond with Auction Fee:", math.floor(resultMCDiamond), "Diamond")
    print("Diamond Profit:", math.floor(resultPDiamond), "Diamond")
    print("Diamond to CROW Profit:", math.floor(resultPCrow), "CROW")
    print("Percent Profit:", math.floor(resultPCTProfit * 100) / 100.0, '%')

    print("\n\n1 - New Calculation")
    print("2 - Back to Main Menu")
    print("3 - Exit Application")
    userInput = input("\nChoose an Option: ")

    if userInput == '1':
        calculateTear()
    elif userInput == '2':
        menuMain()
    elif userInput == '3':
        return
    else:
        menuMain()


if __name__ == '__main__':
    menuMain()
    exit(0)
