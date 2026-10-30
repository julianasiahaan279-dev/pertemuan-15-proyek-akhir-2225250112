def input_data_nilai():
    print("\n=== INPUT NILAI BARU ===")
    try:
        nama = input("Masukkan nama siswa: ")
        nilai = float(input("Masukkan nilai matematika: "))
        if nilai < 0 or nilai > 100:
            print("Nilai harus berada di antara 0 sampai 100!")
            return None
        return {"nama": nama, "nilai": nilai}
    except ValueError:
        print("Input nilai harus berupa angka!")
        return None
