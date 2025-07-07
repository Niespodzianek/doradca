import os
import time

def nacisnij_enter(tekst):
    input(tekst)
    return 0

def czysc_ekran():
    os.system("clear")
    return 0

def zatrzymaj_prace_programu_na_sekund(sekundy):
    time.sleep(sekundy)
    return 0

def w_budowie():
    print("\nFunkcja w budowie !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    nacisnij_enter("\nNaciśnij ENTER aby kontynuować")
    return 0
