from colorama import Fore, Back, Style
from pictures import Pictures
from word import getWord

while True:
    print(("----->") + "Adam Asmaca Oyunu" + ("<-----"))

    word = getWord()
    pic = Pictures()
    guess = []
    status = True
    check = True
    letters = []

    while True:
        print(pic.getPicture())
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
                pic.nextStep()
            check = True
        elif status:
            pic.nextStep()
        else:
            break
        if pic.isEnd():
            print(Fore.WHITE + Back.BLACK + "Kaybettiniz....." + Style.RESET_ALL)
            print("Doğru cevap",Fore.WHITE + Back.RED + word + Style.RESET_ALL,"olacaktı.")
            break

    if not "e" == input("Tekrar Oynamak İstermisiniz? (e/h): "):
        break