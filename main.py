def main():
    while True:
        print("\n=== PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS ===")
        print("1. Lihat Rekap Nilai")
        print("2. Input Nilai Baru")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            print("-> Menampilkan rekap nilai...")
        elif pilihan == "2":
            print("-> Membuka form input nilai...")
        elif pilihan == "3":
            print("Terima kasih sudah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi ya.")

if __name__ == "__main__":
    main()
