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