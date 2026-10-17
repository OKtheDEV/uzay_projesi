# Uzay Projesi - 4. Hafta

## Görev 4 - Önbellekli Rota Sayacı Performans Ölçümü (adım=20)
- **Önbelleksiz süre:** 3.082821 saniye
- **Önbellekli süre:** 0.000065 saniye
- **cache_info:** CacheInfo(hits=91, misses=98, maxsize=None, currsize=98)

## Bonus Görev - Meşgul Bekleme (Busy Waiting) ve time.sleep Farkı
- **Meşgul Bekleme (Busy Waiting):** İşlemcinin sürekli bir döngü içinde koşulun gerçekleşip gerçekleşmediğini aralıksız denetlemesidir. Bu yöntem esnasında CPU çekirdeği %100 yük altında kalır, fazladan güç tüketir ve sistem kaynaklarını gereksiz yere bloke eder.
- **time.sleep():** İşletim sistemine ilgili iş parçacığını (thread) belirtilen süre kadar pasif/uyku moduna almasını bildirir. İşlemci bu bekleme süresince başka işlemleri yürütebilir ve sistem kaynakları verimli kullanılır.