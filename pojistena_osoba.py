class Pojistena_Osoba: # Třída reprezentuje pojistěnou osobu

    def __init__(self, jmeno, prijmeni, vek, telefon): # Konstruktor __init__ inicializuje atributy jmeno, prijmeni, vek a telefon
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self): # Metoda __str__ definuje reprezentaci instance třídy jako textový řetězec
        return f"{self.jmeno} {self.prijmeni}, věk: {self.vek}, telefon: {self.telefon}"


