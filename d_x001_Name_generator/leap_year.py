year = int(input("Please enter year."))

if year % 4 != 0:
    print("Not leap year!")
else:
    if year % 100 != 0:
        print("Leap year")
    else:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("NOT Leap year")


# Alternate Version

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year!")
else:
    print("Not leap year!")
