from evidencni_system import Evidencni_System

# Testovací kód
evidencnisystem = Evidencni_System() # Vytváří se instance třídy Evidencni_System s názvem evidencnisystem.


while True: # V cyklu while True se zobrazuje uživatelské rozhraní.
    print("------------------------------------------")
    print("       EVIDENCE POJISTNÝCH UDÁLOSTÍ       ")
    print("------------------------------------------")
    print("\nVyberte si akci:")
    print("1 - Vytvoření pojištěné osoby")
    print("2 - Zobrazení seznamu pojištěných osob")
    print("3 - Vyhledání pojištěných osob")
    print("4 - Konec")

    volba = input("\nZadejte číslo volby: ") # Uživatel si může vybrat akci zadáním čísla volby.

    if volba == "1": # Volba 1 zobrazí otázky pro vytvoření nové pojištěné osoby a volá se metoda vytvoreni_pojisteneho instance evidencnisystem
        jmeno = input("\nZadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = input("Zadejte telefonní číslo: ")
        evidencnisystem.vytvoreni_pojisteneho(jmeno, prijmeni, vek, telefon)
        input("\nPokračujte stisknutím ENTER...")

    elif volba == "2": # Volba 2 zobrazí seznam pojištěných osob pomocí metody zobrazeny_seznam_pojistenych instance evidencnisystem.
        evidencnisystem.zobrazeny_seznam_pojistenych()
        input("\nPokračujte stisknutím ENTER...")

    elif volba == "3": # Volba 3 zobrazí otázky pro vyhledání pojištěné osoby a volá se metoda vyhledani_pojisteneho instance evidencnisystem.
        jmeno = input("\nZadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        evidencnisystem.vyhledani_pojisteneho(jmeno, prijmeni)
        input("\nPokračujte stisknutím ENTER...")

    elif volba == "4": # Volba 4, cyklus se ukončí a program skončí.
        break
    else:
        print("\nNeplatná volba, zadejte číslo 1 až 4: ") # Pokud uživatel zadá neplatnou volbu, vypíše se chybové hlášení


