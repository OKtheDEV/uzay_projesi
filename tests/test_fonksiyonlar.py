from uzay_oyunu.oyun import envanter_metni, hedef_menusu

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