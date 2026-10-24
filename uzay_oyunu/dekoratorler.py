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

def say(fonk):
    """Fonksiyonun çağrı sayısını bir nitelikte (.cagri) tutan dekoratör."""

    @functools.wraps(fonk)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1
        return fonk(*args, **kwargs)

    sarmalayici.cagri = 0
    return sarmalayici

def log_cagri(fonk):
    """Fonksiyon adını, argümanlarını ve dönüş değerini yazdıran loglama dekoratörü."""

    @functools.wraps(fonk)
    def sarmalayici(*args, **kwargs):
        # Konumsal ve adlı argümanların string temsillerini hazırlıyoruz
        arg_parcalari = [repr(arg) for arg in args]
        kwarg_parcalari = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        tum_argumanlar = ", ".join(arg_parcalari + kwarg_parcalari)

        # Çağrı öncesi log
        print(f"-> {fonk.__name__}({tum_argumanlar})")

        # Fonksiyonu çalıştır
        sonuc = fonk(*args, **kwargs)

        # Çağrı sonrası log
        print(f"<- {fonk.__name__} = {repr(sonuc)}")

        return sonuc

    return sarmalayici

def sinirla(alt: int | float, ust: int | float):
    """Dekore edilen fonksiyonun ilk argümanının [alt, ust] aralığında olmasını zorunlu kılan dekoratör."""

    def dekorator(fonk):
        @functools.wraps(fonk)
        def sarmalayici(*args, **kwargs):
            # İlk argümanı konumsal veya adlı (keyword) argümanlardan alıyoruz
            if args:
                deger = args[0]
            elif kwargs:
                deger = next(iter(kwargs.values()))
            else:
                raise ValueError(
                    f"{fonk.__name__}: Argüman bulunamadı."
                )  # Boş çağrı kontrolü

            if not (alt <= deger <= ust):
                raise ValueError(
                    f"{fonk.__name__}: {deger} değeri {alt}-{ust} aralığında değil"
                )

            return fonk(*args, **kwargs)

        return sarmalayici

    return dekorator

# Başlangıç yakıtı 100 kabul edilerek:
MEVCUT_YAKIT = 100

@sinirla(0, 100)
def yakit_harca(miktar: int) -> int:
    """Verilen miktar kadar yakıt harcar ve kalan yakıtı döner."""
    global MEVCUT_YAKIT
    MEVCUT_YAKIT -= miktar
    return MEVCUT_YAKIT