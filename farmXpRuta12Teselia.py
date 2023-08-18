
import pyautogui as auto
import random as rnd

dulceAroma=4
auto.sleep(1)


while True==True:
    loc = auto.locateCenterOnScreen("lucha.jpg", confidence=0.5)
    hax = auto.locateCenterOnScreen("cielo.jpg", confidence=0.9)
    print(hax)

    if dulceAroma>=4:
        i = 0
        while i <= 3:
            auto.moveTo(1571, 760)
            auto.click()
            auto.sleep(.3)
            auto.moveTo(963, 523)
            auto.click()
            i = i + 1

        auto.moveTo(1890, 650)
        auto.click()
        auto.sleep(1)
        auto.moveTo(1740, 768)
        auto.click()
        auto.sleep(1)
        auto.click(1144, 443)
        auto.click()
        auto.click()
        auto.click()
        auto.sleep(5)
        i = 0
        while i <= 3:
            auto.click(1571, 760)
            auto.click()
            auto.sleep(.3)
            auto.moveTo(963, 523)
            auto.click()
            auto.click()
            i = i + 1

        auto.keyDown("w")
        auto.sleep(3.5)
        auto.keyUp("w")
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

        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")

        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")
        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")

        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")
        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")
        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")
        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")
        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")
        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")
        auto.keyDown("m")
        auto.sleep(.4)
        auto.keyUp("m")
        auto.sleep(.3)
        auto.keyDown("s")
        auto.sleep(2.5)
        auto.keyUp("s")

        auto.sleep(1)
        auto.press("1")
        auto.keyDown("a")
        auto.sleep(3.1)
        auto.keyUp("a")
        auto.keyDown("w")
        auto.sleep(.025)
        auto.keyUp("w")

        dulceAroma=0
        auto.sleep(1.5)
    hax = auto.locateCenterOnScreen("cielo.jpg", confidence=0.8)
    print(hax)
    i = 0
    while i <= 3:
        auto.click(1571, 760)
        auto.click()
        auto.sleep(.3)
        auto.moveTo(963, 523)
        auto.click()
        auto.click()
        i = i + 1

    while hax!=None:
        loc = auto.locateCenterOnScreen("lucha.jpg", confidence=0.5)
        comb= auto.locateCenterOnScreen("comb.jpg",confidence=0.5)
        tranq=auto.locateCenterOnScreen("tranq.jpg",confidence=0.5)
        if loc != None:
            auto.moveTo(loc)
            auto.click()
            auto.sleep(.2)
            if comb!=None:
                auto.moveTo(603,702)
                auto.click()
                auto.click()
                auto.sleep(1.5)
            if tranq!=None:
                auto.moveTo(603, 702)
                auto.click()
                auto.click()
                auto.sleep(1.5)
            else:
                auto.moveTo(400, 760)
                auto.click()
                auto.click()
                auto.sleep(1.5)


            auto.sleep(2.2)
            hax = auto.locateCenterOnScreen("cielo.jpg", confidence=0.8)


    print(hax)
    auto.moveTo(1890,561)
    auto.sleep(.1)
    auto.click()
    auto.moveTo(1747,707)
    auto.click()
    i = 0
    while i <= 3:
        auto.click(1571, 760)
        auto.click()
        auto.sleep(.3)
        auto.moveTo(963, 523)
        auto.click()
        auto.click()
        i = i + 1

    auto.sleep(4)
    i = 0
    while i <= 3:
        auto.click(1571, 760)
        auto.click()
        auto.sleep(.3)
        auto.moveTo(963, 523)
        auto.click()
        auto.click()
        i = i + 1
    auto.sleep(5)
    i = 0
    while i <= 3:
        auto.click(1571, 760)
        auto.click()
        auto.sleep(.3)
        auto.moveTo(963, 523)
        auto.click()
        auto.click()
        i = i + 1
    auto.sleep(5)


    hax = auto.locateCenterOnScreen("cielo.jpg", confidence=0.8)
    while hax!=None:
        loc = auto.locateCenterOnScreen("lucha.jpg", confidence=0.5)
        comb= auto.locateCenterOnScreen("comb.jpg",confidence=0.5)
        tranq=auto.locateCenterOnScreen("tranq.jpg",confidence=0.5)

        if loc != None:
            auto.moveTo(loc)
            auto.click()
            auto.sleep(.2)

            if comb != None:
                auto.moveTo(603, 702)
                auto.click()
                auto.click()
                auto.sleep(1.5)
            if tranq!=None:
                auto.moveTo(603, 702)
                auto.click()
                auto.click()
                auto.sleep(1.5)
            else:
                auto.moveTo(400, 760)
                auto.click()
                auto.click()
                auto.sleep(1.5)

        hax = auto.locateCenterOnScreen("cielo.jpg", confidence=0.8)
        i = 0
        while i <= 3:
            auto.click(1571, 760)
            auto.click()
            auto.sleep(.3)
            auto.moveTo(963, 523)
            auto.click()
            auto.click()
            i = i + 1
        auto.sleep(2)

    hax = auto.locateCenterOnScreen("cielo.jpg", confidence=0.8)
    i = 0
    while i <= 3:
        auto.click(1571, 760)
        auto.click()
        auto.sleep(.3)
        auto.moveTo(963, 523)
        auto.click()
        auto.click()
        i = i + 1

    while hax!=None:
        loc = auto.locateCenterOnScreen("lucha.jpg", confidence=0.5)
        comb= auto.locateCenterOnScreen("comb.jpg",confidence=0.5)
        tranq=auto.locateCenterOnScreen("tranq.jpg",confidence=0.5)

        if loc != None:
            auto.moveTo(loc)
            auto.click()
            auto.sleep(.2)

            if comb != None:
                auto.moveTo(603, 702)
                auto.click()
                auto.click()
                auto.sleep(1.5)
            if tranq!=None:
                auto.moveTo(603, 702)
                auto.click()
                auto.click()
                auto.sleep(1.5)
            else:
                auto.moveTo(400, 760)
                auto.click()
                auto.click()
                auto.sleep(1.5)
        hax = auto.locateCenterOnScreen("cielo.jpg", confidence=0.8)

    dulceAroma = dulceAroma + 1
    auto.sleep(1.5)
    i=0
    while i <= 3:
        auto.click(1571, 760)
        auto.click()
        auto.sleep(.3)
        auto.moveTo(963, 523)
        auto.click()
        auto.click()
        i = i + 1
    auto.sleep(2)



