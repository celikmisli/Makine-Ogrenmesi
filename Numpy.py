#Merhaba... Sizlerle Numpy komutları ve örnekleri paylaşacağım..

import numpy as np

benimListem=[2,3,4]

list= np.array(benimListem)

print(list) #array olarak getirir

print(type(list)) #bizlere tipini getirir

#

import numpy as np

list=np.array(range(0,10))
print(list) # array([0,1,2,3,4,5,6,7,8,9])

liste=np.array(range(0,10,2))
print(liste) # array([0,2,4,6,8]) 2'şer atlattık.

#

import numpy as np

list=np.zeros(25)
print(list) #25 tane 0 değeri getirdi

liste=np.zeros((15,10))
print(liste) #15x10'luk matris şeklinde 0'ları getirdi

#


import numpy as np

list=np.ones(25)
print(list) #25 tane 1 değeri getirdi

liste=np.ones((15,10))
print(liste) #15x10'luk matris şeklinde 1'lerı getirdi

#

import numpy as np

list=np.linspace(0,10,10)
print(list) #10 tane değeri aralarında eşit boşluklar olacak şekilde bize getirdi

#

import numpy as np

list=np.eye(3)
print(list) #4'e 4'lük bir simetrik 0 ile 1lerden oluşan birim matris getirdi.

#

import numpy as np

list=np.random.randn(3)
print(list) #[-1.19541508  0.79262619 -0.29558662]

liste=np.random.randn(5,5)
print(liste) #5x5'lik matris şeklinde getirir


#

import numpy as np

list=np.random.randint(1,5)
print(list) #İstenen sayı aralığında int bir sayı döndürür

liste=np.random.randint(5,20,4)
print(liste) #5 ile 20 arasında 4 tane int sayı getirir

#

import numpy as np

dizi=np.random.randint(1,200,20)
print(dizi) #1 den 100'e kadar olan sayılardan rastgele 20 tane getirdi

dizim=dizi.reshape(4,5)
print(dizim) #dizi listesini 4x5 matris şeklinde getirdi

max=dizim.max()
print(max) # en büyük sayıyı getirdi

min=dizim.min()
print(min) # en küçük sayıyı getirdi

argmax=dizim.argmax()
print(argmax) # en büyük sayıyının indexini getirdi

argmin=dizim.argmin()
print(argmin) # en küçük sayıyının indexini getirdi

#

import numpy as np

dizi=np.arange(50,100)

index=dizi[3:15]

index2=index-5

print(dizi)
#[50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 
# 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]
print(index) 
#[53 54 55 56 57 58 59 60 61 62 63 64]
print(index2)
#[48 49 50 51 52 53 54 55 56 57 58 59]

#

import numpy as np

dizi=np.arange(50,100)

index=dizi[4:8]

dizim=dizi.copy()

indexx=dizim==10

print(indexx)
#Dizimizi değiştirmeden işlem yapmak için copy işlemi kullanılabilir

#

import numpy as np

dizim=[[1,2,3],[4,5,6],[7,8,9]]

dizimMatris=np.array(dizim)

print(dizimMatris) #böylece bir matris ataması yapmış olduk

#

import numpy as np

dizim=[[1,2,3],[4,5,6],[7,8,9]]

dizimMatris=np.array(dizim)
print(dizimMatris) #böylece bir matris ataması yapmış olduk

index=dizimMatris[2]
print(index)

index2=dizimMatris[2][2] #9
print(index2)

index3=dizimMatris[0:3] 
print(index3)

index4=dizimMatris[[0,2]] 
print(index4) #indexleri 0 ve 2 olanları getirir

#


import numpy as np

dizim=np.random.randint(1,100,10)
print(dizim)

dizim2=dizim>35
print(dizim2) #true false şeklinde değerler getirir

dizim3=dizim[dizim2]
print(dizim3) #dizim2'nin sayı halini getirir

dizim4=dizim[dizim>35]
print(dizim4) #dizim3 ile aynı sonucu verir

#

import numpy as np

dizim=np.arange(0,50)
print(dizim)

baskaDizi=dizim+dizim
print(baskaDizi)

baskaDizi2=dizim-dizim
print(baskaDizi2)

baskaDizi3=dizim*dizim
print(baskaDizi3)

baskaDizi4=dizim/dizim
print(baskaDizi4)

baskaDizi5=np.sqrt(dizim)
print(baskaDizi5) #Kareköklerini aldık
