import random
import colorama
from colorama import Fore, Back, Style, init

pictures = ["""
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

    word = random.choice(["alfabe", "abide", "anıt", "acayip", "garip",
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
    step = 0
    guess = []
    status = True
    check = True
    letters = []

    while True:
        print(pictures[step])
        for i, char in enumerate(word): # i index numarası char kelimenin harfi
            print(Fore.BLACK + Back.LIGHTCYAN_EX + char + Style.RESET_ALL if i in guess else Fore.BLACK + Back.LIGHTCYAN_EX + "_"+ Style.RESET_ALL,end=" ")

        print("harf sayısı:",len(word))
        
        if not letters == []:
            print("Kullandığınız harfler:", end=" ")
            for char in letters:
                print(char, end= "")
            print()
        while True:
            choice = input("harf >>>  1 veya kelime tahmini>>> 2 ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    answer = input("Harf giriniz: ")
                    answer = answer[0]
                    letters.append(answer)
                    break
                elif choice == 2:
                    lastAnswer = input("Kelimeyi Tahmin Edin: ")
                    if lastAnswer == word:
                        print(Fore.WHITE + Back.GREEN + "Kazandınız...." + Style.RESET_ALL)
                        status = False
                        break
                    else:
                        print(Fore.WHITE + Back.RED + "malesef yanlış cevap.." + Style.RESET_ALL)
                        break

        if choice == 1:
            for i, char in enumerate(word):
                if answer == char:
                    guess.append(i)
                    check = False
                else:
                    guess.append("-")
            if check:
                step += 1
            check = True
        elif status:
            step += 1
        else:
            break
        if step >= len(pictures):
            print(Fore.WHITE + Back.BLACK + "Kaybettiniz....." + Style.RESET_ALL)
            print("Doğru cevap",Fore.WHITE + Back.RED + word + Style.RESET_ALL,"olacaktı.")
            break

    if not "e" == input("Tekrar Oynamak İstermisiniz? (e/h): "):
        break