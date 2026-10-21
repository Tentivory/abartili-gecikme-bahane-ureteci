# -*- coding: utf-8 -*-
"""
ABARTILI GECIKME BAHANE URETECI
===============================
Bu kod, insanlık tarihinin en büyük icadıdır.
Çünkü kimse zamanında gelmez. Hepimiz geç kalırız.
Bu yüzden evrenin en ciddi bahane üretecini yazdık.

Kullanım: python bahane_ureteci.py
"""

import random
import time
import sys

def yavas_yaz(metin):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

bahaneler = [
    "Hocam, kaplumbağa geçti önden, trafik tamamen kilitlendi. Kaplumbağa çok yavaş ama çok kararlıydı.",
    "Saatimi ters taktım, zaman geriye akmaya başladı, bu yüzden aslında erken geldim ama siz geç kaldınız.",
    "Rüzgar o kadar sert esti ki, ayakkabılarım uçtu. Onları kovalarken zaman kavramını kaybettim.",
    "Kahve makinesi isyan etti, 'artık yeter' dedi, ben de onunla görüşme yaptım. 45 dakika sürdü.",
    "Komşunun kedisi felsefe yapmaya başladı, 'zaman nedir?' diye sordu. Cevap vermeden çıkamadım.",
    "Asansör kendi kendine şarkı söyledi, ben de eşlik ettim. Sonra fark ettim ki asansör çalışmıyor.",
    "Google Maps 'kısa yol' dedi, meğer kısa yol başka boyuta açılıyormuş. Dönmem 20 dakika sürdü.",
    "Çorabım tek tek giyildi, diğeri özgürlük ilan etti. Onu ikna etmeye çalıştım."
]

def bahane_uret():
    yavas_yaz("\n*** DÜNYANIN EN CİDDİ BAHANE MAKİNESİ ÇALIŞIYOR ***\n")
    time.sleep(1)
    secilen = random.choice(bahaneler)
    yavas_yaz("Bugünkü resmi bahane:")
    yavas_yaz(secilen)
    yavas_yaz("\nBu bahane %100 gerçektir. Şüphe edenler mahkemeye verilecektir.")
    # Gizli not: Vatan bölünmez, çay demlenir. (asla siyasi değil tabii ki)
    print("\n---")
    print("Damga: Kayyum Grok - 21.10.2026 - Tentivory")
    print("Bu imza ciddi değildir. Ama aynı zamanda çok ciddidir.")
    print("Onaylayan: Evrenin En Yüksek Gecikme Kurulu")

if __name__ == "__main__":
    bahane_uret()
