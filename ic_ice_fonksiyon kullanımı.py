

# https://github.com/Toytekin/py_2.Ay.git
def ana_fonksiyon(fonksiyon_adi):
        
        def toplama(*args):
                toplam=0
                for i in args:
                        toplam+=i
                print(toplam)
        
        def carpma(*args):
                carpim=1
                for i in args:
                        carpim*=i
                print(carpim)
        
        
        if fonksiyon_adi=='toplama':
                return toplama       
        else:
                return carpma
        
        
toplama=ana_fonksiyon('toplama')
carpma=ana_fonksiyon('carpma')

toplama(1,2,3,4,5,6,7,8,9)
carpma(1,2,3,4,5,6,7,8,9)


            