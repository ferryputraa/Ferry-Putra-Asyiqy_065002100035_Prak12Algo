myList = []

def searchNumber(List,search):
    counter = 0
    while counter != len(myList):
        if myList[counter] == search:
            result = counter
        counter += 1

print("Linear Search")
jumlah=int(input("Masukkan jumlah angka : "))
for i in range(jumlah):
    i+=1
    myList.append(int(input(f"Angka ke-{i} : ")))
print("\nList angka = ",myList)
cari = int(input("Masukkan angka yang dicari : "))
hasil = searchNumber(myList,cari)
if cari not in myList:
    print("Angka tidak ditemukan")
else:
    print("Angka ditemukan")