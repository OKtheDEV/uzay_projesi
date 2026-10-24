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

from uzay_oyunu.dekoratorler import say

def test_say_cagri_sayisi_artiyor():
    @say
    def selam(isim):
        return f"Selam {isim}"

    assert selam.cagri == 0
    selam("Ali")
    assert selam.cagri == 1
    selam("Ayşe")
    assert selam.cagri == 2


def test_say_meta_veri_korunuyor():
    @say
    def ornek():
        """Doküman metni."""
        pass

    assert ornek.__name__ == "ornek"
    assert ornek.__doc__ == "Doküman metni."

from uzay_oyunu.dekoratorler import log_cagri

def test_log_cagri_calisiyor_ve_yazdiriyor(capsys):
    @log_cagri
    def yolculuk(hedef, hiz=1):
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)
    assert sonuc == "orion hiz=3"

    yakalanan = capsys.readouterr().out
    assert "-> yolculuk('orion', hiz=3)" in yakalanan
    assert "<- yolculuk = 'orion hiz=3'" in yakalanan


def test_log_cagri_meta_veri_korunuyor():
    @log_cagri
    def ornek():
        """Log test dokümantasyonu."""
        pass

    assert ornek.__name__ == "ornek"
    assert ornek.__doc__ == "Log test dokümantasyonu."

from unittest.mock import patch
import pytest
from uzay_oyunu.komutlar import KOMUTLAR, envanter, harita, komut, yardim
from uzay_oyunu.oyun import travel

def test_komut_kayit_deseni_ve_value_error():
    @komut("ozel_komut", "Özel bir açıklama")
    def ornek(durum):
        return "çalıştı"

    assert "ozel_komut" in KOMUTLAR
    assert KOMUTLAR["ozel_komut"][1] == "Özel bir açıklama"

    # Aynı adla tekrar kaydedilmek istenirse ValueError fırlatmalı
    with pytest.raises(ValueError):

        @komut("ozel_komut", "Yinelenen komut")
        def ayni_ad(durum):
            pass

def test_komut_yardim():
    durum = {}
    cikti = yardim(durum)
    assert "yardim" in cikti
    assert "envanter" in cikti
    assert "harita" in cikti


def test_komut_envanter():
    durum = {"credits": True, "engines": True, "copilot": False}
    cikti = envanter(durum)
    assert "bol kredi" in cikti
    assert "guclu motorlar" in cikti
    assert "yetenekli bir pilot" not in cikti


def test_komut_harita():
    durum = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["mars", "kara_delik"]},
    }
    cikti = harita(durum)
    assert "mars, kara_delik" in cikti


def test_travel_komut_calistirip_menuyu_tekrar_gosterir(capsys):
    galaksi = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["mars"]},
        "yakit": 50,
        "credits": True,
        "engines": False,
        "copilot": False,
    }

    # Kullanıcı önce 'harita' komutunu girsin, ardından '1' seçeneğiyle çıksın
    girdiler = iter(["harita", "1"])
    with patch("builtins.input", lambda _: next(girdiler)):
        travel(galaksi)

    yakalanan = capsys.readouterr().out
    # 'harita' komutunun sonucunu ekrana basmış olmalı
    assert "mars" in yakalanan
    # Menüyü tekrar gösterdiği için 'Nereye gitmek istersin?' birden fazla kez basılmış olmalı
    assert yakalanan.count("Nereye gitmek istersin?") >= 2

import pytest
from uzay_oyunu.dekoratorler import sinirla

def test_sinirla_sinir_degerleri_0_ve_100():
    @sinirla(0, 100)
    def harca(miktar):
        return 100 - miktar

    # Alt sınır: 0
    assert harca(0) == 100
    # Üst sınır: 100
    assert harca(100) == 0
    # Aralık içi değer: 30
    assert harca(30) == 70

def test_sinirla_aralik_disi_alt_deger_hata():
    @sinirla(0, 100)
    def harca(miktar):
        return 100 - miktar

    # Alt sınırın altı: -1
    with pytest.raises(
        ValueError, match="harca: -1 değeri 0-100 aralığında değil"
    ):
        harca(-1)

def test_sinirla_aralik_disi_ust_deger_hata():
    @sinirla(0, 100)
    def harca(miktar):
        return 100 - miktar

    # Üst sınırın üstü: 150
    with pytest.raises(
        ValueError, match="harca: 150 değeri 0-100 aralığında değil"
    ):
        harca(150)

def test_sinirla_meta_veri_korunuyor():
    @sinirla(0, 50)
    def ornek_fonk(x):
        """Docstring metni."""
        return x

    assert ornek_fonk.__name__ == "ornek_fonk"
    assert ornek_fonk.__doc__ == "Docstring metni."

from functools import lru_cache
from uzay_oyunu.dekoratorler import hafiza

def test_hafiza_lru_cache_ile_karsilastirma():
    # 1. Kendi hafiza dekoratörümüzle Fibonacci
    cagri_hafiza = 0

    @hafiza(maxsize=None)
    def fib_hafiza(n):
        nonlocal cagri_hafiza
        cagri_hafiza += 1
        if n <= 1:
            return n
        return fib_hafiza(n - 1) + fib_hafiza(n - 2)

    # 2. Standart functools.lru_cache ile Fibonacci
    cagri_lru = 0

    @lru_cache(maxsize=None)
    def fib_lru(n):
        nonlocal cagri_lru
        cagri_lru += 1
        if n <= 1:
            return n
        return fib_lru(n - 1) + fib_lru(n - 2)

    # Sonuçlar ve çağrı sayıları birebir aynı olmalı
    sonuc_hafiza = [fib_hafiza(i) for i in range(15)]
    sonuc_lru = [fib_lru(i) for i in range(15)]

    assert sonuc_hafiza == sonuc_lru
    assert cagri_hafiza == cagri_lru

def test_hafiza_maxsize_en_eskiyi_siler():
    hesaplananlar = []

    @hafiza(maxsize=2)
    def carp_iki(x):
        hesaplananlar.append(x)
        return x * 2

    # 1 ve 2 eklenir (kapasite doldu)
    assert carp_iki(1) == 2
    assert carp_iki(2) == 4
    assert len(carp_iki.cache) == 2

    # 3 eklenince en eski girdi olan 1 silinmeli
    assert carp_iki(3) == 6
    assert len(carp_iki.cache) == 2
    assert ( (1,), () ) not in carp_iki.cache

    # 2 hala önbellekte olduğu için tekrar hesaplanmamalı
    carp_iki(2)
    assert hesaplananlar == [1, 2, 3]

    # 1 tekrar çağrılırsa önbellekten silindiği için baştan hesaplanmalı
    carp_iki(1)
    assert hesaplananlar == [1, 2, 3, 1]