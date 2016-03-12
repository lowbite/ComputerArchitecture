# Printing all points to
# choose to calculate calories


str1 = ["Gender:", "1.Male", "2.Female"]
str2 = ["Physical activity:", "1.Minimum physical activity",
        "2. 3 times per week", "3. 5 times per week",
        "4. Every day", "5. 2 times per day"]


# Printing menu of age choice
def readAge():
    while(True):
        try:
            age = input("Age: ")
            if((age >= 13) & (age < 80)):
                break
            else:
                print("Unreal age!")
                print("Repeat please, age should be between 13 and 80")
        except NameError:
            print("Wrong input! Repeat please")
    return age


# Printing menu of gender choice
def readGender():
    while(True):
        for i in str1:
            print i
        try:
            gender = input()
            if((gender > 0) & (gender < 3)):
                break
            else:
                print("Wrong input! Repeat please")
        except NameError:
            print("Wrong input! Repeat please")
    return gender


# Printing menu of weight choice
def readWeight():
    while(True):
        try:
            weight = input("Weight: ")
            if((weight >= 35) & (weight < 250)):
                break
            else:
                print("Repeat please, weight should be between 35 and 250")
        except NameError:
            print("Wrong input! Repeat please")
    return weight


# Printing menu of height choice
def readHeight():
    while(True):
        try:
            height = input("Height in cm: ")
            if((height >= 120) & (height < 250)):
                break
            else:
                print("Repeat please, height should be between 120 and 250")
        except NameError:
            print("Wrong input! Repeat please")
    return height


# Printing menu of physical activity choice
def readPA():
    while(True):
        for i in str2:
            print i
        try:
            pa = input()
            if((pa >= 1) & (pa <= 5)):
                break
            else:
                print("Wrong input! Repeat please...")
        except NameError:
            print("Wrong input! Repeat please")
    return pa


# Printing main menu
def createMenu():
    print("1. Calculate your calories")
    print("2. Exit")


# Printing result of program
def getInfo(result):
    print (str(result) + " kilocalories")
