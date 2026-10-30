import unittest
from src.analisis import hitung_rata_rata, tentukan_predikat

class TestAnalisisNilai(unittest.TestCase):
    
    def test_hitung_rata_rata(self):
        daftar_nilai = [80, 90, 70]
        self.assertEqual(hitung_rata_rata(daftar_nilai), 80.0)

    def test_tentukan_predikat(self):
        self.assertEqual(tentukan_predikat(85), "A")
        self.assertEqual(tentukan_predikat(75), "B")
        self.assertEqual(tentukan_predikat(65), "C")
        self.assertEqual(tentukan_predikat(50), "D")

if __name__ == "__main__":
    unittest.main()
