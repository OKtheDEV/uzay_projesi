import functools
import time

def sure_olc(fonk):
    """Fonksiyonun çalışma süresini time.perf_counter() ile ölçüp ekrana yazdıran dekoratör."""

    @functools.wraps(fonk)
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonk(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{fonk.__name__}: {sure:.4f} sn")
        return sonuc

    return sarmalayici

if __name__ == "__main__":
    import json
    from pathlib import Path

    # galaksi.json dosyasından bağlantıları okuyoruz
    galaksi_yolu = Path(__file__).parent / "galaksi.json"
    with open(galaksi_yolu, "r", encoding="utf-8") as f:
        galaksi_verisi = json.load(f)

    baglantilar = galaksi_verisi.get("baglantilar", {})
    baslangic_gezegeni = galaksi_verisi.get("baslangic", "dünya")

    # Hafta 4'teki fonksiyonun @lru_cache kaldırılmış (önbelleksiz) hali:
    def rota_sayisi_onbelleksiz(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        komsular = baglantilar.get(gezegen, [])
        return sum(rota_sayisi_onbelleksiz(komsu, adim - 1) for komsu in komsular)

    # sure_olc ile sarmalıyoruz
    olculu_rota = sure_olc(rota_sayisi_onbelleksiz)

    # adim=20 için çağırıp süreyi ekranda görüyoruz
    toplam_rota = olculu_rota(baslangic_gezegeni, adim=20)
    print(
        f"{baslangic_gezegeni} gezegeninden 20 adımlık rota sayısı: {toplam_rota}"
    )