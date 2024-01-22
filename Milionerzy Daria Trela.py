import random
import time

class Gracz:
    def __init__(self, imie):
        self.imie = imie
        self.aktualna_kwota = 0
        self.udzielone_poprawne_odpowiedzi = set()
        self.czas_gry = 0

class Milionerzy:
    def __init__(self):
        self.mapa_kategorii = {}
        self.wygrane = [0, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
        self.gracz = None

    def powitanie(self):
        print("Witaj w grze 'Milionerzy'!")
        print("Odpowiedz na pytania, aby wygrać milion dolarów.")
        print("Masz do dyspozycji kategorie: Podstawowe i Zaawansowane - dobierz poziom do swoich możliwości :).")

    def wpisz_imie(self):
        while True:
            imie = input("Podaj swoje imię: ")
            if imie.strip():
                self.gracz = Gracz(imie)
                break
            else:
                print("Imię nie może być puste. Spróbuj jeszcze raz.")

    def zainicjuj_pytania(self):
        podstawowe_pytania = {
            "Co jest stolica Polski?": "Warszawa",
            "Ile wynosi 2 + 2?": "4",
            "Kto napisał 'Pan Tadeusz'?": "Adam Mickiewicz",
            "Ile boków ma kwadrat?": "4",
            "Kto był ojcem Ikara?": "Dedal",
            "Firma z jabłkiem w logo?": "Apple",
            "Jak nazywała się córka Demeter": "Kora",
            "Jaki był słaby punkt Achillesa?": "pięta",
            "Ile wynosi liczba PI w przybliżeniu?": "3,14",
            "Co jest stolicą Francji?": "Paryż",
            "Kto był pierwszym królem Polski": "Chrobry",
            "Która planeta jest trzecia od słońca": "Ziemia",
        }

        zaawansowane_pytania = {
            "Ile wynosi pierwiastek kwadratowy z 144?": "12",
            "Kto odkrył promieniowanie X?": "Wilhelm Conrad Roentgen",
            "Który pierwiastek chemiczny oznaczony jest symbolem 'Au'?": "Złoto",
            "Kto był prezydentem Stanów Zjednoczonych w 2020 roku?": "Joe Biden",
            "Które zwierze jest największe na świecie?": "Płetwal błękitny",
            "Co jest stolicą Japonii?": "Tokio",
            "W którym roku odbyły się pierwsze nowożytne Letnie Igrzyska Olimpijskie?": "1896",
            "Jakie zwierze jest symbolem Australii?": "Kangur",
            "Kto jest autorem 'Złodzieja z Bagdadu'?": "Antoine Galland",
        }

        self.mapa_kategorii = {
            "Podstawowe": podstawowe_pytania,
            "Zaawansowane": zaawansowane_pytania
        }

    def gra_milionerow(self):
        self.powitanie()
        while True:
            self.wpisz_imie()
            start_czasu = time.time()
            while True:
                self.zainicjuj_pytania()
                kategorie = list(self.mapa_kategorii.keys())
                print(f"\nWitaj {self.gracz.imie}! Dostępne kategorie:")
                for i, kategoria in enumerate(kategorie, start=1):
                    print(f"{i}. {kategoria}")

                try:
                    wybrana_kategoria_index = int(input("Wybierz numer kategorii: "))
                    wybrana_kategoria = kategorie[wybrana_kategoria_index - 1]
                except (ValueError, IndexError):
                    print("Błędny wybór kategorii. Spróbuj jeszcze raz.")
                    continue

                pytania = self.mapa_kategorii[wybrana_kategoria]
                pytania_keys = list(pytania.keys())
                pytania_keys = [pytanie for pytanie in pytania_keys if pytanie not in self.gracz.udzielone_poprawne_odpowiedzi]
                random.shuffle(pytania_keys)

                for pytanie in pytania_keys:
                    print(f"\nAktualna kwota: ${self.wygrane[self.gracz.aktualna_kwota]}")
                    print(f"Kategoria: {wybrana_kategoria}")
                    print(f"Pytanie za {self.wygrane[self.gracz.aktualna_kwota + 1]}: {pytanie}")

                    odpowiedz = input("Twoja odpowiedź: ").strip()

                    if odpowiedz.lower() == pytania[pytanie].lower():
                        print("Poprawna odpowiedź!\n")
                        self.gracz.aktualna_kwota += 1
                        self.gracz.udzielone_poprawne_odpowiedzi.add(pytanie)
                    else:
                        print(f"Niestety, zła odpowiedź. Koniec gry. Wygrałeś {self.wygrane[self.gracz.aktualna_kwota]}!")
                        break

                    if self.gracz.aktualna_kwota == len(self.wygrane) - 1:
                        print("Gratulacje! Wygrałeś milion dolarów!")
                        break

                koniec_czasu = time.time()
                self.gracz.czas_gry = koniec_czasu - start_czasu

                print("\nStatystyki końcowe:")
                print(f"Imię: {self.gracz.imie}")
                print(f"Aktualna kwota: ${self.wygrane[self.gracz.aktualna_kwota]}")
                print(f"Czas gry: {self.gracz.czas_gry:.2f} sekund")
                print(f"Liczba poprawnych odpowiedzi: {len(self.gracz.udzielone_poprawne_odpowiedzi)}")

                czy_kontynuowac = input("Czy chcesz kontynuować? (tak/nie): ").lower()
                if czy_kontynuowac != 'tak':
                    print("Dziękujemy za grę!")
                    break

if __name__ == "__main__":
    milionerzy = Milionerzy()
    milionerzy.gra_milionerow()
