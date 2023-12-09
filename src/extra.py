import time as ti
import os

def getListDir(path):
    try:
        files = os.listdir(path)
        if files == []:
            call = input("| Looks like you don't have any database, do you want to create one (Y/N) ? : ").upper()
            if(call == 'Y'):
                databaseName = input("| Enter your database name : ")
                try:
                    os.makedirs(path+"/"+databaseName)
                    print(f"\nDatabase \"{databaseName}\" has been created !\nEnjoy !")
                    return False, path+"/"+databaseName
                except FileExistsError:
                    print("Folder already exist")
            else:
                print("Thank you for using our program !")
        else :
            print("==DATABASE LIST==")
            for file in files:
                print("- "+file)
            return True, path +'/'+ input("|-> Please choose your database : ")
    except FileNotFoundError:
        print("Directory doesn't exist")

def loadFile(path,fileName):
    strLoad = open(path+"/"+fileName+".txt","r")
    strRead = strLoad.read()
    strLoad.close()
    return strRead

def saveFile(path, fileName, strWrite):
    strLoad = open(path+"/"+fileName+".txt","w")
    strLoad.write(strWrite)
    strLoad.close()

def writeBanner(path):
    f = open(path,"r")
    strB = f.read().split('\n')
    for line in strB:
        ti.sleep(0.1)
        print(line)
    f.close()

def writeMenu():
    print("==MAIN MENU==")
    print("1. Add Account")
    print("2. Delete Account")
    print("3. Display Accounts")
    print("4. Exit")