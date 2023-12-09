import encryption as enc
import passwordManager as pwd
import extra as ex
import os

# ex.writeBanner("misc/ascii.txt")
accName = "AccData"
keyName = "Key"
param, path = ex.getListDir("database")

if not param:
    pubKey, privKey, nKey = enc.rsaAlgoritm()
    accMatrix = []
    catArray = []
else:
    try:
        keyString = ex.loadFile(path,keyName)
        pubKey, privKey, nKey = enc.strToKeys(keyString)
        mainString = ex.loadFile(path,accName)
        mainString = enc.decryptString(mainString, privKey, nKey)
        catArray, accMatrix = pwd.stringToDat(mainString)
    except FileNotFoundError:
        print("File is either corrupted or doesnt exist, terminate program")
        exit()
print("\nThe program has been sucessfully loaded !\n")
userInput = -1
while(userInput != "4"):
    ex.writeMenu()
    userInput = str(input("|-> Please input your command : "))
    if userInput == "1":
        pwd.addAccount(accMatrix, catArray)
    elif userInput == "2":
        pwd.deleteAccount(accMatrix, catArray)
    elif userInput == "3":
        pwd.printAccount(accMatrix, catArray)
    elif userInput == "4":
        print("")
    else:
        print("Invalid Command!")

mainString = pwd.datToString(accMatrix, catArray)
mainString = enc.encryptString(mainString, pubKey, nKey)

ex.saveFile(path,accName,mainString)