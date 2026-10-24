from uzay_oyunu.dekoratorler import sure_olc

# 1. Test: Sonuç değişmeden dönüyor mu?
def test_sure_olc_sonuc_degismeden_donuyor():
    @sure_olc
    def topla(a, b):
        return a + b

    assert topla(3, 5) == 8

# 2. Test: Adlı (keyword) argümanlarla çağrı çalışıyor mu?
def test_sure_olc_adli_argumanlar():
    @sure_olc
    def selamla(isim, unvan="Kaptan"):
        return f"Merhaba {unvan} {isim}"

    sonuc = selamla(isim="Ali", unvan="Mühendis")
    assert sonuc == "Merhaba Mühendis Ali"

# 3. Test: __name__ ve __doc__ korunuyor mu?
def test_sure_olc_meta_veri_korunuyor():
    @sure_olc
    def ornek_fonksiyon():
        """Bu bir örnek dokümantasyon metnidir."""
        return True

    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Bu bir örnek dokümantasyon metnidir."