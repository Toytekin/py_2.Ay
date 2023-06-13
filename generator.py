



def kareleriAl():
        for i in range(1,6):
                yield i**2
                
  
  
generator=kareleriAl()
iterator=iter(generator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)


print('**********************')
print(next(iterator))  
  
                
                