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
import methods

wysokosc_domu = 200
szerokosc_domu = 200
lewy_dolny_rog_domu_x = 0
lewy_dolny_rog_domu_y = 0

methods.dom(wysokosc_domu, szerokosc_domu, lewy_dolny_rog_domu_x, lewy_dolny_rog_domu_y)

turtle.exitonclick()
