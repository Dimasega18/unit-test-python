import pandas as pd
import re

class tabel_laki():

    def __init__(self) -> None:
        df = pd.read_csv('.\Persentase penduduk usia 25 Tahun keatas dengan pendidikan SMA .csv')
        df_new = df.copy().iloc[3:,:].reset_index().iloc[:,1:8]

        df_laki = df_new.iloc[:,0:4]
        df_laki['Jenis Kelamin'] = "Laki-laki"
        self.__df = df_laki

    def tabel(self):
        x = self.__df.rename(columns={'Unnamed: 1':'2021','Unnamed: 2':'2022','Unnamed: 3':'2023'})
        return x

    def tahun_2021 (self):
        x = self.__df.rename(columns={'Unnamed: 1':'Persentase'}).iloc[:,[0,1,4]]
        x['Tahun'] = "2021"
        return x
    
    def tahun_2022 (self):
        x = self.__df.rename(columns={'Unnamed: 2':'Persentase'}).iloc[:,[0,2,4]]
        x['Tahun'] = "2022"
        return x

    def tahun_2023 (self):
        x = self.__df.rename(columns={'Unnamed: 3':'Persentase'}).iloc[:,[0,3,4]]
        x['Tahun'] = "2023"
        return x
    
    def only_province(self):
        nama = self.tabel()['Provinsi/Kabupaten/Kota'].values
        data = []
        
        for x in nama :
            data.append(bool(re.search('[!"#$%&\'()*+,-\./:;<=>?@[\\]^_`{|}~]',x)))
        nama_unik = self.tabel().loc[data]
        
        provinsi_unik = nama_unik.loc[(nama_unik['Provinsi/Kabupaten/Kota'] == 'KEP. BANGKA BELITUNG' )]
        provinsi = [True if (x.isupper()) else False for x in self.tabel()['Provinsi/Kabupaten/Kota']]
        
        x = self.tabel().loc[provinsi]._append(provinsi_unik,ignore_index=True).drop_duplicates()
        return x.loc[(x['Provinsi/Kabupaten/Kota'].values != 'INDONESIA' )].rename(columns = {'Provinsi/Kabupaten/Kota':'Provinsi'})
    
    def city_regency(self):
        nama = self.tabel()['Provinsi/Kabupaten/Kota'].values
        data = []
        
        for x in nama :
            data.append(bool(re.search('[!"#$%&\'()*+,-\./:;<=>?@[\\]^_`{|}~]',x)))
        nama_unik = self.tabel().loc[data]
        
        kota_kab_unik = nama_unik.loc[~(nama_unik['Provinsi/Kabupaten/Kota'] == 'KEP. BANGKA BELITUNG' )]
        kota_kab = [True if ((x.istitle()) or not (x.isupper()))  else False for x in self.tabel()['Provinsi/Kabupaten/Kota']]

        x = self.tabel().loc[kota_kab]._append(kota_kab_unik,ignore_index=True).drop_duplicates().rename(columns = {'Provinsi/Kabupaten/Kota':'Kabupaten & Kota'})
        return x

        
    
class tabel_perempuan():

    def __init__(self) -> None:
        df = pd.read_csv('.\Persentase penduduk usia 25 Tahun keatas dengan pendidikan SMA .csv')
        df_new = df.copy().iloc[3:,:].reset_index().iloc[:,1:8]

        df_perempuan = df_new.iloc[:,[0,4,5,6]]
        df_perempuan['Jenis Kelamin'] = 'Perempuan'
        self.__df = df_perempuan

    def tabel(self):
        x = self.__df.rename(columns={'Unnamed: 4':'2021','Unnamed: 5':'2022','Unnamed: 6':'2023'})
        return x

    def tahun_2021 (self):
        x = self.__df.rename(columns={'Unnamed: 4':'Persentase'}).iloc[:,[0,1,4]]
        x['Tahun'] = "2021"
        return x
    
    def tahun_2022 (self):
        x =self.__df.rename(columns={'Unnamed: 5':'Persentase'}).iloc[:,[0,2,4]]
        x['Tahun'] = "2022"
        return x

    def tahun_2023 (self):
        x = self.__df.rename(columns={'Unnamed: 6':'Persentase'}).iloc[:,[0,3,4]]
        x['Tahun'] = "2023"
        return x
    
    def only_province(self):
        nama = self.tabel()['Provinsi/Kabupaten/Kota'].values
        data = []
        for x in nama :
            data.append(bool(re.search('[!"#$%&\'()*+,-\./:;<=>?@[\\]^_`{|}~]',x)))
        nama_unik = self.tabel().loc[data]
        
        provinsi_unik = nama_unik.loc[(nama_unik['Provinsi/Kabupaten/Kota'] == 'KEP. BANGKA BELITUNG' )]
        provinsi = [True if x.isupper() else False for x in self.tabel()['Provinsi/Kabupaten/Kota']]
        
        x = self.tabel().loc[provinsi]._append(provinsi_unik,ignore_index=True).drop_duplicates().rename(columns = {'Provinsi/Kabupaten/Kota':'Provinsi'})
        return x.loc[(x['Provinsi'].values != 'INDONESIA' )]
    
    def city_regency(self):
        nama = self.tabel()['Provinsi/Kabupaten/Kota'].values
        data = []
        
        for x in nama :
            data.append(bool(re.search('[!"#$%&\'()*+,-\./:;<=>?@[\\]^_`{|}~]',x)))
        nama_unik = self.tabel().loc[data]
        
        kota_kab_unik = nama_unik.loc[~(nama_unik['Provinsi/Kabupaten/Kota'] == 'KEP. BANGKA BELITUNG' )]
        kota_kab = [True if ((x.istitle()) or not (x.isupper()))  else False for x in self.tabel()['Provinsi/Kabupaten/Kota']]

        x = self.tabel().loc[kota_kab]._append(kota_kab_unik,ignore_index=True).drop_duplicates().rename(columns = {'Provinsi/Kabupaten/Kota':'Kabupaten & Kota'})
        return x

if __name__ == '__main__':
    df = tabel_perempuan()
    print(df.only_province().shape)