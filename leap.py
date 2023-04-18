def CheckLeap(Year):
    if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
        print("given year is a leap year")
    else:
        print("given year is not a leap year")
        

Year = int(input("enter the number: "))
CheckLeap(Year)