import json

# Zadanie 1: System zarządzania aplikacjami mobilnymi
print("Zad1")
class AplikacjaMobilna:
    liczba_pobran = 0
    
    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja
    
    def nowe_pobranie(self):
        AplikacjaMobilna.liczba_pobran += 1
    
    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran
    
    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as f:
            dane = json.load(f)
        return cls(dane["nazwa"], dane["wersja"])

# Przykład użycia
app = AplikacjaMobilna.z_json("app.json")
print(f"Aplikacja: {app.nazwa}, Wersja: {app.wersja}")
app.nowe_pobranie()
print(f"Liczba pobrań: {AplikacjaMobilna.ile_pobran()}")
print()

# Zadanie 2: Klasa Matrix
print("Zad2")
class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def __add__(self, other):
        return Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    
    def __mul__(self, other):
        return Matrix(
            self.a * other.a + self.b * other.c, self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c, self.c * other.b + self.d * other.d
        )
    
    def __str__(self):
        return f"[{self.a}, {self.b};\n {self.c}, {self.d}]"
    
    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"

# Przykład użycia
m1 = Matrix(1, 2, 3, 4)
m2 = Matrix(2, 0, 1, 2)

m3 = m1 + m2
print("m3: ", m3)

m4 = m1 * m2
print("m3: ", m4)
print("m4: ", repr(m4))
print()


# Zadanie 3: Klasa Student
print("Zad3")
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __eq__(self, other):
        return self.score == other.score
    
    def __ne__(self, other):
        return self.score != other.score
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score
    
    def __str__(self):
        return f"Student({self.name}, wynik: {self.score})"

# Przykład użycia
s1 = Student("Ola", 85)
s2 = Student("Marek", 90)

print(s1 < s2)
print(s1 > s2)
print(s1 == s2)
