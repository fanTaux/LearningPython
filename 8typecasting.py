new_score = float(input("Masukkan nilai baru: "))
score = (90 + 80 + 70.5 + new_score) / 3
print("Nilai rata-rata adalah..." + str(score))

print(min(10, 20, 30, -5, 0))
print(max(10, 20, 30, -5, 0))

#str(x) -> mengubah x menjadi tipe data string
data1 = 32
print(str(data1))
print(type(str(data1)))

#int(x) -< mengubah x menjadi tipe data integer
data2 = 2.78
print(int(data2))
print(type(int(data2)))

#float(x) -> mengubah x menjadi tipe data float
data3 = "18.213"
print(float(data3))
print(type(float(data3)))

#bool(x) -> mengubah x menjadi tipe data boolean
data4 = "mawar"
print(bool(data4))
print(type(bool(data4)))

#abs(x) -> mengubah x menjadi nilai abso
data5 = -15
print(abs(data5))
print(type(abs(data5)))

#round(x) -> mengubah x menjadi pembulatan terdekat
data6 = 9.69
print(round(data6))
print(type(round(data6)))

#round(x, y) -> mengubah x menjadi pembulatan dengan y angka dibelakang koma
data7 = 9.666666
print(round(data7, 1))
print(round(data7, 3))
print(type(round(data7, 1)))
print(type(round(data7, 3)))

#len(x) -> mengubah x menjadi panjang dari x
data8 = "abcdefghij"
print(len(data8))
print(type(len(data8)))

#min(x, y) -> mengembalikan nilai terkecil dari x dan y
data9a = 15
data9b = 20
print(min(data9a, data9b))
print(type(min(data9a, data9b)))

#max(x, y) -> mengembalikan nilai terbesar dari x dan y
data10a = 15
data10b = 20
print(max(data10a, data10b))
print(type(max(data10a, data10b)))

#just to keep the streak running