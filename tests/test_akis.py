import itertools
from uzay_oyunu.akis import fibonacci

def test_fibonacci_gorev_1():
    # 1. next() ile ilk 3 elemanı alma kontrolü
    g1 = fibonacci()
    assert (next(g1), next(g1), next(g1)) == (0, 1, 1)

    # 2. itertools.islice ile ilk 12 elemanı alma kontrolü
    g2 = fibonacci()
    ilk_12 = list(itertools.islice(g2, 12))
    assert ilk_12 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # 3. itertools.takewhile ile 100'den küçük elemanları alma kontrolü
    g3 = fibonacci()
    yuzden_kucukler = list(itertools.takewhile(lambda x: x < 100, g3))
    assert yuzden_kucukler == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # 4. Üretecin tek kullanımlık (exhaustible) olduğunun kanıtı:
    # Aynı üreteçten (g4) arka arkaya islice yapıldığında ikinci çağrı farklı/devam eden sonuç üretmeli
    g4 = fibonacci()
    parca_1 = list(itertools.islice(g4, 4))  # [0, 1, 1, 2]
    parca_2 = list(itertools.islice(g4, 4))  # [3, 5, 8, 13]
    assert parca_1 != parca_2
    assert parca_1 == [0, 1, 1, 2]
    assert parca_2 == [3, 5, 8, 13]

import pytest
from uzay_oyunu.akis import yakit_gostergesi

def test_yakit_gostergesi():
    # Dokümandaki örnek: 100 yakıt, 30 tüketim -> [70, 40, 10, 0]
    gosterge = yakit_gostergesi(100, 30)
    assert list(gosterge) == [70, 40, 10, 0]

    # StopIteration davranışı testi
    g = yakit_gostergesi(20, 10)
    assert next(g) == 10
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)

from uzay_oyunu.oyun import galaksi_kur, travel

def test_travel_yakit_bitisi():
    galaksi = galaksi_kur(["Dunya", "Mars"], {"Dunya": ["Mars"]}, "Dunya", yakit=10)
    # Tüketim 10 olduğunda ilk adımda yakıt 0'a iner, sonrakinde biter
    travel(galaksi, tuketim=10)
    sonuc = travel(galaksi, tuketim=10)
    assert "Yakıtın bitti, uzayda sürükleniyorsun…" in sonuc