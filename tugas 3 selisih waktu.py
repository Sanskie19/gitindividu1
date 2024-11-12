#NAMA : MUHAMMAD IHSAN ANSORI
#NIM : 2400409
#KELAS : RPL 1C

def input_waktu():
    while True:
        jam = input("Jam: ")
        menit = input("Menit: ")
        detik = input("Detik: ")

        if jam == "" or menit == "" or detik == "":
            print("Input tidak boleh kosong. Silakan coba lagi.")
            continue

        jam = int(jam)
        menit = int(menit)
        detik = int(detik)

        if 0 <= jam < 24 and 0 <= menit < 60 and 0 <= detik < 60:
            return jam, menit, detik
        else:
            print("Input tidak valid. Harap masukkan jam (0-23), menit (0-59), dan detik (0-59).")

def hitung_selisih_waktu():
    print("Input waktu mulai:")
    jam_mulai, menit_mulai, detik_mulai = input_waktu()

    print("Input waktu selesai:")
    jam_selesai, menit_selesai, detik_selesai = input_waktu()

    total_detik_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_detik_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

    selisih_detik = total_detik_selesai - total_detik_mulai

    jam_selisih = selisih_detik // 3600
    menit_selisih = (selisih_detik % 3600) // 60
    detik_selisih = selisih_detik % 60

    return jam_selisih, menit_selisih, detik_selisih

jam, menit, detik = hitung_selisih_waktu()
print(f"\nSelisih waktu: {jam} jam - {menit} menit - {detik} detik")
print("hello world")