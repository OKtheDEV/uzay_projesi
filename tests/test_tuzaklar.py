# Hatalı hal: Varsayılan liste [] hafızada tek bir nesne olarak kalır
# def yakit_ekle(miktar, depo=[]):
#     depo.append(miktar)
#     return depo

# Düzeltilmiş hal (None kalıbı):
def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Depoya yakit ekler; depo belirtilmezse her cagrida yeni liste olusturur."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def test_yakit_ekle_bagimsiz_listeler():
    # İlk çağrı: sadece [10] dönmeli
    sonuc1 = yakit_ekle(10)
    assert sonuc1 == [10]

    # İkinci çağrı: depo verilmediğinde önceki 10 kalmamalı, sadece [20] dönmeli
    sonuc2 = yakit_ekle(20)
    assert sonuc2 == [20]

def test_yakit_ekle_var_olan_depo():
    mevcut_depo = [5, 15]
    sonuc = yakit_ekle(25, mevcut_depo)
    assert sonuc == [5, 15, 25]