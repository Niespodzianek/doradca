import yfinance
from funkcje_pomocnicze import czysc_ekran, nacisnij_enter, zatrzymaj_prace_programu_na_sekund, w_budowie
from listy_spolek import wszystkie, polskie, nasdaq, usa_ai, usa_cyberbezp, usa_finanse, usa_chipy, usa_militar
import time

gotowka = 0

def naglowek(gotowka):
	czysc_ekran()
	print(10 * "*"+ "    DORADCA    " + 10 * "*")
	print(35 * "*")
	aktualny_stan_rachunku(gotowka)
	return 0

def aktualny_stan_rachunku(gotowka):
	print(f"Stan konta:\n\tgotówka: {gotowka} PLN\n\nposiadane akcje: ")
	return 0

def pozyskanie_notowan(nazwa_spolki):
	pozyskane_notowania = yfinance.Ticker(nazwa_spolki)
	notowania_spolki = pozyskane_notowania.history(period="max")
	return notowania_spolki

def dopisywanie_danych(dane):
	dane["srednia_K"] = dane.Close.rolling(window = 21, min_periods = 21).mean()
	dane["srednia_D"] = dane.Close.rolling(window = 89, min_periods = 89).mean()
	odchylenie = dane.Close.rolling(window = 21, min_periods = 21).std()
	dane["boll_D"] = dane["Close"] - odchylenie
	dane["boll_G"] = dane["Close"] + odchylenie
	return dane

def analizator(dane):
	# print(dane)
	komentarz = None
	ostatni_wiersz = len(dane.Close) - 1
	notowanie = dane.iloc[ostatni_wiersz, 3]
	srednia_K = dane.iloc[ostatni_wiersz, 7] 
	srednia_D = dane.iloc[ostatni_wiersz, 8]
	boll_D = dane.iloc[ostatni_wiersz, 9] 
	boll_G = dane.iloc[ostatni_wiersz,10] 
	# print(f"{notowanie:.2f}, {srednia_K:.2f}, {srednia_D:.2f}")
	if srednia_K > srednia_D:
		if notowanie > srednia_K:
			komentarz = "Silny trend rosnący"
		elif srednia_D > notowanie:
			komentarz = "Trend rosnący, głęboka korekta, możliwość otwarcia długiej pozycji"
		elif srednia_K > notowanie:
			komentarz = "Trend rosnący w korekcie"
		else:
			komentarz = "Kurs na średniej"
		if notowanie > boll_G:
			komentarz = "Trend rosnący, mocno przegrzany, możliwość korekty"
		elif boll_D > notowanie:
			komentarz = "Trend rosnący, głęboka kortekta, możliwość otwarcia długiej pozycji"
	elif srednia_D > srednia_K:
		if srednia_K > notowanie:
			komentarz = "Silny trend spadkowy"
		elif notowanie > srednia_D:
			komentarz = "Trend spadkowy, głęboka korekta, możliwość otwarcia krótkiej pozycji"
		elif notowanie > srednia_K:
			komentarz = "Trend spadkowy w korekcie"
		if boll_D > notowanie:
			komentarz = "Silny trend spadkowy, mocno przegrzany, możliwość korekty"
		elif notowanie > boll_G:
			komentarz = "Trend spadkowy, głęboka korekta, możliwość otwarcia krótkiej pozycji"
	else:
		komentarz = "Skrzyżowanie średnich"
	return komentarz

def generator_wyniku(nazwa, dane):
    wynik = f"{nazwa} \t- {dane}"
    return wynik

def program(lista, info):
	wynik_dzialania_programu = []
	# tikery analizowanych spolek
	lista_spolek = lista
	 # pozyskanie danych
	for spolka in lista_spolek:
		notowania_surowe = pozyskanie_notowan(spolka)
		# print(f"DEBUG: notowania pozyskane z internetu dla spolki {spolka}: {notowania_surowe}")
		# input("Nacisnij ENTER")
		notowania_przeksztalcone = dopisywanie_danych(notowania_surowe)
		# print(f"DEBUG: notowania przeksztalcone do analizy: {notowania_przeksztalcone}")
		# input("Nacisnij ENTER")
		wynik_analizy = analizator(notowania_przeksztalcone)
		wynik_ostateczny = generator_wyniku(spolka, wynik_analizy)
		wynik_dzialania_programu.append(wynik_ostateczny)
	# wyświetlenie wyniku działania programu
	czysc_ekran()
	naglowek(gotowka)
	print("\n"+ info)
	# print(info)
	for pozycja in wynik_dzialania_programu:
		print(pozycja)
	nacisnij_enter()

if __name__ == "__main__":
	# print("PROGRAM PRACUJE")
	# odczyt z pliku stanu gotówki
	czysc_ekran()
	print("Witaj w programie !!!!!!!!!!!!!! POMOCNIK !!!!!!!!!!!!!!")
	print("Program analizuje notowania wybranych spółek i generuje komentarze")
	nacisnij_enter()
	program_pracuje = True
	while program_pracuje:
		naglowek(gotowka)
		main_menu = input("\nWybierz pozycje z listy głównego MENU:\n(1) Przegląd trendu rynków\n(2) Zmiany w portfelu\n(Q) Wyjście z programu\n\nTwój wybór: ")
		if main_menu == "1":
			petla_pracuje = True
			while petla_pracuje:
				czysc_ekran()
				naglowek(gotowka)
				wybor_przeglad_rynkow = input("\nWybierz pozycje z listy, których kurs akcji Cię interesuje:\n(1) Wszystkie\n(2) Polskie\n(3) NASDAQ\n(4) USA AI\n(5) USA Cyberbezpieczeństwo\n(6) USA Finanse\n(7) USA Chipy\n(8) USA Militarne\n(Q) Powrót do poprzedniego menu\n\nTwój wybór: ")
				if wybor_przeglad_rynkow == "1":
					informacja = "Analiza wszystkich obserwowanych spółek:\n"
					program(lista=wszystkie, info=informacja)
				elif wybor_przeglad_rynkow == "2":
					informacja = "Analiza obserwowanych spółek z GPW:\n"
					program(lista=polskie, info=informacja)
				elif wybor_przeglad_rynkow == "3":
					informacja = "Analiza spółek z rynku NASDAQ:\n"
					program(lista=nasdaq, info=informacja)
				elif wybor_przeglad_rynkow == "4":
					informacja = "Analiza spółek z branży AI:\n"
					program(lista=usa_ai, info=informacja)
				elif wybor_przeglad_rynkow == "5":
					informacja = "Analiza spółek z branży cyberbezpieczeństwa i ochrony danych:\n"
					program(lista=usa_cyberbezp, info=informacja)
				elif wybor_przeglad_rynkow == "6":
					informacja = "Analiza spółek z branży finansów i bankowości:\n"
					program(lista=usa_finanse, info=informacja)
				elif wybor_przeglad_rynkow == "7":
					informacja = "Analiza spółek z branży produkcji układów scalonych:\n"
					program(lista=usa_chipy, info=informacja)
				elif wybor_przeglad_rynkow == "8":
					informacja = "Analiza spółek z branży produkcji bronii:\n"
					program(lista=usa_militar, info=informacja)
				elif wybor_przeglad_rynkow == "Q" or wybor_przeglad_rynkow == "q":
					petla_pracuje = False
				else:
					print("\nBłędny wybór !!!!!!")
					nacisnij_enter()		
		elif main_menu == "2":
			petla_pracuje = True
			while petla_pracuje:
				czysc_ekran()
				naglowek(gotowka)
				wybor_zmiany_w_portfelu = input("\nWybierz pozycje z listy:\n(1) Kupno\n(2) Sprzedaż\n(3) Wpłata\n(4) Wypłata\n(5) Historia operacji\n(Q) Powrót do poprzedniego menu\n\nTwój wybór: ")
				if wybor_zmiany_w_portfelu == "1":
					w_budowie()
				elif wybor_zmiany_w_portfelu == "2":
					w_budowie()
				elif wybor_zmiany_w_portfelu == "3":
					w_budowie()
				elif wybor_zmiany_w_portfelu == "4":
					w_budowie()
				elif wybor_zmiany_w_portfelu == "5":
					w_budowie()
				elif wybor_zmiany_w_portfelu == "Q" or wybor_zmiany_w_portfelu == "q":
					petla_pracuje = False
				else:
					print("\nBłędny wybór !!!!!!")
					nacisnij_enter()
		elif main_menu == "Q" or main_menu == "q":
			# zapis do  pliku  stanu gotówki
			print("\nDo zobaczenia !!!!!")
			zatrzymaj_prace_programu_na_sekund(sekundy=3)
			program_pracuje = False
		else:
			print("\nBłędny wybór !!!!!!")
			nacisnij_enter()
			czysc_ekran()
exit()
