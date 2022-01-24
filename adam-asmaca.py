import random
import colorama
from colorama import Fore, Back, Style, init

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]

while True:
    print(("----->") + "Adam Asmaca Oyunu" + ("<-----"))

    kelime = random.choice(["alfabe", "abide", "anıt", "acayip", "garip",
"acıma", "merhamet", "açıkgöz", "kurnaz", "isim", "adale", "affetmek", "bağışlamak",
"kırmızı","alelade","sıradan","iltihap", "girişken","bağışlamak","bayındır","veteriner",
"bellek","beyanat","zavallı","meridyen","operatör","yürekli","ağırbaşlı","cimri","mühendis",
"ekseriyet","darılmak","kıymetli","vaziyet","arkadaş","eklem","ekonomi","güvenlik","endüstri",
"enteresan","faaliyet","garip","istikbal","dilbilgisi","kuvvetli","sonbahar","komedi","duygulu",
"haysiyet","kaplıca","karakter","samimi","yönetim","ihracat","ihtiyaç","sandalye","açıklama",
"ithalat","yetenek","karabasan","sermaye","kuruluş","gereksiz","tapınak","hapishane","yaratık",
"basımevi","milletvekili","uygarlık","yardımcı","bağımsız","öğretmen","rutubet","Nasihat",
"mükafat","hiddet","öğrenim","teşkilat","orijinal","ayakkabı","siyaset","rastlantı","Saldırı",
"sürekli","sorumluluk","kuşku","kutlama","uçurum","millet","memleket","vilayet","arlıklı",
"dönemeç","vaziyet","karat","zorunlu","zeybek","zehir","metelik","subay","ziraat","zırnık",
"patlama"])
    adim = 0
    tahmin = []
    durum = True
    kont = True
    harfler = []

    while True:
        print(resim[adim])
        for i, char in enumerate(kelime): # i index numarası char kelimenin harfi
            print(Fore.BLACK + Back.LIGHTCYAN_EX + char + Style.RESET_ALL if i in tahmin else Fore.BLACK + Back.LIGHTCYAN_EX + "_"+ Style.RESET_ALL,end=" ")

        print("harf sayısı:",len(kelime))
        
        if not harfler == []:
            print("Kullandığınız harfler:", end=" ")
            for char in harfler:
                print(char, end= "")
            print()
        while True:
            secim = input("harf >>>  1 veya kelime tahmini>>> 2 ")
            if secim.isdigit():
                secim = int(secim)
                if secim == 1:
                    cevap = input("Harf giriniz: ")
                    cevap = cevap[0]
                    harfler.append(cevap)
                    break
                elif secim == 2:
                    soncevap = input("Kelimeyi Tahmin Edin: ")
                    if soncevap == kelime:
                        print(Fore.WHITE + Back.GREEN + "Kazandınız...." + Style.RESET_ALL)
                        durum = False
                        break
                    else:
                        print(Fore.WHITE + Back.RED + "malesef yanlış cevap.." + Style.RESET_ALL)
                        break

        if secim == 1:
            for i, char in enumerate(kelime):
                if cevap == char:
                    tahmin.append(i)
                    kont = False
                else:
                    tahmin.append("-")
            if kont:
                adim += 1
            kont = True
        elif durum:
            adim += 1
        else:
            break
        if adim >= len(resim):
            print(Fore.WHITE + Back.BLACK + "Kaybettiniz....." + Style.RESET_ALL)
            print("Doğru cevap",Fore.WHITE + Back.RED + kelime + Style.RESET_ALL,"olacaktı.")
            break

    if not "e" == input("Tekrar Oynamak İstermisiniz? (e/h): "):
        break