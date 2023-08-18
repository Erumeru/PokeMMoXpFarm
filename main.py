from builtins import int

#Este script funciona en Vermilion City arriba de los entrenadores dobles de la ruta 6 en kanto, solo se pone en hierba y se activa teniendo el pkmn en primer lugar del equipo con dia de pago en primer ataque
import pyautogui as auto
import random as rnd

auto.FAILSAFE=False
pp=0
seguir=True
auto.sleep(2)
while True==True:
    intentos=0
    while seguir == True:

        auto.keyDown("d")
        auto.sleep(.3)
        auto.keyUp("d")
        auto.keyDown("a")
        auto.sleep(.1)
        auto.keyUp("a")
        loc = auto.locateCenterOnScreen("lucha.jpg", confidence=0.5)
        drowzee = auto.locateCenterOnScreen("drowzee.jpg", confidence=0.6)

        if loc != None:
            intentos=0
            if pp >= 20:
                print("PP de dia de pago usados")
                auto.click(loc)
                random = rnd.randint(1,3)
                if (random%2)==0:
                    auto.moveTo(600, 700)
                else:
                    auto.moveTo(404, 750)
                auto.click()
                auto.click()
                auto.click()
                auto.sleep(10)
                locChar = auto.locateCenterOnScreen("charDer.jpg", confidence=0.5)
                locCharIzq = auto.locateCenterOnScreen("charIzq.jpg", confidence=0.5)
                if locChar == None or locCharIzq == None:
                    loc = auto.locateCenterOnScreen("lucha.jpg", confidence=0.5)
                    auto.click(loc)
                    random = rnd.randint(1, 3)
                    if (random % 2) == 0:
                        auto.moveTo(600, 700)
                    else:
                        auto.moveTo(404, 750)
                    auto.click()
                    auto.click()
                    auto.click()
                if locChar != None or locCharIzq != None:
                    print("terminarada")
                    seguir = False

            if drowzee != None:
                random = rnd.randint(1, 3)
                if (random % 2) == 0:
                    auto.moveTo(loc)
                    auto.click()
                    auto.click()
                    auto.click()
                else:
                    print("ataquebajoa")
                    auto.moveTo(loc)
                    auto.click()
                    auto.moveTo(404, 750)
                    auto.click()

            auto.moveTo(loc)
            auto.click()
            auto.click()
            auto.click()
            pp = pp + 1
        intentos = intentos + 1
        print(loc)
        print(pp)
        print("intentos")
        print(intentos)
        if intentos>=45:
            atras=auto.locateCenterOnScreen("atras.jpg",confidence=0.6)
            if atras!=None:
                auto.moveTo(atras)
                auto.click()
            #Caso que se rompe el script, vuelvo a ciudad carmin y me regreso hacia arriba
            auto.click(1890,650)
            auto.sleep(1)
            auto.click(1740,768)
            auto.sleep(1)
            auto.click(1040,630)
            intentos=0
            auto.sleep(5)
            auto.press("1")
            auto.keyDown("d")
            auto.sleep(1)
            auto.keyUp("d")

            auto.keyDown("w")
            auto.sleep(1.3)
            auto.keyUp("w")

    while seguir == False:
        auto.moveTo(1890, 650)
        auto.click()
        auto.sleep(1)
        auto.moveTo(1740, 768)
        auto.click()
        auto.sleep(1)
        auto.click(1040, 630)
        intentos = 0
        auto.sleep(5)

        auto.keyDown("w")
        auto.sleep(3)
        auto.keyUp("w")
        auto.press("n")
        auto.sleep(.4)

        auto.keyDown("n")
        auto.sleep(.6)
        auto.keyUp("n")

        auto.keyDown("n")
        auto.sleep(.4)
        auto.keyUp("n")

        auto.keyDown("n")
        auto.sleep(.4)
        auto.keyUp("n")

        auto.keyDown("n")
        auto.sleep(.4)
        auto.keyUp("n")

        auto.keyDown("n")
        auto.sleep(.4)
        auto.keyUp("n")
        auto.keyDown("n")
        auto.sleep(.4)
        auto.keyUp("n")
        auto.keyDown("n")
        auto.sleep(.4)
        auto.keyUp("n")
        auto.keyDown("n")
        auto.sleep(.4)
        auto.keyUp("n")

        auto.keyDown("s")
        auto.sleep(1.2)
        auto.keyUp("s")

        auto.sleep(1)

        auto.press("1")
        auto.keyDown("d")
        auto.sleep(.69)
        auto.keyUp("d")

        auto.keyDown("w")
        auto.sleep(1.3)
        auto.keyUp("w")
        pp=0
        seguir = True

