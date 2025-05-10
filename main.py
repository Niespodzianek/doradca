import pandas
import random

# zmienne
otwarcie = None
zamkniecie = None
maxi = None
mini = None
obrot = None

# testery
test_1 = None

def generator_sesji_gieldowej():
	notowania = []
	liczba_sesji = 200
	licznik = 0
	notowanie = 100
	zakres_wahan = 0
	while licznik < liczba_sesji:
		if licznik > 0:
			zakres_wahan = random.randint(-10, 10)
			notowanie = zakres_wahan / 100 * notowanie + notowanie
		licznik += 1 
		print(f"Notowanie: {licznik} - kurs: {notowanie:.2f} PLN, zmiana o: {zakres_wahan}")
		notowania.append(notowanie)
	return notowania

def dopisywanie_danych(dane):
	dane["srednia_K"] = dane.kurs.rolling(window = 21, min_periods = 21).mean()
	dane["srednia_D"] = dane.kurs.rolling(window = 55, min_periods = 55).mean()
	odchylenie = dane.kurs.rolling(window = 21, min_periods = 21).std()
	dane["boll_D"] = dane["kurs"] - odchylenie
	dane["boll_G"] = dane["kurs"] + odchylenie
	return dane

def analizator_kursu(dane):
	print(dane)
	pozycja = len(dane.kurs) - 1
	notowanie = dane.loc[pozycja, "kurs"]
	srednia_K = dane.loc[pozycja, "srednia_K"]
	srednia_D = dane.loc[pozycja, "srednia_D"]
	boll_D = dane.loc[pozycja, "boll_D"]
	boll_G = dane.loc[pozycja, "boll_G"]
	print(f"{notowanie:.2f}, {srednia_K:.2f}, {srednia_D:.2f}")
	if srednia_K > srednia_D:
		if notowanie > srednia_K:
			komentarz = "Silny trend rosnacy"
		elif srednia_D > notowanie:
			komentarz = "Trend rosnacy, gleboka korekta, mozliwosc otwarcia dlugiej pozycji"
		elif srednia_K > notowanie:
			komentarz = "Trend rosnacy w korekcie"
		else:
			komentarz = "Kurs na sredniej"
		if notowanie > boll_G:
			komentarz = "Trend rosnacy, mocno przegrzany, mozliwosc korekty"
		elif boll_D > notowanie:
			komentarz = "Trend rosnacy, gleboka kortekta, okazja otwarcia dlugiej pozycji"
	elif srednia_D > srednia_K:
		if srednia_K > notowanie:
			komentarz = "Silny trend spadkowy"
		elif notowanie > srednia_D:
			komentarz = "Trend spadkowy, gleboka korekta, mozliwosc otwarcia krotkiej pozycji"
		elif notowanie > srednia_K:
			komentarz = "Trend spadkowy w korekcie"
		if boll_D > notowanie:
			komentarz = "Silny trend spadkowy, mozno przegrzany, mozliwosc korekty"
		elif notowanie > boll_G:
			komentarz = "Trend spadkowy, gleboka korekta, okazja otwarcia krotkiej pozycji"
	else:
		komentarz = "Skrzyzowanie srednich"
	return komentarz

def generator_wyniku(nazwa, dane):
    wynik = f"{nazwa} \t- {dane}"
    return wynik

if __name__ == "__main__":
	print("PROGRAM PRACUJE")
	# pozyskanie danych

	dane_analizowanej_spolki = pandas.DataFrame(generator_sesji_gieldowej(), columns = ["kurs"])
	nazwa_analizowanej_spolki = "Apple"
	
	# dopisanie parametrow
	dane_gotowe = dopisywanie_danych(dane_analizowanej_spolki)

	# analizator kursu
	wynik_analizy = analizator_kursu(dane_gotowe)
	wynik_zbiorczy = generator_wyniku(nazwa_analizowanej_spolki, wynik_analizy)
	print(wynik_zbiorczy)

