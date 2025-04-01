from typing import List, Dict, Optional, Iterator

# Zadanie 1: Inteligentny asystent językowy (kompozycja)
class Asystent:
    def __init__(self, nazwa: str, wersja: str):
        self.nazwa = nazwa
        self.wersja = wersja

class AnalizaJezykowa:
    def analizuj_zapytanie(self, zapytanie: str) -> str:
        if "pogoda" in zapytanie.lower():
            return "Pogoda"
        elif "czas" in zapytanie.lower():
            return "Czas"
        return "Nieznana intencja"

class GeneratorOdpowiedzi:
    def generuj_odpowiedz(self, analiza: str) -> str:
        odpowiedzi = {
            "Pogoda": "Dziś jest słonecznie!",
            "Czas": "Jest godzina 12:00.",
            "Nieznana intencja": "Nie rozumiem pytania."
        }
        return odpowiedzi.get(analiza, "Nieznana intencja")

class InteligentnyAsystent:
    def __init__(self, nazwa: str, wersja: str):
        self.asystent = Asystent(nazwa, wersja)
        self.analiza = AnalizaJezykowa()
        self.generator = GeneratorOdpowiedzi()

    def odpowiedz_na_zapytanie(self, zapytanie: str) -> str:
        analiza = self.analiza.analizuj_zapytanie(zapytanie)
        return self.generator.generuj_odpowiedz(analiza)

# Testowanie
asystent = InteligentnyAsystent("ChatBot", "1.0")
print(asystent.odpowiedz_na_zapytanie("Jaka jest pogoda?"))
print(asystent.odpowiedz_na_zapytanie("Która godzina?"))

# Zadanie 2: Funkcja average
def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0

# Testowanie
print(average([1.5, 2.5, 3.0]))

# Zadanie 3: Klasa Library
class Library:
    def __init__(self):
        self.books: Dict[str, str] = {}
    
    def add_book(self, isbn: str, title: str):
        self.books[isbn] = title
    
    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)

# Testowanie
library = Library()
library.add_book("978-3-16-148410-0", "Python Programming")
print(library.find_book("978-3-16-148410-0"))
print(library.find_book("123-4-56-789012-3"))

# Zadanie 4: Generator Fibonacciego
def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Testowanie
fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))

# Zadanie 5: Iteracyjny chatbot
class SimpleChatbot:
    def __init__(self, questions: List[str]):
        self.questions = questions
        self.index = 0
    
    def __iter__(self) -> Iterator[str]:
        return self
    
    def __next__(self) -> str:
        if self.index >= len(self.questions):
            raise StopIteration
        question = self.questions[self.index]
        self.index += 1
        return question

# Testowanie
bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
for question in bot:
    print(question)
    input()  # Użytkownik wpisuje odpowiedź
