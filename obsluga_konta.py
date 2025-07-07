from funkcje_pomocnicze import nacisnij_enter

gotowka = 0

def sztywne_ustalenie_stanu_gotowki():
    print("\n" + 50 * "*" + "\n" + 50 * "*")
    print("\nMODUŁ SZTYWNEGO USTALENIA STANU GOTÓWKI NA KONCIE:")
    print(50 * "-")
    global gotowka
    gotowka = float(input("\nWpisz kwotę posiadanej gotówki na koncie w PLN: "))
    print(f"\nStan gotówki na koncie został ustawiony na {gotowka} PLN")
    nacisnij_enter("\nNaciśnij ENTER aby powrócić do menu obsługi portfela")
    return gotowka

def wplata(gotowka):
    print("\n" + 50 * "*" + "\n" + 50 * "*")
    print("\nMODUŁ WPŁATY GOTÓWKI NA KONTO:")
    print(50 * "-")
    wplacana_kwota = float(input("\nWpisz kwotę wpłacach środków na konto w PLN: "))
    gotowka += wplacana_kwota
    print(f"\nWpłacono {wplacana_kwota} PLN")
    nacisnij_enter("\nNaciśnij ENTER aby powrócić do menu obsługi portfela")
    return gotowka

def wyplata(gotowka):
    print("\n" + 50 * "*" + "\n" + 50 * "*")
    print("\nMODUŁ WYPŁATY GOTÓWKI Z KONTA:")
    print(50 * "-")
    if gotowka > 0:
        wyplacana_kwota = float(input("\nWpisz kwotę wypłacanych środków z konta w PLN: "))
        if wyplacana_kwota > gotowka:
            print("\nBrak wystarczających środków na koncie !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            nacisnij_enter("\nNaciśnij ENTER aby powrócić do menu obsługi portfela")
            return gotowka
        else:
            gotowka -= wyplacana_kwota
            print(f"\nWypłacono {wyplacana_kwota} PLN")
            nacisnij_enter("\nNaciśnij ENTER aby powrócić do menu obsługi portfela")
            return gotowka
    else:
        print("\nBrak środków na koncie !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        nacisnij_enter("\nNaciśnij ENTER aby powrócić do menu obsługi portfela")
        return gotowka
