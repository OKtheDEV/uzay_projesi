import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu, galaksi_kur

def test_envanter_metni():
    assert (
        envanter_metni(True, False, True)
        == "Sende: bol kredi, yetenekli bir pilot"
    )
    assert envanter_metni(False, False, False) == ""
    assert (
        envanter_metni(True, True, True)
        == "Sende: bol kredi, guclu motorlar, yetenekli bir pilot"
    )

def test_hedef_menusu():
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen
    assert hedef_menusu([]) == "Nereye gitmek istersin?"

def test_galaksi_kur():
    veri = {
        "gezegenler": ["dünya", "mars"],
        "baglantilar": {"dünya": ["mars"], "mars": ["dünya"]},
        "baslangic": "dünya",
        "yakit": 100,
    }
    g = galaksi_kur(**veri)
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100

    # yakit parametresi verilmediginde varsayilan 50 olmali
    g2 = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g2["yakit"] == 50

    # baslangic listede yoksa ValueError vermeli
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "jupiter")