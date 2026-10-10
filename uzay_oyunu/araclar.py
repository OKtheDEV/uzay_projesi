from collections.abc import Callable

def hamle_sayaci() -> Callable[[], int]:
    """Her cagrildiginda hamle sayisini 1 artiran bir sayac fonksiyonu dondurur (closure)."""
    sayac = 0

    def say() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return say

def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri baglanti sayisina gore azalan, esitlik durumunda alfabetik sirada dondurur."""
    baglantilar = galaksi.get("baglantilar", {})
    gezegenler = galaksi.get("gezegenler", list(baglantilar.keys()))

    # Siralama kurali:
    # 1. Baglanti sayisi azalan (eksi isaretiyle ters cevirilir: -len(...))
    # 2. Alfabetik artan sira (gezegen adi)
    return sorted(
        gezegenler, key=lambda g: (-len(baglantilar.get(g, [])), g)
    )