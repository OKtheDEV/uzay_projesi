def gorev_kaydi(
    baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str
) -> str:
    """Gorev basligi, yapilacak adimlar, oncelik derecesi ve ek bilgileri

    formatlayarak dondurur.
    """
    satirlar = [f"[{oncelik.upper()}] {baslik}"]

    for sira, adim in enumerate(adimlar, start=1):
        satirlar.append(f"  {sira}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f"  {anahtar}: {deger}")

    metin = "\n".join(satirlar)
    print(metin)
    return metin

if __name__ == "__main__":
    # 1. Bicim: Standart ve argumanlari dogrudan gecerek cagri
    gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="YÜKSEK",
        sorumlu="Ayşe",
    )

    print("\n" + "=" * 40 + "\n")

    # 2. Bicim: Listeyi (*) ve sozluk eklerini (**) acarak cagri
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}

    gorev_kaydi(
        "Kara deliğe atla",
        *adim_listesi,
        oncelik="YÜKSEK",
        **ek_bilgiler,
    )