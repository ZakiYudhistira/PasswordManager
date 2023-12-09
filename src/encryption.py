import sympy as sy
import random as rd
import math as m

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def get2Prime():
    p = rd.randint(100,1000)
    q = rd.randint(100,1000)
    while p == q:
        q = rd.randint(100,1000)
    return sy.prime(p),sy.prime(q)

def getPub(m):
    while(True):
        e = rd.randrange(1,200)
        if (gcd(e,m) == 1):
            return e

def inverseMod(pub,m):
    for i in range(10,m):
        if((pub*i)%m == 1):
            return i

def rsaAlgoritm():
    p,q = get2Prime()
    n = p*q
    m = (p-1)*(q-1)

    pub = getPub(m)
    while pub == 1:
        pub = getPub(m)
    priv = inverseMod(pub,m)
    return pub,priv,n

def encrypt(char,pub,n):
    return int(pow(ord(char),pub,n))

def decrypt(value,priv,n):
    return int(pow(value,priv,n))

def encryptString(stringInput,pub,n):
    result = ""
    first = True
    for c in stringInput:
        if(c == '\n'):
            result += c
        else:
            if first:
                result += str(encrypt(c,pub,n))
                first = False
            else:
                result += '!' + str(encrypt(c,pub,n))
    return result

def decryptString(stringInput, priv, n):
    result = ""
    stringInput = stringInput.split('\n')
    for line in stringInput:
        parse = line.split('!')
        for num in parse:
            if(num != ''):
                result += chr(decrypt(int(num),priv,n))
        result += '\n'
    return result

def strToKeys(strKey):
    strKey = strKey.replace('\n',"")
    strKey = strKey.split(';')
    return int(strKey[0]), int(strKey[1]), int(strKey[2])

def keysToStr(pub, priv, n):
    return str(pub)+";"+str(priv)+";"+str(n)

# # print(rsaAlgoritm())
pub = 183
priv = 5684407
n = 16013551


testStr = """Google;Gaming;Entertainment
steam;cok;123;Gaming
uplay;jarjot;upin;Gaming
google;zakicandra81@gmail.com;zakicandra8*1;Google
spotify;zakisekuy83@gmail.com;zakisekuy8*3;Entertainment
"""
encrypted = encryptString(testStr,pub,n)
decrypted = decryptString(encrypted,priv,n)
f = open("sss.txt","w")
f.write(encrypted)
f.close()

