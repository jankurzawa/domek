# Narysuj domek według podanego schematu.

#   * Na bazie kwadratu o długości boku 200 (można skopiować z przykładu)
#
#   * Drzwi to:
#       Prostokąt o szerokości 2/5 szerokości domku i wysokości 1/3 wysokości domku.
#       Umiejscowione są symetrycznie na środku dolnej krawędzi.
#
#   * Dom posiada cztery okna:
#       * Wszystkie o wysokości 1/7 wysokości domku.
#       * Oddalone są od bocznych krawędzi domku o 1/10 szerokości domku oraz o 1/10 szerokości domku od środka.
#       * Dolna krawędź dolnych okien znajduje się w połowie domku.
#       * Dolna krawędź górnych okien znajduje się o 2/7 wysokości domku poniżej górnej krawędzi domku.

# Po zakończeniu pracy (na zajęciach lub w domu) prześlij rozwiązanie na swoją gałązkę gita.
# Przypomnienie przydatnych komend:
#
############# Ustawianie swoich danych
# git config --global user.name "Imię nazwisko"
# git config --global user.email "mail"
#############
#
############# Tworzenie gałązki z przepięciem na nią
# git checkout -b <nazwa brancha>
#############
#
############# Dodanie i zacommitowanie pliku
# git add <plik>
# git commit -m “wiadomość w commicie”
#############
#
############# Wypchnięcie zmian na zdalne repo
# (pierwszy raz) git push -u origin HEAD
# (kolejne razy) git push
#############

import turtle

## funkcja 'prostokąt' rysuje prostokąt
# lewy_dolny_rog_x i lewy_dolny_rog_y to współrzędne lewego-dolnego rogu kwadratu
# wysokosc i szerokosc to wymiary kwadratu
def prostokat(lewy_dolny_rog_x, lewy_dolny_rog_y, wysokosc, szerokosc):
    turtle.penup()
    turtle.setposition(lewy_dolny_rog_x, lewy_dolny_rog_y)
    turtle.pendown()
    turtle.setposition(lewy_dolny_rog_x, lewy_dolny_rog_y + wysokosc)
    turtle.setposition(lewy_dolny_rog_x + szerokosc, lewy_dolny_rog_y + wysokosc)
    turtle.setposition(lewy_dolny_rog_x + szerokosc, lewy_dolny_rog_y)
    turtle.setposition(lewy_dolny_rog_x, lewy_dolny_rog_y)
    turtle.penup()

## funkcja 'okna' odpowiada za narysowanie czterech okien wywołując 4-krotnie funkcję 'prostokąt' z odpowiednimi (uprzednio obliczonymi) argumentami
# lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu i  szerokosc_domu to dane domu,
# które są punktem odniesienia do proporcjonalnego obliczania lokacji i wymiarów okien
def okna(lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu, szerokosc_domu):
    lewa_krawedz_lewego_okna_x = lewy_dolny_rog_domu_x + (szerokosc_domu / 10) # współrzędna 'x' lewej krawędzi okien po lewej stronie
    lewa_krawedz_prawego_okna_x = lewy_dolny_rog_domu_x + (szerokosc_domu * 6 / 10) # współrzędna 'x' lewej krawędzi okien po prawej stronie
    dolna_krawedz_dolnego_okna_y = lewy_dolny_rog_domu_y + (wysokosc_domu / 2) # współrzędna 'y' dolnej krawędzi okien dolnych
    dolna_krawedz_gornego_okna_y = lewy_dolny_rog_domu_y + (wysokosc_domu * 5 / 7) # współrzędna 'y' dolnej krawędzi okien górnych

    wysokosc_okna = wysokosc_domu / 7
    szerokosc_okna = szerokosc_domu * 3 / 10

    prostokat(lewa_krawedz_lewego_okna_x, dolna_krawedz_dolnego_okna_y,wysokosc_okna, szerokosc_okna) # lewe, dolne okno
    prostokat(lewa_krawedz_prawego_okna_x, dolna_krawedz_dolnego_okna_y, wysokosc_okna, szerokosc_okna, ) # prawe, dolne okno
    prostokat(lewa_krawedz_lewego_okna_x, dolna_krawedz_gornego_okna_y, wysokosc_okna, szerokosc_okna, ) # lewe, górne okno
    prostokat(lewa_krawedz_prawego_okna_x, dolna_krawedz_gornego_okna_y, wysokosc_okna, szerokosc_okna, ) # prawe, górne okno

## funkcja 'drzwi' odpowiada za narysowanie drzwi poprzez wywołanie funkcji 'prostokąt' z odpowiednimi (uprzednio obliczonymi) argumentami
# lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu i  szerokosc_domu to dane domu,
# które są punktem odniesienia do proporcjonalnego obliczania lokacji i wwymiarów drzwi
def drzwi(lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu, szerokosc_domu):
    wysokosc_drzwi = wysokosc_domu / 3
    szerokosc_drzwi = szerokosc_domu * 2 / 5

    srodek_dolnej_krwedzi_drzwi_x = lewy_dolny_rog_domu_x + (szerokosc_domu / 2) # współrzędna 'x' środka drzwi
    lewy_dolny_rog_drzwi_x = srodek_dolnej_krwedzi_drzwi_x - (szerokosc_drzwi / 2) # współrzędna 'x' lewego, dolnego rogu drzwi
    lewy_dolny_rog_drzwi_y = lewy_dolny_rog_domu_y # współrzędna 'y' lewego, dolnego rogu drzwi PS. Przypisanie wartości do nowej zmiennej jest jedynie dla lepszej czytelności w późniejszym kodzie

    prostokat(lewy_dolny_rog_drzwi_x, lewy_dolny_rog_drzwi_y, wysokosc_drzwi, szerokosc_drzwi) # drzwi

## funkcja 'dach' odpowiada za narysowanie trójkąta równoraminennego, który stanowi dach
def dach(lewy_gorny_rog_domu_x, lewy_gorny_rog_domu_y, szedokosc_domu):
    turtle.penup()
    turtle.setposition(lewy_gorny_rog_domu_x, lewy_gorny_rog_domu_y)
    turtle.pendown()
    turtle.setposition(lewy_gorny_rog_domu_x - szedokosc_domu / 10, lewy_gorny_rog_domu_y)
    turtle.setposition(lewy_gorny_rog_domu_x + (szedokosc_domu / 2), lewy_gorny_rog_domu_y + (szedokosc_domu / 3))
    turtle.setposition(lewy_gorny_rog_domu_x + szedokosc_domu + (szedokosc_domu / 10), lewy_gorny_rog_domu_y)
    turtle.setposition(lewy_gorny_rog_domu_x - szedokosc_domu / 10, lewy_gorny_rog_domu_y)
    turtle.penup()

## funkcja 'dom' to główna funkcja odpowiadająca za narysowanie całego domu w tym: okien, drzwi, domu (ścian, sufitu, podłogi)
# lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y to współrzędne lewege, dolnego rogu domu
# wysokosc_domu i szerokosc_domu to wymiary domu, według których obliczane są pozostałe elementy
def dom(lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu, szerokosc_domu):

    prostokat(lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu, szerokosc_domu) # ściany, sufit, podłoga (dom)

    okna(lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu, szerokosc_domu) # okna

    drzwi(lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu, szerokosc_domu) # drzwi

    lewy_gorny_rog_domu_x = lewy_dolny_rog_domu_x # współrzędna 'x' lewego, górnego rogu domu
    lewy_gorny_rog_domu_y = lewy_dolny_rog_domu_y + wysokosc_domu # współrzędna 'y' lewego, górnego rogu domu

    dach(lewy_gorny_rog_domu_x, lewy_gorny_rog_domu_y, szerokosc_domu) # dach

# Dane Wejściowe:
# wymiary domu oraz współrzędne
wysokosc_domu = 200
szerokosc_domu = 200
lewy_dolny_rog_domu_x = 0
lewy_dolny_rog_domu_y = 0

dom(lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y, wysokosc_domu, szerokosc_domu) # dom - główna funkcja

turtle.exitonclick()
