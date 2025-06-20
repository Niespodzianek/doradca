import pandas
import random
import yfinance

def dopisywanie_danych(dane):
	dane["srednia_K"] = dane.Close.rolling(window = 21, min_periods = 21).mean()
	dane["srednia_D"] = dane.Close.rolling(window = 89, min_periods = 55).mean()
	odchylenie = dane.Close.rolling(window = 21, min_periods = 21).std()
	dane["boll_D"] = dane["Close"] - odchylenie
	dane["boll_G"] = dane["Close"] + odchylenie
	return dane

def analizator(dane):
	# print(dane)
	ostatni_wiersz = len(dane.Close) - 1
	notowanie = dane.iloc[ostatni_wiersz, 3]
	srednia_K = dane.iloc[ostatni_wiersz, 7] 
	srednia_D = dane.iloc[ostatni_wiersz, 8]
	boll_D = dane.iloc[ostatni_wiersz, 9] 
	boll_G = dane.iloc[ostatni_wiersz,10] 
	# print(f"{notowanie:.2f}, {srednia_K:.2f}, {srednia_D:.2f}")
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
			komentarz = "Silny trend spadkowy, mocno przegrzany, mozliwosc korekty"
		elif notowanie > boll_G:
			komentarz = "Trend spadkowy, gleboka korekta, okazja otwarcia krotkiej pozycji"
	else:
		komentarz = "Skrzyzowanie srednich"
	return komentarz

def pozyskanie_danych(nazwa_spolki):
	pozyskane_dane = yfinance.Ticker(nazwa_spolki)
	notowania_spolki = pozyskane_dane.history(period="max")
	return notowania_spolki

def generator_wyniku(nazwa, dane):
    wynik = f"{nazwa} \t- {dane}"
    return wynik

if __name__ == "__main__":
	print("PROGRAM PRACUJE")
	wynik_dzialania_programu = []
	
	# tikery analizowanych spolek
	lista_spolek = ["AAPL", "MSFT", "PLTR", "TSLA", "GOOG", "AMZN", "META", "NVDA", "AMD", "INTC", "SMCI", "QCOM", "ARM", "HPQ", "TSM", "MU", "AVGO", "ASX", "ASML", "FNV", "WPM", "GFI", "AU", "AEM", "KGC", "GDX", "NEM", "GM", "QS", "BA", "LMT", "BAC", "DB", "V", "MA", "ALR.WA", "CBF.WA", "CDR.WA", "MBK.WA", "PKN.WA", "XTB.WA", "ALE.WA", "BDX.WA", "CCC.WA", "DNP.WA", "KGH.WA", "KRU.WA", "KTY.WA", "LPP.WA", "OPL.WA", "PCO.WA", "PKO.WA", "PZU.WA", "SPL.WA", "ZAB.WA", "11B.WA", "ATT.WA", "CPS.WA", "JSW.WA", "PEO.WA", "PGE.WA", "RBW.WA", "SNT.WA", "TPE.WA", "TXT.WA", "BFT.WA", "BHW.WA"]
	 # pozyskanie danych
	for spolka in lista_spolek:
		notowania_surowe = pozyskanie_danych(spolka)
		# print(f"DEBUG: notowania pozyskane z internetu dla spolki {spolka}: {notowania_surowe}")
		# input("Nacisnij ENTER")
		notowania_przeksztalcone = dopisywanie_danych(notowania_surowe)
		# print(f"DEBUG: notowania przeksztalcone do analizy: {notowania_przeksztalcone}")
		# input("Nacisnij ENTER")
		wynik_analizy = analizator(notowania_przeksztalcone)
		wynik_ostateczny = generator_wyniku(spolka, wynik_analizy)
		wynik_dzialania_programu.append(wynik_ostateczny)
	
	for pozycja in wynik_dzialania_programu:
		print(pozycja)

