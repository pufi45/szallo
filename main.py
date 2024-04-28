from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Absztrakt Szoba osztály
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def get_ar(self):
        """Visszaadja a szoba árát."""
        pass

class EgyagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

class KetagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_hozzaad(self, szoba):
        """Hozzáad egy szobát a szálloda szobalistájához."""
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = {}

    def foglal(self, szobaszam, datum):
        """Szoba foglalása adott dátumra, ha az szabad."""
        if datum < datetime.now().date():
            return "A foglalás dátuma nem lehet múltbeli."
        if (szobaszam, datum) in self.foglalasok:
            return "Ez a szoba ezen a napon már foglalt."
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok[(szobaszam, datum)] = szoba
                return f"Foglalás sikeres. Ár: {szoba.get_ar()} Ft"
        return "Nem létező szobaszám."

    def lemondas(self, szobaszam, datum):
        """Foglalás lemondása adott szobához és dátumhoz."""
        if (szobaszam, datum) in self.foglalasok:
            del self.foglalasok[(szobaszam, datum)]
            return "Lemondás sikeres."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        """Összes foglalás listázása."""
        if not self.foglalasok:
            return "Nincsenek foglalások."
        return '\n'.join([f"Szobaszám: {key[0]}, Dátum: {key[1]}" for key in self.foglalasok])

szalloda = Szalloda("Remélem Működik Szálló")
szalloda.szoba_hozzaad(EgyagyasSzoba(50000, 101))
szalloda.szoba_hozzaad(KetagyasSzoba(70000, 102))
szalloda.szoba_hozzaad(KetagyasSzoba(80000, 103))

foglalas_kezelo = Foglalas(szalloda)
foglalas_kezelo.foglal(101, datetime.now().date() + timedelta(days=10))
foglalas_kezelo.foglal(103, datetime.now().date() + timedelta(days=20))
foglalas_kezelo.foglal(101, datetime.now().date() + timedelta(days=25))
foglalas_kezelo.foglal(102, datetime.now().date() + timedelta(days=30))


def proba():
    while True:
        print("\nVálasszon az alábbi műveletek közül:")
        print("1 - Szoba foglalása")
        print("2 - Foglalás lemondása")
        print("3 - Foglalások listázása")
        print("4 - Kilépés")
        valasztas = input("Kérem adja meg a választását: ")

        if valasztas == "1":
            szobaszam = int(input("Adja meg a szobaszámot (101, 102 vagy 103): "))
            datum = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás dátum!")
                continue
            eredmeny = foglalas_kezelo.foglal(szobaszam, datum)
            print(eredmeny)

        elif valasztas == "2":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            datum = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás dátum!")
                continue
            eredmeny = foglalas_kezelo.lemondas(szobaszam, datum)
            print(eredmeny)

        elif valasztas == "3":
            print(foglalas_kezelo.foglalasok_listazasa())

        elif valasztas == "4":
            print("Kilépés a programból.")
            break
        else:
            print("Érvénytelen választás, próbálja újra.")

proba()