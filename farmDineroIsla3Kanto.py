import pyautogui as auto

auto.sleep(2)
seguir=True
pp=0
intentos=0
while True==True:
    while seguir==True:

        btnLucha = auto.locateCenterOnScreen("lucha.jpg", confidence=0.5)
        if btnLucha != None:
            if pp >= 26:
                estadoPersian = auto.locateCenterOnScreen("veneno.jpg", confidence=0.8)
                if estadoPersian != None:
                    auto.press("m")
                    auto.press("m")
                    auto.press("m")
                    auto.moveTo(610, 750)
                    auto.sleep(.1)
                    auto.click()
                    pp = 29
                else:
                    auto.click(btnLucha)
                    auto.moveTo(404, 750)
                    auto.click()
                    auto.click()
                    auto.click()
                    intentos = 0
                    pp = pp + 1
                    auto.sleep(5.2)
            else:
                estadoPersian = auto.locateCenterOnScreen("veneno.jpg", confidence=0.8)
                if estadoPersian != None:
                    print("envenenado")
                    auto.press("m")
                    auto.press("m")
                    auto.press("m")
                    auto.moveTo(610, 750)
                    auto.sleep(.1)
                    auto.click()
                    pp = 29
                else:
                    auto.click(btnLucha)
                    auto.sleep(.1)
                    auto.click()
                    auto.click()
                    auto.click()
                    pp = pp + 1
                    auto.sleep(5.2)
                    intentos = 0

        if intentos>=45:
            pp=29

        if pp>=27:
            auto.sleep(2)
            auto.moveTo(1890, 650)
            auto.click()
            auto.sleep(1)
            auto.moveTo(1740, 768)
            auto.click()
            auto.sleep(1)
            auto.click(1140, 697)
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

            #salimos del centro

            pp=0
            auto.press("1")
            auto.keyDown("a")
            auto.sleep(1)
            auto.keyUp("a")
            auto.keyDown("w")
            auto.sleep(2)
            auto.keyUp("w")
            auto.keyDown("d")
            auto.sleep(1.4)
            auto.keyUp("d")
            auto.keyDown("s")
            auto.sleep(.6)
            auto.keyUp("s")
            auto.keyDown("a")
            auto.sleep(1.8)
            auto.keyUp("a")
            auto.keyDown("s")
            auto.sleep(.5)
            auto.keyUp("s")
            auto.keyDown("a")
            auto.sleep(.15 )
            auto.keyUp("a")
            auto.keyDown("w")
            auto.sleep(.4)
            auto.keyUp("w")
            auto.keyDown("a")
            auto.sleep(.5)
            auto.keyUp("a")
            auto.keyDown("s")
            auto.sleep(.3)
            auto.keyUp("s")
            auto.keyDown("a")
            auto.sleep(.5)
            auto.keyUp("a")

        #buscamos en hierba
        auto.keyDown("s")
        auto.sleep(.5)
        auto.keyUp("s")
        auto.keyDown("w")
        auto.sleep(.2)
        auto.keyUp("w")

        intentos=intentos+1
        print(intentos)





