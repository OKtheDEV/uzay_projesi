import time
from collections.abc import Callable
from functools import wraps
from typing import Any

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

    return sorted(
        gezegenler, key=lambda g: (-len(baglantilar.get(g, [])), g)
    )

def sure_olc(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """Bir fonksiyonun calisma suresini olcen ve ekrana yazdiran sarmalayici dekorator."""

    @wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"{fonksiyon.__name__} calisma suresi: {gecen_sure:.6f} saniye")
        return sonuc

    return sarmalayici

if __name__ == "__main__":
    # Bonus yonergesindeki deneme cagrisi:
    ornek_galaksi = {
        "gezegenler": ["dünya", "mars", "centauri", "sirius"],
        "baglantilar": {
            "dünya": ["mars", "centauri"],
            "mars": ["dünya"],
            "centauri": ["dünya", "sirius"],
            "sirius": ["centauri"],
        },
    }

    olculen_en_bagli = sure_olc(en_bagli_gezegenler)
    sirali = olculen_en_bagli(ornek_galaksi)
    print("Sonuc:", sirali)