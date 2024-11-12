#NAMA : MUHAMMAD IHSAN ANSORI
#NIM : 2400409
#KELAS : RPL 1C

#bisa menggunakan angka bilangan bulat, contoh : 10, 20, 30
#bisa menggunakan angka desimal, contoh : 2.5, 3.5(pada desimmal gunakan titik karena kalau koma input tidak valid)

print("selamat datang di aplikasi rata rata")
def hitung_total_dan_rata_rata():
    nilai = []
    
    while True:
        inp = input("Masukkan nilai atau jika nilai yang dimasukkan sudah cukup ketik selesai: ")
        
        if inp.lower() == "selesai":
            break
        
        if inp.replace('.', '', 1).isdigit():  
            nilai.append(float(inp)) 
        else:
            print("Input tidak valid, silakan masukkan angka atau 'selesai'.")

    
    total = sum(nilai)  
    rata_rata = total / len(nilai) if len(nilai) > 0 else 0 
    
    return total, rata_rata

total, rata_rata = hitung_total_dan_rata_rata()
print("Total:", total)
print("Rata-rata:", rata_rata)