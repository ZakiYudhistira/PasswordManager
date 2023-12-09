def printCategories(catArray):
    print("\n==ACCOUNT CATEGORIES==")
    for i in range(len(catArray)):
        print(f"{i+1}.{catArray[i]}")

def addAccount(accMatrix, catArray):
    print("|-> ADD ACCOUNT")
    accountType = input("| Please enter your account type : ")
    name = input("| Please enter your account name : ")
    password = input("| Please enter your password : ")

    printCategories(catArray)
    n = len(catArray)+1
    print(f"{n}.ADD NEW TYPE")
    catAcc = int(input("\n| Enter your account category : "))

    if catAcc == n:
        catName = input("| Enter your new category : ")
        catArray.append(catName)
        print(f"\n{catName} sucessfully added to the CATEGORY database !\n")
    
    addUser = []
    addUser.append(accountType)
    addUser.append(name)
    addUser.append(password)
    addUser.append(catArray[catAcc-1])
    accMatrix.append(addUser)

    print("Account sucessfully added to the database!")

def printAccount(accMatrix, catArray):
    print("==ACCOUNT DATABASE==")
    for tp in catArray:
        print(f">> {tp} ACCOUNT <<\n")
        count = 1
        for i in range(len(accMatrix)):
            if tp == accMatrix[i][3]:
                print(f"[{count}] {accMatrix[i][0]} Account")
                print(f"| Username : {accMatrix[i][1]}")
                print(f"| Password : {accMatrix[i][2]}\n")
                count += 1
    
def deleteAccount(accMatrix, catArray):
    print("|-> DELETE ACCOUNT")
    printCategories(catArray)
    catAcc = int(input("| Enter your account category : "))
    temp = []
    count = 1
    print("\n==ACCOUNT LIST==")
    for i in range(len(accMatrix)):
        if catArray[catAcc-1] == accMatrix[i][3]:
            print(f"[{count}] {accMatrix[i][0]} Account")
            print(f"| Username : {accMatrix[i][1]}")
            temp.append(accMatrix[i][1])
            count += 1
    delN = int(input("Input your desired account : "))

    ynn = input(f"Are you sure you want to delete the Account \"{temp[delN-1]}\" (Y/N) ? : ").upper()
    if ynn == 'Y':
        for i in range(len(accMatrix)):
            if temp[delN-1] == accMatrix[i][1]:
                cat = accMatrix[i][3]
                break
        accMatrix.pop(1)
        countCat = getCatCount(accMatrix, cat)
        print(cat)
        print(f"\n| Account {temp[delN-1]} has been succesfuly deleted !")
        if countCat == 0:
            catArray.remove(cat)
            print(f"| The Category {cat} has been succcesfully deleted !\n")

def datToString(accMatrix, catArray):
    datStr = ""
    first = True
    for cat in catArray:
        if first :
            datStr += cat
            first = False
        else:
            datStr += ";" + cat
    datStr += "\n"
    for acc in accMatrix:
        datStr += acc[0]
        datStr += ";" + acc[1]
        datStr += ";" + acc[2]
        datStr += ";" + acc[3]
        datStr += "\n"
    return datStr

def stringToDat(string):
    lines = string.split('\n')
    accMatrix = []
    first = True
    for elm in lines:
        if first :
            catArray = elm.split(';')
            first = False
        else:
            acc = elm.split(';')
            if(acc != ['']):
                accMatrix.append(acc)
    return catArray, accMatrix

def getCatCount(accMatrix, cat):
    count = 0
    for i in range(len(accMatrix)):
        if accMatrix[0][2] == cat:
            count += 1
    return count