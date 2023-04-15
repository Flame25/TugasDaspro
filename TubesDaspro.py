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
seed : int = 0
totalBatu : int = 0
totalPasir : int = 0
totalAir : int = 0

#Kumpulan Fungsi 

def panjangFile(namaFile): 
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
    
    for i in range(n2): 
        for j in range(m): 
            newArray[i + n][j] = array2[j]

    return newArray
def initializeArray2 (array : list, n :int, m:int, array2:list , n2:int) : 
    newArray = [["" for i in range(m)] for i in range(n+n2)]
    for i in range(n): 
        for j in range(m): 
            newArray[i][j] = array[i][j]

    for i in range(n2): 
        for j in range(m): 
            newArray[i + n][j] = array2[i][j]

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
    tmpArray = [[""for i in range(n)]for i in range(panjangFile(namaFile))]
    while(isiFile != ""): 
        tmpStr = splitArr(isiFile,n)
        for i in range(n) : 
            tmpArray[x][i] = tmpStr[i]
        x+=1
        isiFile = f.readline()
    print(tmpArray)
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
        if(panjangFile("bahan_bangunan.csv")>1): loadBahanBangunan()
    elif(userCommand == "break"): 
        global sedangBerjalan 
        sedangBerjalan = False
    elif(userCommand == "summonjin"): 
        summonJin()
    elif(userCommand == "cekuser"):
        printUser()
    elif(userCommand == "hapusjin"):
        hapusJin()
    elif(userCommand == "save"): 
        save()
    elif(userCommand == "ubahjin"): 
        ubahTipeJin()
    elif(userCommand == "ayamberkokok"): 
        ayamBerkokok()
    elif(userCommand == "kumpul"): 
        Kumpul()
    elif(userCommand == "bangun"): 
        Bangun()
    elif(userCommand == "exit"): 
        Exit()
    elif(userCommand == "help"): 
        Help()
    elif(userCommand == "hancurkancandi"):
        hancurkanCandi()

def logIn(): 
    print("Silahkan masukkan username Anda")
    global userName , userPass
    lengthArray = panjangFile("user.csv")
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
        if(cekUser(namaJin, userFile,panjangFile("user.csv"))) : 
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
    arrayNew = initializeArray(userFile, panjangFile("user.csv"),3,arrayTemp,1)
    writeFile("user.csv",arrayNew,panjangFile("user.csv")+1,3)
    loadUserFile()

def loadBahanBangunan(): 
    global totalBatu,totalAir,totalPasir, bahanBangunan
    bahanBangunan = load("bahan_bangunan.csv",3)
    if(panjangFile("bahan_bangunan.csv") > 1): 
        totalPasir = int(bahanBangunan[1][2])
        totalBatu = int(bahanBangunan[2][2])
        totalAir = int(bahanBangunan[3][2])
    print("Daftar bahan bangunan berhasil di-load")

def loadUserFile():
    global userFile 
    userFile = load("user.csv",3)
    print("Daftar user berhasil di-load")

def loadDaftarCandi(): 
    global daftarCandi 
    daftarCandi = load("candi.csv",5)
    print("Daftar candi berhasil di-load")

def lcg(a : int , c: int, m: int ) -> int : # X = (a*x + c) mod m 
    global seed 
    hasilLCG = (a*seed + c) % m
    seed = hasilLCG
    return hasilLCG %6

def save(): 
    panjangFileUser = panjangFile("user.csv")
    panjangFileBahan = panjangFile("bahan_bangunan.csv")
    panjangFIleCandi = panjangFile("candi.csv")
    namaFolder = input("Masukklan nama folder : ")
    print("Saving...")
    if not os.path.exists("save"): 
        os.mkdir("save")

    namaFolder= "save/"+namaFolder
    if os.path.exists(namaFolder): 
        os.chdir(namaFolder)
    else : 
        print("Membuat folder " + namaFolder)
        os.mkdir(namaFolder)
        os.chdir(namaFolder)
    writeFile("user.csv", userFile , panjangFileUser,3 )
    writeFile("bahan_bangunan.csv",bahanBangunan, panjangFileBahan,3 )
    writeFile("candi.csv", daftarCandi, panjangFIleCandi,5 )
    os.chdir("../")   #Keluar dari folder save
    os.chdir("../")   #Keluar dari folder parent save
    print("Berhasil menyimpan data di folder " + namaFolder + " !")    

def getJin(userName): 
    arrayJin = ["" for i in range(3)]
    for i in range(panjangFile("user.csv")): 
        for j in range(3): 
            if(userFile[i][0] == userName ): 
                arrayJin = [i]
    return arrayJin
 
def ubahTipeJin():
    while True  : 
        userNameJin = input("Masukkan username jin : ")
        if( cekUser(userNameJin)) : 
            break 
        else : 
            print("Tidak ada jin dengan username tersebut.")
    arrayJin = getJin(userNameJin)
    while True :
        if(arrayJin[2] == "Pengumpul"): 
            konfirmasiUser = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
        elif(arrayJin[2] == "Pembangung"): 
            konfirmasiUser = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ')
        else : 
            print("Error")
            return 0
        if(konfirmasiUser == "Y" or konfirmasiUser =="y"): 
            break
        else : 
            return 0 
        
    for i in range(panjangFile("user.csv")):
        if(userFile[i][0] == userNameJin):
            if(arrayJin[2] == "Pembangun"): 
                userFile[i][2] = "Pengumpul"
            else : 
                userFile[i][2] ="Pembangun"
    writeFile("user.csv", userFile,panjangFile("user.csv"), 3)
    print("Tipe jin berhasil diubah")
    loadUserFile()
    return 0 
    
def hapusJin(): 
    while True : 
        namaJin = input("Masukkan username jin : ")
        if( cekUser(namaJin,userFile,panjangFile("user.csv"))) : 
            break 
        else : 
            print("Tidak ada jin dengan username tersebut.")
    while True :
        konfirmasiUser = input("Apakah anda yakin ingin menghapus jin dengan username " +namaJin + "(Y/N)? ")
        if(konfirmasiUser == "Y" or konfirmasiUser =="y") :
            break
        else : 
            return 0
    arrayNew = [["" for i in range(3)] for i in range(panjangFile("user.csv") -1)]
    x = 0
    for i in range(panjangFile("user.csv")):
        for j in range(3): 
            if(userFile[i][0] != namaJin):
                arrayNew[i][j] = userFile[x][j]
        x+=1
    writeFile("user.csv", arrayNew, panjangFile("user.csv")-1 ,3)
    print("Jin "+ namaJin + " berhasil dihapus.")
    loadUserFile()
    
def ayamBerkokok(): 
    print("Kukuruyuk.. Kukuruyuk..\n")
    print("Jumlah candi : " + str(panjangFile("candi.csv") -1) +"\n")
    if(panjangFile("candi.csv") -1 == 100): 
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else : 
        
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("\n")
        print("*Bandung Bondowoso angry noise* \nRoro Jonggrang dikutuk menjadi candi.")

def Kumpul(): 
    global totalBatu, totalPasir, totalAir, bahanBangunan
    nPasir = lcg(151811,3112,50603)
    nBatu =lcg(151813,3112,50603)
    nAir = lcg(1518019,3112,50605)   
    totalBatu += nBatu
    totalAir += nAir
    totalPasir += nPasir
    print("Jin menemukan " + str(nPasir) + " pasir "  + str(nBatu) + " batu " + str(nAir) + " air")
    arrayTemp = [["Pasir","sebuah pasir",str(nPasir)], ["Batu","sebuah batu", str(nBatu)], ["Air", "sebuah air", str(nAir)]]
    if(panjangFile("bahan_bangunan.csv") == 1): 
        print(bahanBangunan)
        arrayNew = initializeArray2(bahanBangunan,1, 3, arrayTemp, 3)
        writeFile("bahan_bangunan.csv", arrayNew, 4 , 3)
    else : 
        bahanBangunan[1][2] = str(totalPasir)
        bahanBangunan[2][2] = str(totalBatu)
        bahanBangunan[3][2] = str(totalAir)
        writeFile("bahan_bangunan.csv", bahanBangunan, panjangFile("bahan_bangunan.csv"),3)
    loadBahanBangunan()
def cekId(id:int): 
    for i in range(panjangFile("candi.csv")): 
        if(id == daftarCandi[i][0]): 
            return True
    return False

def hancurkanCandi(): 
    while True : 
        idCandi = input("Masukkan id candi: ")
        if(cekId(idCandi)) : 
            break
        else : 
            print("Tidak ada candi dengan id  " +  idCandi)
    while True : 
        konfirmasiUser = input("Apakah anda yakin ingin menghancurkan candi ID: "+ idCandi+ "  (Y/N)? ") 
        if(konfirmasiUser == "y" or konfirmasiUser =="Y"): 
            break; 
        else: 
            return 0
    arrayNew = [["" for i in range(5)] for i in range(panjangFile("candi.csv") -1)]
    x = 0
    for i in range(panjangFile("candi.csv") -1 ):
        if(daftarCandi[i][0] == idCandi):
            x+=1
        for j in range(5): 
                arrayNew[i][j] = daftarCandi[x][j]
        else : x += 1
    print(arrayNew)
    writeFile("candi.csv", arrayNew, panjangFile("candi.csv")-1 ,5)
    print("Candi dengan id " + idCandi + " berhasil dihapus")
    loadDaftarCandi()
    
def Bangun(): 
    global totalPasir, totalBatu, totalAir, daftarCandi, bahanBangunan
    nPasir = lcg(151873,3112,50603)
    nBatu =lcg(151879,3112,50603)
    nAir = lcg(151837,3112,50603)
    print("Bahan yang diperlukan : " + str(nPasir) + " pasir, " + str(nBatu) + " batu, " + str(nAir) +" air")
    if(nPasir <= totalPasir and nAir <= totalAir and nBatu <= totalBatu): 
        print("Candi berhasil dibangun.")
        sisaCandi =100 - panjangFile("candi.csv") +1
        print("Sisa candi yang perlu dibangun: " + str(sisaCandi))
        totalPasir -= nPasir
        totalAir -= nAir
        totalBatu -= nBatu
        idCandi = 0
        for i in range(1,panjangFile("candi.csv")): 
            if(i == panjangFile("candi.csv") -1  or i != int(daftarCandi[i][0]) ): 
                idCandi = i
        arrayTemp = [str(idCandi), userName, str(nPasir), str(nBatu),str(nAir)]
        if(panjangFile("candi.csv") -1 < 100): 
            arrayNew = initializeArray(daftarCandi, panjangFile("candi.csv"),5, arrayTemp,1)
            writeFile("candi.csv", arrayNew, panjangFile("candi.csv") + 1, 5)
            bahanBangunan[1][2] = str(totalPasir)
            bahanBangunan[2][2] = str(totalBatu)
            bahanBangunan[3][2] = str(totalAir)
            writeFile("bahan_bangunan.csv", bahanBangunan, panjangFile("bahan_bangunan.csv"), 3)
            loadBahanBangunan()
            loadDaftarCandi()
    else  : 
        print("Bahan bangunan tidak mencukupi")
        print("Candi tidak bisa dibangun!")
def Exit(): 
    panjangFileUser = panjangFile("user.csv")
    panjangFileBahan = panjangFile("bahan_bangunan.csv")
    panjangFIleCandi = panjangFile("candi.csv")
    while True :
        konfirmasiUser = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if(konfirmasiUser == "Y" or konfirmasiUser =="y"): 
            writeFile("user.csv", userFile , panjangFileUser,3 )
            writeFile("bahan_bangunan.csv",bahanBangunan, panjangFileBahan,3 )
            writeFile("candi.csv", daftarCandi, panjangFIleCandi,5 )
            break
        elif(konfirmasiUser == "n" or konfirmasiUser =="N") : 
            break

    sys.exit()
def Help(): 
    print("=========== HELP ===========")
    if(userName == "" and userPass == ""): 
        print("1. Login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif(userName == "Bondowoso"): 
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
    elif(userName == "Roro") : 
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")

#Program Utama
memintaArgs()
print("Loading...")
print('Selamat datang di program "Manajerial Candi" ')

loadUserFile()
loadBahanBangunan()
loadDaftarCandi()

while sedangBerjalan : 
    x = input(">>>> ")
    switch(x) 
