import numpy as np

("""
1) 0-29 arası(29 dahil, toplam 30 tam sayı) tam sayılardan oluşan bir boyutlu bir array oluşturun ardından bu array'in shape'ini (15,2) şeklinde güncelleyip 2 boyutlu hale getirin.
2) 60 adet rastgele tam sayı verilerinden oluşan bir boyutlu bir array oluşturun. Devamında bu array'i istediğiniz shapelerde 3 boyutlu hale getirin ve son durumda oluşan array'in boyutunu ve shape'ini kontrol edin.
3) 20 elemanlı ve sadece rakamlardan oluşan iki boyutlu bir array oluşturun. Ardından bu array'i düzleştirin ve tek boyutlu hale getirin ve son durumda oluşan array'in boyutunu ve shape'ini kontrol edin.
4) İstediğiniz herhangi elemanlardan oluşan 2 Boyutlu bir array oluşturun. Oluşturduğunuz bu 2 boyutlu array'in içindeki bütün elemanları hem yavaş yol olan for döngüsüyle hem de daha hızlı yol olan uygun NumPy metoduyla tek tek dönerek ekrana yazdırın.
5) 5,10,15,20,25,30 değerlerinden oluşan bir boyutlu bir array ve
   1,2,3,4,5,6 değerlerinden oluşan başka bir boyutlu bir array oluşturun.
   Bu arraylerinin elemanlarına kendi aralarında 4 işlem uygulayın. İki arrayinde 1.indexindekiler toplansın/çıkartılsın/çarpılsın/bölünsün gibi.
6) 0-100 arası rastgele 10 tam sayıdan oluşan bir array oluşturun ve oluşturulan arrayin sum/mean/max/var/std değerlerini inceleyin.
7) 0-20 arası(20 dahil değil) tam sayılardan oluşan ve 500-530(530 dahil) arası tam sayılardan oluşan 2 array oluşturun. Ardından bu iki array'i concatenate ederek ekrana yazdırın.
8) 15-50(50 dahil) arası tam sayılardan oluşan bir array oluşturun. Daha sonra 10-100 arası(100 dahil) tam sayılardan oluşan 2.bir array oluşturun. Bu 2 arrayi concatanate ederek 3.bir array oluşturun ve bu array'in 25.index ile 50.index'i(50 dahil) arasındaki değerlerini 888 yapın.
9) 0-40(40 dahil değil) arası değerlerden oluşan (8,5) shape'inde 2 boyutlu bir array ve  320-360(360 dahil değil) değerlerinden oluşan (8,5) shape'inde 2 boyutlubaşka bir array oluşturun. Devamında bu iki array'i hem axis = 0'da hem de axis = 1'de concatenate ederek farkı karşılaştırın.
10) 9.Soruda oluşturduğunuz 2 array'i axis = 2'de concatenate etmeye çalışın. Ardından axis = 2'de stacklemeye(yığınlamaya) çalışın. İkisi arasındaki farkı karşılaştırın.
11) [1, 20, 25, 4, 4, 5, 4, 4, 1, 6, 9, 12, 1, 5] değerlerinden oluşan bir boyutlu bir array oluşturun. Devamında bu array'in içinde değeri 5'e eşit olan değerlerin indexleri bulun.
12) Yukarıda oluşturduğunuz array içinde değeri çift olan değerlerin indexlerini bulun.
13) Yukarıda oluşturduğunuz array içinde değeri 4'den büyük olan değerlerin indexlerini bulun.
14) Yukarıda oluşturduğunuz array içinde değeri 5'e tam bölünen değerlerin indexlerini bulun.
15) 85-100(100 dahil) arasından rastgele 1 tam sayı seçin
16) İki basamaklı tam sayılar arasından rastgele sayılar seçerek (3,3) shape'inde bir array oluşturun.
17) 35-60 arasındaki tam sayılardan bir array oluşturun, ardından bu array içinden rastgele 1 tam sayı seçin.
18) Sadece [3, 8, 10, 53] değerlerinden oluşan (2,5) shape'inde 2 boyutlu bir array oluşturun.
""")

print("***************************************************************************")

arr = np.arange(0, 30).reshape(15, 2)
print(arr)

print("***************************************************************************")

arr2 = np.random.randint(0, 100, 60).reshape(3, 5, 4)
print(arr2.shape)
print(arr2.ndim)

print("***************************************************************************")

arr3 = np.random.randint(0,10 , 20).reshape(5,4)
new_arr3 = arr3.reshape(-1)
print(new_arr3)
print(new_arr3.shape)
print(new_arr3.ndim)

print("***************************************************************************")

arr4 = np.random.randint(10, 100, 12).reshape(4, 3)
print("*****************************    EN YAVASI    **********************************************")
for x in arr4:
    for y in x:
        print(y)
print("*****************************    ORTA HIZLI   **********************************************")
new_arr4 = arr4.reshape(-1)
for x in new_arr4:
    print(x)
print("*****************************    EN HIZLI     ******************************************")
for x in np.nditer(arr4):
    print(x)

print("***************************************************************************")

arr5 = np.array([5, 10, 15, 20, 25, 30])
arr5_next = np.array([1, 2, 3, 4, 5, 6])
print(arr5 + arr5_next)
print(arr5 - arr5_next)
print(arr5 * arr5_next)
print(arr5 / arr5_next)

print("***************************************************************************")

arr6 = np.random.randint(0, 100, 10)
print(arr6)
print(arr6.sum())
print(arr6.mean())
print(arr6.max())
print(arr6.var())
print(arr6.std())

print("***************************************************************************")

arr7 = np.arange(20)
arr7_next = np.arange(500,531)

birlesme = np.concatenate([arr7,arr7_next],axis=0)
print(birlesme)

print("***************************************************************************")

arr8 = np.arange(15,51)
arr8_next = np.arange(10,101)
birlesik = np.concatenate([arr8,arr8_next],axis=0)
birlesik[25:51] = 888
print(birlesik)

print("***************************************************************************")

arr9 =np.arange(0,40).reshape(8,5)
arr9_next = np.arange(320,360).reshape(8,5)
xe_gore = np.concatenate([arr9,arr9_next],axis=0)
ye_gore = np.concatenate([arr9,arr9_next],axis=1)
print(xe_gore)
print(ye_gore)

print("***************************************************************************")

arr9_update = arr9.reshape(2,5,4)
arr9_next_update = arr9_next.reshape(2,5,4)
arr10 = np.concatenate([arr9_update,arr9_next_update],axis=2)
yigin = np.stack([arr9_update,arr9_next_update],axis=2)
print(arr10)
print("*************************")
print(yigin)

print("***************************************************************************")

arr11 = np.array([1, 20, 25, 4, 4, 5, 4, 4, 1, 6, 9, 12, 1, 5])
xx = np.where(arr11 == 5)
print(xx)

print("***************************************************************************")

cift_mi = np.where(arr11 % 2 == 0)
print(cift_mi)

print("***************************************************************************")

arr13 = np.where(arr11 > 4)
print(arr13)

print("***************************************************************************")

arr14 = np.where(arr11 % 5 == 0 )
print(arr14)

print("***************************************************************************")

arr15 = np.random.randint(85,101,1)
print(arr15)

print("***************************************************************************")

arr16 = np.random.randint(10,100,9).reshape(3,3)
print(arr16)

print("***************************************************************************")

arr17 = np.arange(35,60)
rast = np.random.choice(arr17)
print(rast)

print("***************************************************************************")

arr18 = np.random.choice([3,8,10,53],size=(2,5))
print(arr18)

print("***************************************************************************")

