from collections.abc import Iterator

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