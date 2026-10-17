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

from uzay_oyunu.akis import ayristir, satirlari_oku, uzun_yolculuklar

def test_seyir_defteri_boru_hatti(tmp_path):
    # Geçici bir seyir dosyası oluşturarak izole test yapalım
    test_veri = (
        "dünya -> sirius 12\n"
        "sirius -> orion 8\n"
        "orion -> centauri 15\n"
        "# bakım molası\n"
        "centauri -> orion 15\n"
        "orion -> sirius 8\n"
        "sirius -> kara_delik 30\n"
    )
    dosya = tmp_path / "seyir.txt"
    dosya.write_text(test_veri, encoding="utf-8")

    # 1. Toplam yakıt kontrolü (Görselde: sum(...) == 88)
    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(str(dosya))))
    assert toplam_yakit == 88

    # 2. uzun_yolculuklar filtresi (esik=10) kontrolü
    # Beklenen hedefler: ['sirius', 'centauri', 'orion', 'kara_delik']
    kayitlar = ayristir(satirlari_oku(str(dosya)))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]

    # 3. Yorum ve boş satır atlama kontrolü
    satirlar = list(satirlari_oku(str(dosya)))
    assert len(satirlar) == 6
    assert not any(s.startswith("#") for s in satirlar)

from uzay_oyunu.akis import rota_sayaci

def test_rota_sayaci():
    # Basit bir galaksi grafı kuralım:
    # A <-> B (birbirine bağlı iki gezegen)
    baglantilar = {
        "A": ["B"],
        "B": ["A"],
    }
    say = rota_sayaci(baglantilar)

    # 0 adımda sadece olduğu yerde durur: 1
    assert say("A", 0) == 1
    # 1 adımda A -> B: 1
    assert say("A", 1) == 1
    # 2 adımda A -> B -> A: 1
    assert say("A", 2) == 1

    # Üçgen bağlantı:
    # Dunya -> [Mars, Venus], Mars -> [Dunya], Venus -> [Dunya]
    ucgen_baglanti = {
        "Dunya": ["Mars", "Venus"],
        "Mars": ["Dunya"],
        "Venus": ["Dunya"],
    }
    say_ucgen = rota_sayaci(ucgen_baglanti)
    # 1 adım: Dunya -> Mars, Dunya -> Venus (2)
    assert say_ucgen("Dunya", 1) == 2
    # 2 adım: Dunya -> Mars -> Dunya, Dunya -> Venus -> Dunya (2)
    assert say_ucgen("Dunya", 2) == 2
    # 3 adım: 4 rota
    assert say_ucgen("Dunya", 3) == 4

    # lru_cache devrede mi kontrolü
    info = say_ucgen.cache_info()
    assert info.hits > 0

from uzay_oyunu.akis import tik_tak_calistir, zamanlayici

def test_zamanlayici_ve_tik_tak():
    # 0.1 saniyelik zamanlayıcı testi
    z = zamanlayici(0.05)
    t1 = next(z)
    t2 = next(z)
    assert t2 > t1

    # Kısa bir simülasyon (örneğin 0.01 saniye) ile fonksiyonun çalıştığını doğrulama
    sonuc = tik_tak_calistir(toplam_sure=0.01)
    assert isinstance(sonuc, list)