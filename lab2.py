# Zadanie 1: Hierarchia klas książek
class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
    
    def opis(self):
        return f"{self.tytul} - {self.autor} ({self.rok_wydania})"

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku
    
    def opis(self):
        return f"{super().opis()} - eBook ({self.rozmiar_pliku} MB)"

class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania
    
    def opis(self):
        return f"{super().opis()} - Audiobook ({self.czas_trwania} min)"

# Testowanie
ksiazka1 = Ebook("Python dla każdego", "Mark Lutz", 2021, 5.4)
ksiazka2 = Audiobook("Sztuka wojny", "Sun Tzu", 2019, 180)
print(ksiazka1.opis())
print(ksiazka2.opis())

# Zadanie 2: System logowania
class UserNotFoundError(Exception):
    pass

class WrongPasswordError(Exception):
    pass

class UserAuth:
    def __init__(self, users):
        self.users = users
    
    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError("Użytkownik nie istnieje")
        if self.users[username] != password:
            raise WrongPasswordError("Nieprawidłowe hasło")
        print("Logowanie powiodło się")

# Testowanie
auth = UserAuth({"admin": "1234", "user": "abcd"})
try:
    auth.login("admin", "1234")  # Sukces
except Exception as e:
    print(f"Błąd: {e}")

try:
    auth.login("unknown", "pass")  # Powinien rzucić UserNotFoundError
except Exception as e:
    print(f"Błąd: {e}")

try:
    auth.login("user", "wrongpass")  # Powinien rzucić WrongPasswordError
except Exception as e:
    print(f"Błąd: {e}")
