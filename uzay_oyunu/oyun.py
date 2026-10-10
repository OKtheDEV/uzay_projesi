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
    """Gidilebilecek hedefleri numarali liste metni olarak dondurur."""
    satirlar = ["Nereye gitmek istersin?"]
    for sira, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{sira}] {hedef}")
    return "\n".join(satirlar)

def travel():
    """Uzay yolculugu ana dongusu."""
    pass