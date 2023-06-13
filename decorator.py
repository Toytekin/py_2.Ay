

# https://github.com/Toytekin/py_2.Ay.git


def ekstraDekoratore(fonk):
        def wrapper(sayilar):
                cift_Syilar=0
                cifler_Toplami=0
                tek_Sayilar=0 
                tekler_Toplami=0 
           
                for sayi in sayilar:
                        if sayi%2==0:
                                cift_Syilar+=1
                                cifler_Toplami+=sayi
                        else:
                                tek_Sayilar+=1
                                tekler_Toplami+=sayi 
                                
                cift_Ortalam=cifler_Toplami/cift_Syilar
                tek_Ortalama=tekler_Toplami/tek_Sayilar
                
                print(f'Tek Sayiların ortalamasi {tek_Ortalama}')
                print(f'Çiift Sayiların ortalaması {cift_Ortalam}')                
                fonk(sayilar)         
        return wrapper

@ekstraDekoratore
def ortalamaBul(sayilar):
        toplam=0
        for i in sayilar:
                toplam+=i
        ortalama=toplam/len(sayilar)
        print(f'Genel Ortalama {ortalama}')
        

     
ortalamaBul([12,235,354,2,4,8,6,1,77,88,99,22])                
        
        
        
#                       NOTLAR        



# 1. En üste ekstra özellikler diye bir fonksiyon yazdım.

# 2. Bu fonksiyon içinde << def wrapper(sayilar) >> özel fonksiyonu çağırdım

# 3. Daha sonro bu fonksiyoınun işlemlerinden sonra fonksiyonumu return ettim. <<  return wrapper >>

# 4. Özelliği eklemek istediğim fonksiyoınun üzerinde @ işaretiyle tanımlama yaptım
        