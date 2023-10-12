import turtle
def prostokat(wysokosc, szerokosc, lewy_rog_x, lewy_rog_y):
    turtle.penup()
    turtle.setposition(lewy_rog_x, lewy_rog_y)
    turtle.pendown()
    turtle.setposition(lewy_rog_x, lewy_rog_y + wysokosc)
    turtle.setposition(lewy_rog_x + szerokosc, lewy_rog_y + wysokosc)
    turtle.setposition(lewy_rog_x + szerokosc, lewy_rog_y)
    turtle.setposition(lewy_rog_x, lewy_rog_y)
    turtle.penup()

def okna(wysokosc_okna, szerokosc_okna, wysokosc_domu, szerokosc_domu, lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y):
    lewa_krawedz_lewego_okna_x = lewy_dolny_rog_domu_x + (szerokosc_domu / 10)
    lewa_krawedz_prawego_okna_x = lewy_dolny_rog_domu_x + (szerokosc_domu * 6 / 10)
    dolna_krawedz_dolnego_okna_y = lewy_dolny_rog_domu_y + (wysokosc_domu / 2)
    dolna_krawedz_gornego_okna_y = lewy_dolny_rog_domu_y + (wysokosc_domu * 5 / 7)

    prostokat(wysokosc_okna, szerokosc_okna, lewa_krawedz_lewego_okna_x, dolna_krawedz_dolnego_okna_y)
    prostokat(wysokosc_okna, szerokosc_okna, lewa_krawedz_prawego_okna_x, dolna_krawedz_dolnego_okna_y)
    prostokat(wysokosc_okna, szerokosc_okna, lewa_krawedz_lewego_okna_x, dolna_krawedz_gornego_okna_y)
    prostokat(wysokosc_okna, szerokosc_okna, lewa_krawedz_prawego_okna_x, dolna_krawedz_gornego_okna_y)

def drzwi(wysokosc_drzwi, szerokosc_drzwi, srodek_dolnej_krwedzi_drzwi_x, srodek_dolnej_krwedzi_drzwi_y):
    lewy_dolny_rog_drzwi_x = srodek_dolnej_krwedzi_drzwi_x - (szerokosc_drzwi / 2)
    lewy_dolny_rog_drzwi_y = srodek_dolnej_krwedzi_drzwi_y
    prostokat(wysokosc_drzwi, szerokosc_drzwi, lewy_dolny_rog_drzwi_x, lewy_dolny_rog_drzwi_y)

def dach(lewy_gorny_rog_domu_x, lewy_gorny_rog_domu_y, szedokosc_domu):
    turtle.penup()
    turtle.setposition(lewy_gorny_rog_domu_x, lewy_gorny_rog_domu_y)
    turtle.pendown()
    turtle.setposition(lewy_gorny_rog_domu_x - szedokosc_domu / 10, lewy_gorny_rog_domu_y)
    turtle.setposition(lewy_gorny_rog_domu_x + (szedokosc_domu / 2), lewy_gorny_rog_domu_y + (szedokosc_domu / 3))
    turtle.setposition(lewy_gorny_rog_domu_x + szedokosc_domu + (szedokosc_domu / 10), lewy_gorny_rog_domu_y)
    turtle.setposition(lewy_gorny_rog_domu_x - szedokosc_domu / 10, lewy_gorny_rog_domu_y)
    turtle.penup()

def dom(wysokosc_domu, szedokosc_domu, lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y):

    prostokat(wysokosc_domu, szedokosc_domu, lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y)

    wysokosc_okna = wysokosc_domu / 7
    szerokosc_okna = szedokosc_domu * 3 / 10

    okna(wysokosc_okna, szerokosc_okna, wysokosc_domu, szedokosc_domu, lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y)

    wysokosc_drzwi = wysokosc_domu / 3
    szerokosc_drzwi = szedokosc_domu * 2 / 5
    srodek_dolnej_krwedzi_drzwi_x = lewy_dolny_rog_domu_x + (szedokosc_domu / 2)
    srodek_dolnej_krwedzi_drzwi_y = lewy_dolny_rog_domu_y

    drzwi(wysokosc_drzwi, szerokosc_drzwi, srodek_dolnej_krwedzi_drzwi_x, srodek_dolnej_krwedzi_drzwi_y)

    lewy_gorny_rog_domu_x = lewy_dolny_rog_domu_x
    lewy_gorny_rog_domu_y = lewy_dolny_rog_domu_y + wysokosc_domu

    dach(lewy_gorny_rog_domu_x, lewy_gorny_rog_domu_y, szedokosc_domu)
