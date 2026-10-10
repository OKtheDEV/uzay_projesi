import json

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

def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandirilmis liste metni olarak dondurur."""
    satirlar = ["Nereye gitmek istersin?"]
    for sira, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{sira}] {hedef}")
    return "\n".join(satirlar)

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

def travel():
    """Uzay yolculugu fonksiyonu."""
    pass