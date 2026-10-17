from uzay_oyunu.istatistik import (
    buyuk_harfli_gezegenler_comp,
    buyuk_harfli_gezegenler_map,
    cok_baglantili_gezegenler_comp,
    cok_baglantili_gezegenler_filter,
    hizli_yolculuk,
    toplam_baglanti_reduce,
    toplam_baglanti_sum,
    yolculuk,
)

def test_istatistik_gorev_5():
    gezegenler = ["dünya", "centauri", "sirius", "orion", "kara_delik"]
    baglantilar = {
        "dünya": ["sirius", "orion"],
        "centauri": ["orion", "sirius"],
        "sirius": ["dünya", "orion", "kara_delik"],
        "orion": ["dünya", "sirius", "centauri"],
        "kara_delik": ["sirius"],
    }

    # 1. Büyük harfli liste testleri
    beklenen_buyuk = ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]
    assert buyuk_harfli_gezegenler_map(gezegenler) == beklenen_buyuk
    assert buyuk_harfli_gezegenler_comp(gezegenler) == beklenen_buyuk

    # 2. En az 2 bağlantılı gezegenler testleri (kara_delik hariç hepsi en az 2)
    beklenen_baglantililar = ["dünya", "centauri", "sirius", "orion"]
    assert cok_baglantili_gezegenler_filter(gezegenler, baglantilar) == beklenen_baglantililar
    assert cok_baglantili_gezegenler_comp(gezegenler, baglantilar) == beklenen_baglantililar

    # 3. Toplam bağlantı sayısı testleri (2 + 2 + 3 + 3 + 1 = 11 veya örnekteki gibi)
    assert toplam_baglanti_reduce(baglantilar) == 11
    assert toplam_baglanti_sum(baglantilar) == 11

    # 4. partial (hizli_yolculuk) testi
    # Mesafe 30 iken hız=3 ile 10.0 çıkmalı
    assert hizli_yolculuk(30) == 10.0
    assert yolculuk(30, hiz=1) == 30.0