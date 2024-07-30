import unittest
import main

class test_data(unittest.TestCase):

    def test_column_row_table(self):
        
        x = main.tabel_laki().only_province().shape[0]
        y = main.tabel_laki().city_regency().shape[0]
        z = x + y
        
        self.assertEqual(main.tabel_laki().tabel().shape[0],549)
        self.assertEqual(main.tabel_laki().tabel().shape[1],5)
        self.assertEqual(main.tabel_perempuan().tabel().shape[0],549)
        self.assertEqual(main.tabel_perempuan().tabel().shape[1],5)

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

    def test_table_type(self):
        
        self.assertEqual(main.tabel_laki().tabel()['Provinsi/Kabupaten/Kota'].dtype,"object")
        self.assertEqual(main.tabel_laki().tabel()['Jenis Kelamin'].dtype,"object")
        self.assertEqual(main.tabel_laki().tabel()['2021'].dtype,"float64")
        self.assertEqual(main.tabel_laki().tabel()['2022'].dtype,"float64")
        self.assertEqual(main.tabel_laki().tabel()['2023'].dtype,"float64")

        self.assertEqual(main.tabel_perempuan().tabel()['Provinsi/Kabupaten/Kota'].dtype,"object")
        self.assertEqual(main.tabel_perempuan().tabel()['Jenis Kelamin'].dtype,"object")
        self.assertEqual(main.tabel_perempuan().tabel()['2021'].dtype,"float64")
        self.assertEqual(main.tabel_perempuan().tabel()['2022'].dtype,"float64")
        self.assertEqual(main.tabel_perempuan().tabel()['2023'].dtype,"float64")

if __name__ == '__main__':
    unittest.main()

