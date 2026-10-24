import json
from uzay_oyunu.akis import yakit_gostergesi
from uzay_oyunu.dekoratorler import log_cagri
from uzay_oyunu.komutlar import KOMUTLAR

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Envanter durumuna gore uygun aciklama metnini dondurur."""
    ogeler = []
    if credits:
        ogeler.append("bol kredi")
    if engines:
        ogeler.append("guclu motorlar")
    if copilot:
        ogeler.append("yetenekli bir pilot")

    if not ogeler:
        return ""
    return f"Sende: {', '.join(ogeler)}"

@log_cagri
def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandirilmis liste metni olarak dondurur."""
    satirlar = ["Nereye gitmek istersin?"]
    for sira, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{sira}] {hedef}")
    return "\n".join(satirlar)

@log_cagri
def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs: int,
) -> dict:
    """Oyun galaksisini kurar; baslangic konumunu ve yakiti ayarlar."""
    if baslangic not in gezegenler:
        raise ValueError(f"Baslangic gezegeni '{baslangic}' gezegenler listesinde yok.")

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }

def travel(
    galaksi: dict | None = None, tuketim: int = 5, durum: dict | None = None
) -> str:
    """Galakside seyahat eder; komut girdilerini çalıştırır ve yakıt tüketimini yönetir."""
    if galaksi is None:
        return ""

    # Eğer durum sözlüğü harici verilmediyse galaksi sözlüğünden oluşturulur
    if durum is None:
        durum = galaksi

    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {})
    hedefler = baglantilar.get(konum, [])

    # İnteraktif girdi kontrolü:
    # Oyuncu konsoldan komut girdiğinde menüyü tekrar gösterir
    while True:
        try:
            print(hedef_menusu(hedefler))
            girdi = input("> ").strip().lower()
        except (EOFError, OSError):
            # Test ortamında input mocklanmamışsa veya dosya sonuysa döngüden çık
            break

        if not girdi:
            break

        if girdi in KOMUTLAR:
            komut_fonk, _ = KOMUTLAR[girdi]
            sonuc = komut_fonk(durum)
            if sonuc:
                print(sonuc)
            continue  # Komut çalıştıktan sonra aynı menüyü tekrar gösterir

        # Komut değilse, gezegen seçimi olarak kabul edilir ve döngü biter
        break

    # Standart yakıt tüketim adımı
    baslangic_yakit = galaksi.get("yakit", 100)
    gosterge = yakit_gostergesi(baslangic_yakit, tuketim)

    try:
        kalan_yakit = next(gosterge)
        galaksi["yakit"] = kalan_yakit
        return f"Yolculuk yapıldı. Kalan yakıt: {kalan_yakit}"
    except StopIteration:
        return "Yakıtın bitti, uzayda sürükleniyorsun…"