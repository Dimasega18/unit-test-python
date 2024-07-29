import unittest
import main

class test_data(unittest.TestCase):

    def test_total_tabel(self):
        
        x = main.tabel_laki().only_province().shape[0]
        y = main.tabel_laki().city_regency().shape[0]
        z = x + y
        
        self.assertEqual(main.tabel_laki().tabel().shape,main.tabel_perempuan().tabel().shape)
        self.assertEqual(main.tabel_laki().tahun_2021().shape,main.tabel_perempuan().tahun_2021().shape)
        self.assertEqual(main.tabel_laki().tahun_2022().shape,main.tabel_perempuan().tahun_2022().shape)
        self.assertEqual(main.tabel_laki().tahun_2023().shape,main.tabel_perempuan().tahun_2023().shape)
        self.assertEqual(main.tabel_laki().tahun_2023().shape,main.tabel_perempuan().tahun_2023().shape)
        self.assertEqual(main.tabel_laki().only_province().shape,main.tabel_perempuan().only_province().shape)
        self.assertEqual(main.tabel_laki().city_regency().shape,main.tabel_perempuan().city_regency().shape)
        self.assertEqual(z,548)

        x = main.tabel_perempuan().only_province().shape[0]
        y = main.tabel_perempuan().city_regency().shape[0]
        z = x + y
        
        self.assertEqual(z,548)


if __name__ == '__main__':
    unittest.main()

