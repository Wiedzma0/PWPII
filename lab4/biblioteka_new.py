class Ksiazka:
    def __init__(self, tytul: str, autor: str, dostepna: bool = True) -> None:
        self.tytul = tytul  # Poprawiona wielkość liter
        self.autor = autor
        self.dostepna = dostepna


class Biblioteka:
    def __init__(self) -> None:
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka: Ksiazka) -> None:
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul: str) -> str:
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:  # Poprawiona wielkość liter
                if ksiazka.dostepna:
                    ksiazka.dostepna = False
                    return f"Wypozyczono: {tytul}"
                return f"Ksiazka {tytul} niedostepna"
        return f"Brak ksiazki: {tytul}"

    def zwroc_ksiazke(self, tytul: str) -> str:
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:  # Poprawiona wielkość liter
                ksiazka.dostepna = True
                return f"Zwrocono: {tytul}"
        return f"Nie nalezy do biblioteki: {tytul}"

    def dostepne_ksiazki(self) -> list[str]:
        return [ksiazka.tytul for ksiazka in self.lista_ksiazek if ksiazka.dostepna]


def main() -> None:
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedzmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostepne ksiazki:", biblioteka.dostepne_ksiazki())


if __name__ == "__main__":
    main()
