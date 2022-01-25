import random

words = ["alfabe", "abide", "anıt", "acayip", "garip",
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
"patlama"]

def getWord():
    return random.choice(words)