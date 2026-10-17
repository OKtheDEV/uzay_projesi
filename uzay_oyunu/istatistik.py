"""Galaksi verisi üzerinde istatistiksel işlemler ve fonksiyonel araçlar modülü."""

from functools import partial, reduce

# Soru 1: Gezegen adlarının büyük harfli listesi
def buyuk_harfli_gezegenler_map(gezegenler: list[str]) -> list[str]:
    """map kullanarak gezegen adlarını büyük harfe çevirir."""
    return list(map(str.upper, gezegenler))

def buyuk_harfli_gezegenler_comp(gezegenler: list[str]) -> list[str]:
    """Liste üreteci (list comprehension) kullanarak gezegen adlarını büyük harfe çevirir."""
    return [g.upper() for g in gezegenler]

# Soru 2: En az iki bağlantısı olan gezegenler
def cok_baglantili_gezegenler_filter(
    gezegenler: list[str], baglantilar: dict[str, list[str]]
) -> list[str]:
    """filter kullanarak en az 2 bağlantısı olan gezegenleri süzer."""
    return list(filter(lambda g: len(baglantilar.get(g, [])) >= 2, gezegenler))

def cok_baglantili_gezegenler_comp(
    gezegenler: list[str], baglantilar: dict[str, list[str]]
) -> list[str]:
    """Liste üreteci kullanarak en az 2 bağlantısı olan gezegenleri süzer."""
    return [g for g in gezegenler if len(baglantilar.get(g, [])) >= 2]

# Soru 3: Toplam bağlantı sayısı
def toplam_baglanti_reduce(baglantilar: dict[str, list[str]]) -> int:
    """functools.reduce kullanarak toplam bağlantı sayısını hesaplar."""
    uzunluklar = [len(komsular) for komsular in baglantilar.values()]
    if not uzunluklar:
        return 0
    return reduce(lambda acc, x: acc + x, uzunluklar)

def toplam_baglanti_sum(baglantilar: dict[str, list[str]]) -> int:
    """sum ve üreteç ifadesi kullanarak toplam bağlantı sayısını hesaplar."""
    return sum(len(komsular) for komsular in baglantilar.values())

# functools.partial ile hızlı yolculuk fonksiyonu
def yolculuk(mesafe: int, hiz: int = 1) -> float:
    """Verilen mesafe ve hıza göre yolculuk süresini hesaplar."""
    return mesafe / hiz

hizli_yolculuk = partial(yolculuk, hiz=3)

# YORUM VE KARŞILAŞTIRMA:
# Python'da liste üreteçleri (list comprehensions) ve doğrudan 'sum()' fonksiyonu,
# 'map', 'filter' ve 'reduce' kullanımına göre çok daha okunabilir ve Pythonik kabul edilir.
# lambda ifadelerinin yarattığı sözdizimi kalabalığını ortadan kaldırır ve kodu daha sade kılar.