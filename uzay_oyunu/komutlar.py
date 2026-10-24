import functools
from typing import Any, Callable

# Komutları saklayan sözlük: {komut_adi: (fonksiyon, aciklama)}
KOMUTLAR: dict[str, tuple[Callable, str]] = {}

def komut(ad: str, aciklama: str = ""):
    """Fonksiyonu KOMUTLAR sözlüğüne kaydeden parametreli dekoratör."""
    if ad in KOMUTLAR:
        raise ValueError(f"'{ad}' adlı komut zaten kayıtlı!")

    def dekorator(fonk: Callable):
        KOMUTLAR[ad] = (fonk, aciklama)

        @functools.wraps(fonk)
        def sarmalayici(*args, **kwargs):
            return fonk(*args, **kwargs)

        return sarmalayici

    return dekorator

@komut("yardim", "komutları listeler")
def yardim(durum: dict[str, Any]) -> str:
    """Kayıtlı komutları ve açıklamalarını listeler."""
    satirlar = []
    for ad in sorted(KOMUTLAR.keys()):
        _, aciklama = KOMUTLAR[ad]
        satirlar.append(f"{ad:<8} {aciklama}")
    return "\n".join(satirlar)

@komut("envanter", "eşyalarını gösterir")
def envanter(durum: dict[str, Any]) -> str:
    """Oyuncunun envanterindeki eşyaları gösterir."""
    credits_ = durum.get("credits", False)
    engines = durum.get("engines", False)
    copilot = durum.get("copilot", False)

    ogeler = []
    if credits_:
        ogeler.append("bol kredi")
    if engines:
        ogeler.append("guclu motorlar")
    if copilot:
        ogeler.append("yetenekli bir pilot")

    if not ogeler:
        return "Envanterin boş."
    return f"Sende: {', '.join(ogeler)}"

@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum: dict[str, Any]) -> str:
    """Mevcut konumdan gidilebilecek gezegenleri virgülle ayrılmış döndürür."""
    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {})
    komsular = baglantilar.get(konum, [])
    return ", ".join(komsular)