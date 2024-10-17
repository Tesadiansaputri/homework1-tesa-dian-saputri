barang = {
    "blender":200000,
    "rice cooker":300000,
    "pisau":20000,
    "wajan":50000,
    "kompor":250000,
    "panci":100000,
}
print("====== Daftar Menu ======")
for i in barang:
    print("Daftar barang : ", i,"Harga :",barang[i])
print("pembelian diatas Rp500.000,- mendapatkan diskon 20%")

beli = input("Pilih barang :  ")
jumlah = int(input("Jumlah barang yang di beli : "))
bayar = jumlah * barang[beli]

if bayar >500000:
    diskon = bayar*20/100
    total = bayar - diskon
else:
    total = bayar
print("Detail Pembayaran")
print("barang yang dibeli       : ",beli)
print("Jumlah yang dibeli      : ",jumlah)
print("Total biaya              : ",bayar)
print("Total yang harus dibayar : ",total)


