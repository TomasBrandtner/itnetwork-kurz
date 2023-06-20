from pojistena_osoba import Pojistena_Osoba

class Evidencni_System: # Třída reprezentuje evidenční systém pro pojištěné osoby

    def __init__(self): # Konstruktor __init__ inicializuje prázdný seznam pojisteni, který slouží k ukládání instance třídy Pojistena_Osoba
        self.pojisteni = []

    def vytvoreni_pojisteneho(self, jmeno, prijmeni, vek, telefon): # Metoda vytvoreni_pojisteneho vytváří novou instanci třídy Pojistena_Osoba a přidává ji do seznamu pojisteni
        pojisteny = Pojistena_Osoba(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)
        print("\nPojištěná osoba úspěšně vytvořena")

    def zobrazeny_seznam_pojistenych(self): # Metoda zobrazeny_seznam_pojistenych zobrazuje seznam všech pojištěných osob uložených v seznamu pojisteni
        if not self.pojisteni:
            print("\nNeexistuje žádná pojištěná osoba")
        else:
            print("\nSeznam pojištěných osob:")
            for pojisteny in self.pojisteni:
                print(pojisteny)

    def vyhledani_pojisteneho(self, jmeno, prijmeni): # Metoda vyhledani_pojisteneho vyhledává pojištěnou osobu podle zadaného jména a příjmení a vypisuje její informace, pokud je nalezena
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print("\nPojištěná osoba nalezena:")
                print(pojisteny)
                return
        print("\nPojištěná osoba nenalezena")
