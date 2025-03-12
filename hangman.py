#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 02:54:07 2025

@author: baharzengoglu
"""

import random

kelimeler = ["python", "programlama", "bilgisayar", "veritabani", "yazilim"]
kelime = random.choice(kelimeler)
tahmin_edilen = ["_"] * len(kelime)
hak = 6
harfler = []

while hak > 0 and "_" in tahmin_edilen:
    print(" ".join(tahmin_edilen))
    tahmin = input("Harf gir: ").lower()

    if tahmin in harfler:
        print("Bu harfi zaten söyledin.")
        continue
    
    harfler.append(tahmin)
    
    if tahmin in kelime:
        for i in range(len(kelime)):
            if kelime[i] == tahmin:
                tahmin_edilen[i] = tahmin
    else:
        hak -= 1
        print(f"Yanlış! Kalan hak: {hak}")

if "_" not in tahmin_edilen:
    print("Tebrikler, kelimeyi buldun:", kelime)
else:
    print("Kaybettin! Kelime şuydu:", kelime)