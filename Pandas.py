#Merhaba. Ben Misli Çelik
#Burada Pandas kütüphanesi çalışmalarımı sizlerle paylaşacağım...


#SERİLER


import numpy as np
import pandas as pd

sozlukYas={'Misli':23, 'Kaan':27, 'Nalan':53}

goruntu=pd.Series(sozlukYas)

print(goruntu) #Sıralı ve yan yana şekilde getirir

#


import numpy as np
import pandas as pd

sozlukYas=[23,27,53]
SozlukIsim=['Misli','Kaan','Nalan']

goruntu=pd.Series(sozlukYas, SozlukIsim)

print(goruntu) #Sıralı ve yan yana şekilde getirir


#

import numpy as np
import pandas as pd

sozlukYas=[23,27,53]
SozlukIsim=['Misli','Kaan','Nalan']

goruntu=pd.Series(data=sozlukYas, index=SozlukIsim)

print(goruntu) #Sıralı ve yan yana şekilde getirir

#

import numpy as np
import pandas as pd

sozlukYas=np.array([10,20,30])
SozlukIsim=['Misli','Kaan','Nalan']

goruntu=pd.Series(data=sozlukYas, index=SozlukIsim)

print(goruntu) #Sıralı ve yan yana şekilde getirir

#

import numpy as np
import pandas as pd

sozluk=pd.Series(['Misli', 'Kaan', 'Nalan'])
print(sozluk)

sozluk2=pd.Series(['Misli', 'Kaan', 'Nalan'], [1,2,3])
print(sozluk2)

#

import numpy as np
import pandas as pd

sinav1=pd.Series([88,76,84],['Misli', 'Kaan', 'Nalan'])
sinav2=pd.Series([94,100,91],['Misli', 'Kaan', 'Nalan'])
 
sonuc=sinav1+sinav2
print(sonuc)

sonuc2=sinav1*sinav2
print(sonuc2)

sonuc3=sinav1*0.3+sinav2*0.7
print(sonuc3)

#

import numpy as np
import pandas as pd

sinav1=pd.Series([88,76,84],['Misli', 'Kaan', 'Nalan'])
sinav2=pd.Series([94,100,91],['Misli', 'Ayşe', 'Fatma'])
 
sonuc=sinav1+sinav2
print(sonuc)

sonuc2=sinav1*sinav2
print(sonuc2)

sonuc3=sinav1*0.3+sinav2*0.7
print(sonuc3)
# Burada kesişmeyen değerler NaN olarak karşımıza çıkmaktadır.



#DATA FRAME


import numpy as np
import pandas as pd

data=np.random.randn(3,4)

print(data)

dataFrame=pd.DataFrame(data) #bir tablo gibi gözükmesi için kullanıldı

print(dataFrame) 

index=dataFrame[0] #Kolon olarak seçer

print(index)

#

import numpy as np
import pandas as pd

data=np.random.randn(4,3)

print(data)

dataFrame=pd.DataFrame(data) #bir tablo gibi gözükmesi için kullanıldı

print(dataFrame) 

index=dataFrame[0] #Kolon olarak seçer

print(index)

dataFrame2=pd.DataFrame(data, index=['Misli', 'Kaan', 'Kenan', 'Nalan'], columns=['Yüzde', 'Kar', 'Zarar'])

print(dataFrame2)

istenen=dataFrame2.loc['Misli'] #kolonları getirir

print(istenen)

istenen2=dataFrame2.iloc[1] #Yine Misliyi kolon olarak getirir

print(istenen2)

dataFrame2['Zam']=dataFrame2['Yüzde']*dataFrame2['Zarar']

print(dataFrame2['Zam'])

drop=dataFrame2.drop['Zam', axis=1]

print(drop)

drop2=dataFrame2.drop['Misli']

print(drop2)

istenen3=dataFrame2.loc['Misli']['Kar']

print(istenen3)

esitlik=dataFrame2[dataFrame2['Zam']<0]

print(esitlik)

reset=dataFrame2.reset_index()

print(reset) #indexleri resetler

#

import numpy as np
import pandas as pd

index1=['Öğrenci', 'Öğrenci', 'Öğrenci', 'Mezun', 'Mezun', 'Mezun']
index2=['Ayşe', 'Ahmet', 'Mehmet', 'Fatma', 'Ceren', 'Ali']

birlestir=list(zip(index1, index2))
birlesmis=pd.MultiIndex.from_tuples(birlestir)

index3=[[40,10],[10,30],[45,23],[15,36],[32,44],[18,21]]
index3Numpy=np.array(index3)

tabloDataFrame=pd.DataFrame(index3Numpy, index=birlesmis, columns=['Sıra', 'Sınıf'])

print(tabloDataFrame)

#

import numpy as np
import pandas as pd

veri={'Ankara':[30,40,50], 'Konya':[40,np.nan,19], 'Bursa':[15,np.nan,32]}
dataFrame=pd.DataFrame(veri,['pazartesi', 'salı', 'Çarşamba'])

print(dataFrame)

sil=dataFrame.dropna()

print(sil)

sil2=dataFrame.dropna(axis=1)

print(sil2)

sil3=dataFrame.dropna(axis=1, thresh=2)

print(sil3)

doldur=dataFrame.fillna(100)

print(doldur) #NaN değerleri 100 ile doldurdu


#GroupBy


import numpy as np
import pandas as pd

veri={'Bölüm': ['İstatistik', 'Bilgisayar Mühendisliği', 'Bilgisayar Mühendisliği', 'İstatistik', 'Fizik','Fizik'],
      'Öğrenci İsmi': ['Misli', 'Can', 'Erhan', 'Duygu', 'Merve', 'Nisa'],
      'Notlar': [93,91,86,85,79,76]
}

dataFrame=pd.DataFrame(veri, ['1.', '2.', '3.', '4.', '5.', '6.'])

print(dataFrame)

grup=dataFrame.groupby('Bölüm')

say=grup.count()

print(say)

ortalama=grup.mean()

print(ortalama)

min=grup.min()

print(min)

max=grup.max()

print(max)

des=grup.describe()

print(des) #Tüm Özellikleri hesaplar


#

import numpy as np
import pandas as pd

veri1={'Bölüm': ['İstatistik', 'Bilgisayar Mühendisliği', 'Bilgisayar Mühendisliği', 'İstatistik', 'Fizik','Fizik'],
      'Öğrenci İsmi': ['Misli', 'Can', 'Erhan', 'Duygu', 'Merve', 'Nisa'],
      'Notlar': [93,91,86,85,79,76]
}

veri2={'Bölüm': ['İstatistik', 'Yazılım Mühendisliği', 'Bilgisayar Mühendisliği', 'İstatistik', 'Kimya','Fizik'],
      'Öğrenci İsmi': ['İlayda', 'Oğulcan', 'Erdem', 'Derya', 'Meryem', 'Nergis'],
      'Notlar': [98,94,87,81,78,69]
}

veri3={'Bölüm': ['İstatistik', 'Bilgisayar Mühendisliği', 'Makine Mühendisliği', 'İstatistik', 'Matematik','Fizik'],
      'Öğrenci İsmi': ['Aleyna', 'Cenk', 'Mutlu', 'Serkan', 'Melek', 'Deniz'],
      'Notlar': [99,97,83,74,65,53]
}


dataFrame1=pd.DataFrame(veri1, ['1.', '2.', '3.', '4.', '5.', '6.'])

print(dataFrame1)

dataFrame2=pd.DataFrame(veri2, ['7.', '8.', '9.', '10.', '11.', '12.'])

print(dataFrame2)

dataFrame3=pd.DataFrame(veri3, ['13.', '14.', '15.', '16.', '17.', '18.'])

print(dataFrame3)


birlestir=pd.concat([dataFrame1, dataFrame2, dataFrame3])

print(birlestir)


#Merge


import numpy as np
import pandas as pd

veri1={'Bölüm': ['İstatistik', 'Bilgisayar Mühendisliği', 'Bilgisayar Mühendisliği', 'İstatistik', 'Fizik','Fizik'],
      'Öğrenci İsmi': ['Misli', 'Can', 'Erhan', 'Duygu', 'Merve', 'Nisa'],
      'Notlar1': [93,91,86,85,74,72]
}

veri2={'Bölüm': ['İstatistik', 'Bilgisayar Mühendisliği', 'Bilgisayar Mühendisliği', 'İstatistik', 'Fizik','Fizik'],
      'Öğrenci İsmi': ['Ahmet', 'Canan', 'Erdem', 'Derya', 'Meral', 'Ayşe'],
      'Notlar2': [95,97,89,86,79,76]
}


dataFrame1=pd.DataFrame(veri1, ['1.', '2.', '3.', '4.', '5.', '6.'])

dataFrame2=pd.DataFrame(veri2, ['1.', '2.', '3.', '4.', '5.', '6.'])

merge=pd.merge(dataFrame1,dataFrame2, on='Bölüm')
print(merge)

#

import numpy as np
import pandas as pd
from pandas.core.algorithms import value_counts

veri={'Bölüm': ['İstatistik', 'Bilgisayar Mühendisliği', 'Bilgisayar Mühendisliği', 'İstatistik', 'Fizik','Fizik'],
      'Öğrenci İsmi': ['Misli', 'Can', 'Erhan', 'Duygu', 'Merve', 'Nisa'],
      'Notlar': [93,91,86,85,74,72]
}


dataFrame=pd.DataFrame(veri, ['1.', '2.', '3.', '4.', '5.', '6.'])

unique=dataFrame['Bölüm'].unique()
print(unique) #tekilleri getirir. Aynı verileri tek biri veri olarak getirir

nunique=dataFrame['Bölüm'].nunique()
print(nunique) #tekilleri sayısal olarak getirir. Yani kaç tane farklı değer varsa sayısını bize verir

value_count=dataFrame['Bölüm'].value_counts()
print(value_count) #Her birinden kaç tane volduğunu bize gösterir

def NotlariCarp(Notlar):
    return Notlar*0.70

carpim=dataFrame['Notlar'].apply(NotlariCarp)
print(carpim)

null=dataFrame.isnull()
print(null) #Null değer olmayanlara False yazılır

pivot=dataFrame.pivot_table(
    values='Notlar', index=['Bölüm', 'Öğrenci İsmi'], aggfunc=np.sum #aynı isim varsa toplar
)
print(pivot)