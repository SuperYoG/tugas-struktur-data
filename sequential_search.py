# Sequential Search untuk mencari huruf A pada nama YOGA
nama = "YOGA"

data = [huruf for huruf in nama]

print("Data:", data)

cari = "A"
ditemukan = False

for i in range(len(data)):
    if data[i] == cari:
        print("Huruf", cari, "ditemukan pada indeks ke-", i)
        ditemukan = True
        break

if not ditemukan:
    print("Huruf tidak ditemukan")
