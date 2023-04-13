import os 
import csv
import argparse 
import sys
import typing

#Deklarasi Global Variabel
userName : str  = ""
userPass : str  = ""
userFile : str = [[""] for i in range(101)]
bahanBangunan : str = [[""] for i in range(101)]
daftarCandi : str = [[""] for i in range(101)]
sedangBerjalan : bool = True


#Kumpulan Fungsi 

def panjangArray(namaFile): 
    f = open(namaFile, "r")
    i = 0
    t = "test"
    while(t != ""): 
        t = f.readline()
        i+=1 
    return i-1

def length(nString:str): 
    nMark : chr = '.'
    nString+= nMark
    i = 0
    while(nString[i] != nMark): 
        i+=1
    return i 

def cekPass(PassUser, arrayUser,n): 
    for i in range(n): 
        if( arrayUser[i][1] == PassUser): 
            return True
    return False

def cekUser(nameUser, arrayUser,n): 
    for i in range(n): 
        if( arrayUser[i][0] == nameUser): 
            return True
    return False
def initializeArray (array : list, n :int, m:int, array2:list , n2:int) : 
    newArray = [["" for i in range(m)] for i in range(n+n2)]
    for i in range(n):
        for j in range(m): 
            newArray[i][j] = array[i][j]
    
    if(array2!="."):
        for i in range(n2): 
            for j in range(m): 
                newArray[i + n][j] = array2[j]

    return newArray
            
        
def splitArr(nString:str,n:int): #Split dilakukan dengan asumsi ";" sebagai pemisah
    tmpArray = ["" for i in range(n)]
    tmpStr = ""
    indexArray =0
    for i in range(length(nString)): 
        if(nString[i] == ";"):
            tmpArray[indexArray]=tmpStr
            tmpStr = ""
            indexArray +=1
        else : 
            tmpStr+=nString[i]
    tmpStr = removeEndspace(tmpStr)
    tmpArray[indexArray]=tmpStr
    return tmpArray

def removeEndspace (x): 
    temp = ""
    for i in range(length(x)): 
        if(x[i] == "\n" ) : 
            break ; 
        else :
            temp += x[i]
    return temp
            
def memintaArgs() : #Prosedur untuk parent folder
    parser = argparse.ArgumentParser()
    parser.add_argument("Parent_Folder",help="nama parent folder penyimpanan data untuk aplikasi",type=str)
    args  = parser.parse_args()
    path = args.Parent_Folder
    if os.path.exists(path) : 
        print("Folder exist...")
        os.chdir(path)
        print("Parent Folder located....")
        
def load(namaFile:str,n:int) :  #Prosedur load
    f = open(namaFile, 'r') 
    isiFile= f.readline()
    isiFile = str(isiFile)
    x = 0 
    tmpArray = [[""for i in range(n)]for i in range(panjangArray(namaFile))]
    while(isiFile != ""): 
        tmpStr = splitArr(isiFile,n)
        for i in range(n) : 
            tmpArray[x][i] = tmpStr[i]
        x+=1
        isiFile = f.readline()
    print(tmpArray)
    print("Data berhasil di-load")
    return tmpArray
        
def writeFile(namaFile,array,n , m): 
    f = open(namaFile, "w")
    for i in range(n): 
        for j in range(m): 
            if(j == m-1): 
                f.write(array[i][j])
            else :
                f.write(array[i][j]+";") 
        f.write("\n")
    f.close()

def printUser(): 
    print(userFile)

def logOut():
    global userPass,userName 
    if(userPass == "" and userName ==""): 
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu ")
    else : 
        userPass = ""
        userName = ""
        print("Logout berhasil")

def switch(userCommand): 
    if( userCommand == "logout"):
        logOut()
    elif(userCommand =="login"): 
        logIn()
    elif(userCommand == "load"): 
        global userFile, daftarCandi, bahanBangunan 
        userFile = load("user.csv",3)
        daftarCandi = load("candi.csv",5)
        bahanBangunan = load("bahan_bangunan.csv",3)
    elif(userCommand == "break"): 
        global sedangBerjalan 
        sedangBerjalan = False
    elif(userCommand == "summonjin"): 
        summonJin()
    elif(userCommand == "cekuser"):
        printUser()
    elif(userCommand == "hapusjin"):
        hapusJin()

def logIn(): 
    print("Silahkan masukkan username Anda")
    global userName , userPass
    lengthArray = panjangArray("user.csv")
    while True: 
        userName = input(">>>> ")
        if(cekUser(userName,userFile, lengthArray)) : 
            print("Masukkan Password")
            userPass = input(">>>> ")
            if(cekPass(userPass,userFile,lengthArray)):     
                print("Login Berhasil")
                break
            else: 
                print("Password Salah")
        else : 
            print("User Tidak Ditemukan")
        print("Masukkan Username Ulang")

def summonJin(): 
    print("Jenis jin yang dapat dipanggil : ")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n(2) Pembangun - Bertugas membangun candi")
    while True: 
        inputNomer = input("Masukkan nomer jenis jin yang ingin dipanggil : ")
        if(inputNomer == "1" ): 
            print('Memilih jin "Pengumpul"')
            tipeJin = "Pengumpul"
            break
        elif(inputNomer == "2" ): 
            print('Memilih jin "Pembangun"')
            tipeJin = "Pembangun"
            break
        else : 
            print('Tidak ada jenis jin bernomor "%d"' %inputNomer)
    while True: 
        namaJin = input("Masukkan username jin : ")
        if(cekUser(namaJin, userFile,panjangArray("user.csv"))) : 
            print('Username "Genie" sudah diambil! ')
        else: 
            print("Pendaftaran Username berhasil")
            break
    while True : 
        passJin = input("Masukkan password jin : ")
        if(len(passJin) < 5 or length(passJin) > 25): 
            print("Password panjangnya harus 5 - 25 karakter!")
        else : 
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            break
    print("Jin " + namaJin + " berhasil dipanggil")
    arrayTemp = [namaJin, passJin, tipeJin]
    arrayNew = initializeArray(userFile, panjangArray("user.csv"),3,arrayTemp,1)
    writeFile("user.csv",arrayNew,panjangArray("user.csv")+1,3)
    load()

def hapusJin(): 
    while True : 
        namaJin = input("Masukkan username jin : ")
        if( cekUser(namaJin,userFile,panjangArray("user.csv"))) : 
            break 
        else : 
            print("Tidak ada jin dengan username tersebut.")
    while True :
        konfirmasiUser = input("Apakah anda yakin ingin menghapus jin dengan username " +namaJin + "(Y/N)? ")
        if(konfirmasiUser == "Y" or konfirmasiUser =="y") :
            break
        else : 
            return 0
    arrayNew = [["" for i in range(3)] for i in range(panjangArray("user.csv") -1)]
    x = 0
    for i in range(panjangArray("user.csv")):
        for j in range(3): 
            if(userFile[i][0] != namaJin):
                arrayNew[i][j] = userFile[x][j]
        x+=1
    writeFile("user.csv", arrayNew, panjangArray("user.csv")-1 ,3)
    print("Jin "+ namaJin + " berhasil dihapus.")
    load()
    

#Program Utama
memintaArgs()
print("Loading...")
print('Selamat datang di program "Manajerial Candi" ')
 
while sedangBerjalan : 
    x = input(">>>> ")
    switch(x) 

print(userFile)










