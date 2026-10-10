# Python Kapsam (Scope) ve Değişken Davranışları

## 1. Örnek: Yerel ve Global Kapsam Ayrımı
```python
x = 10
def goster():
    print(x)
goster()

Tahmin: 10 yazdırır.
Gerçek Sonuç: 10
Nedeni: Fonksiyon kendi yerel (local) kapsamında x bulamazsa, LEGB (Local -> Enclosing -> Global -> Built-in) arama kuralı gereği bir üst kapsama (global) bakar ve 10 değerini okur.


x = 10
def degistir():
    x = 20
degistir()
print(x)

Tahmin: 10 yazdırır.
Gerçek Sonuç: 10
Nedeni: Fonksiyon içindeki x = 20 ataması sadece o fonksiyona ait yerel (local) yeni bir değişken oluşturur. Dışarıdaki global x değişkeninin değeri bundan etkilenmez ve 10 kalır.


x = 10

def arttir():
    x += 1

arttir()

Tahmin: Hata verir (UnboundLocalError).
Gerçek Sonuç: UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
Nedeni ve Açıklaması:
Python bir fonksiyonu çalıştırırken gövdede x = ... veya x += ... gibi bir atama işlemi gördüğü anda o değişkeni doğrudan yerel (local) değişken olarak kabul eder.
x += 1 ifadesi aslında x = x + 1 demektir. Python sağdaki x değerini okumak ister; fakat x artık yerel kabul edildiği ve henüz yerel bir başlangıç değeri atanmadığı için dışarıdaki global 10'a bakmaz. Tanımsız bir yerel değişkene erişilmeye çalışıldığı için Python UnboundLocalError fırlatır.