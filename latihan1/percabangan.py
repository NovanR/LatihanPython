# lulus = input("Apakah si diaz jago main ml? [ya/tidak]")

# if lulus == "tidak":
#     print("Si diaz turu");

# if lulus == "ya":
#     print("Si diaz jago");

a = 10000
print ("Masukkan total belanja: Rp ")
total_belanja = input()
bayar = total_belanja

if total_belanja > a :
    print("kamu mendapatkan diskon 10%")

# perhitungan diskon
    diskon = (total_belanja * 10) / 100
    bayar = total_belanja - diskon

print ("Total yang harus dibayar" + bayar)


