import os

# Struktur folder dan file yang mau dibuat
struktur = {
    "src": ["__init__.py", "analisis.py", "input_nilai.py"],
    "tests": ["__init__.py", "test_analisis.py"],
}

# Membuat folder utama dan file di dalamnya
os.makedirs("src", exist_ok=True)
os.makedirs("tests", exist_ok=True)

# Membuat file utama main.py
main_code = '''def main():
    while True:
        print("\\n=== PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS ===")
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
'''

with open("main.py", "w", encoding="utf-8") as f:
    f.write(main_code)

# Membuat file kosong untuk src dan tests
for folder, files in struktur.items():
    for file in files:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("# " + file + "\n")

print("Mantap! Semua folder dan file proyek berhasil dibuat otomatis!")