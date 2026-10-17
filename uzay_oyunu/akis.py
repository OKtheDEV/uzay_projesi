from collections.abc import Iterator
from collections.abc import Iterable, Iterator
from collections.abc import Callable, Iterable, Iterator
from functools import lru_cache
import time

def fibonacci() -> Iterator[int]:
    """Sonsuz Fibonacci dizisi elemanlarını sırasıyla üreten bir üreteç (generator).
    0, 1, 1, 2, 3, 5, 8, ... şeklinde değerleri 'yield' eder.
    Yields:
        int: Fibonacci dizisinin sıradaki sayısı.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """Her adımda yakıtı tüketim kadar azaltıp kalan yakıtı üreten üreteç.
    Yakıt sıfıra indiğinde 0 değerini üretip sonlanır.

    Args:
        yakit (int): Başlangıçtaki toplam yakıt miktarı.
        tuketim (int): Her bir adım/yolculuk başına tüketilen yakıt miktarı.

    Yields:
        int: Kalan yakıt miktarı (en az 0).
    """
    kalan = yakit
    while kalan > 0:
        kalan = max(0, kalan - tuketim)
        yield kalan

def satirlari_oku(yol: str) -> Iterator[str]:
    """Belirtilen dosyadaki boş ve '#' ile başlayan yorum satırlarını atlayarak satırları üretir.

    Args:
        yol (str): Okunacak dosyanın dosya yolu.

    Yields:
        str: Temizlenmiş ve filtrelenmiş satır metni.
    """
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz = satir.strip()
            if not temiz or temiz.startswith("#"):
                continue
            yield temiz

def ayristir(satirlar: Iterable[str]) -> Iterator[tuple[str, str, int]]:
    """'kaynak -> hedef yakit' formatındaki satırları (kaynak, hedef, yakit) demetine ayrıştırır.

    Args:
        satirlar (Iterable[str]): Ayrıştırılacak satır akışı.

    Yields:
        tuple[str, str, int]: (kaynak, hedef, yakıt) demeti.
    """
    for satir in satirlar:
        # Örnek: 'dünya -> sirius 12'
        kaynak, kalan = satir.split("->")
        kaynak = kaynak.strip()
        hedef, yakit_str = kalan.strip().rsplit(maxsplit=1)
        yield (kaynak, hedef, int(yakit_str))

def uzun_yolculuklar(
    kayitlar: Iterable[tuple[str, str, int]], esik: int
) -> Iterator[tuple[str, str, int]]:
    """Yakıtı verilen eşik değerinden kesinlikle büyük olan yolculukları süzen üreteç.

    Args:
        kayitlar (Iterable[tuple[str, str, int]]): Yolculuk kayıtları akışı.
        esik (int): Yakıt eşik sınırı.

    Yields:
        tuple[str, str, int]: Eşik değerinden büyük yakıta sahip kayıt.
    """
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit

def rota_sayaci(baglantilar: dict[str, list[str]]) -> Callable[[str, int], int]:
    """Verilen gezegen bağlantı haritasına göre önbellekli bir rota sayacı döndürür.

    Args:
        baglantilar (dict[str, list[str]]): Gezegenlerin komşuluk listesini içeren sözlük.

    Returns:
        Callable[[str, int], int]: (gezegen, adim) alıp toplam rota sayısını döndüren fonksiyon.
    """

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Verilen gezegenden başlayıp tam adim kadar süren farklı rotaların sayısını hesaplar."""
        if adim == 0:
            return 1

        komsular = baglantilar.get(gezegen, [])
        return sum(rota_sayisi(komsu, adim - 1) for komsu in komsular)

    return rota_sayisi

def zamanlayici(aralik: float) -> Iterator[float]:
    """Belirli periyotlarla tetiklenen zamanlayıcı üreteci.

    Args:
        aralik (float): Tetiklenme aralığı (saniye).

    Yields:
        float: Tetiklenme anındaki zaman damgası.
    """
    hedef = time.perf_counter() + aralik
    while True:
        if time.perf_counter() >= hedef:
            yield hedef
            hedef += aralik

def tik_tak_calistir(toplam_sure: float = 10.0) -> list[str]:
    """10 saniye boyunca 2 saniyede bir 'tik', 5 saniyede bir 'tak' üretir.

    AÇIKLAMA (Meşgul Bekleme vs time.sleep):
    - Meşgul Bekleme (Busy Waiting): Döngü sürekli CPU'yu meşgul ederek
      koşulun sağlanıp sağlanmadığını aralıksız sorgular. CPU kullanımı %100'e fırlar
      ve enerji/kaynak israfına yol açar.
    - time.sleep(): İş parçacığını uyku durumuna alarak CPU kullanımını askıya alır;
      işletim sistemi diğer süreçleri çalıştırabilir, kaynak tasarrufu sağlar.
    """
    t_tik = zamanlayici(2.0)
    t_tak = zamanlayici(5.0)

    baslangic = time.perf_counter()
    olaylar: list[str] = []

    sonraki_tik = time.perf_counter() + 2.0
    sonraki_tak = time.perf_counter() + 5.0

    while time.perf_counter() - baslangic < toplam_sure:
        su_an = time.perf_counter()
        if su_an >= sonraki_tik:
            print("tik")
            olaylar.append("tik")
            sonraki_tik += 2.0
        if su_an >= sonraki_tak:
            print("tak")
            olaylar.append("tak")
            sonraki_tak += 5.0

    return olaylar