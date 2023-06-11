## Python'da decoratorların nerelerde ve nasıl kullanılır

1. Python'da decoratorlar, fonksiyonları veya sınıfları değiştirmek, genişletmek veya başka bir işlevi eklemek için kullanılan işlevlerdir. Decoratorlar, fonksiyon veya sınıf tanımlamalarının hemen üzerine "@" sembolüyle birlikte kullanılırlar.

## Fonksiyon Decoratorları:
 İşlev çağrısından önce veya sonra ekstra bir işlem yapmak için kullanılabilir.

 Fonksiyonu önbelleğe almak, hata denetimi yapmak veya performans ölçümü yapmak gibi ekstra özellikler eklemek için kullanılabilir.

 Aşağıdaki örnek, bir fonksiyonun ne kadar süreyle çalıştığını ölçmek için bir decorator kullanır: 

##
import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time} seconds.")
        return result
    return wrapper

@calculate_time
def calculate_sum(a, b):
    time.sleep(2)
    return a + b

print(calculate_sum(3, 5))
##

## Sınıf Decoratorları:
Sınıfları genişletmek veya sınıf seviyesindeki işlemleri yapmak için kullanılabilir.
Sınıfın tüm örneklerini izlemek veya bir sınıfa özel metotları otomatik olarak eklemek gibi ekstra işlevler sağlamak için kullanılabilir.
Aşağıdaki örnek, bir sınıfın tüm metodlarının çağrıldığında loglama yapmasını sağlayan bir decorator kullanır:



##
def log_calls(cls):
    for name, method in cls.__dict__.items():
        if callable(method):
            setattr(cls, name, log_method_calls(method))
    return cls

def log_method_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
class MyClass:
    def method1(self):
        print("Executing method1")
    
    def method2(self):
        print("Executing method2")

obj = MyClass()
obj.method1()
obj.method2()

##