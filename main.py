"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bull & Cows

author: Tomáš Beneš
email: tomasbenes21@gmail.com

"""
    
from random import choice, seed, sample
seed(2)

#### Definované funkce #############################

# Funkce pro generování čísel jako list (první číslo nesmí být 0)
def generovani_cisel():
    cisla = list(range(10))
    prvni_cislo = choice(cisla[1:])  # První číslo nesmí být 0
    cisla.remove(prvni_cislo)  # Odstraníme vybranou číslici
    cisla_k_uhadnuti = sample(cisla, 3)  # Vybereme 3 unikátní čísla
    cisla_k_uhadnuti.insert(0, prvni_cislo)  # První číslo přidáme na začátek
    return cisla_k_uhadnuti

# Funkce pro získání vstupu od uživatele (4 unikátní čísla, první nesmí být 0)
def zadani_cislic():
    while True:
        user_input = input("Zadejte 4místný kód (čísla 0-9, bez duplikátů, první nesmí být 0): ")
        if len(user_input) == 4 and user_input.isdigit() and len(set(user_input)) == 4 and user_input[0] != '0':
            return [int(c) for c in user_input] # Převedeme string na list čísel
        else:
            print("Neplatný vstup, zkuste to znovu.")

# Funkce pro vyhodnocení bulls a cows
def vyhodnoceni(vygenerovane, hadane):
    bulls = sum(v == h for v, h in zip(vygenerovane, hadane))  # Správná čísla na správných pozicích
    cows = sum(min(vygenerovane.count(digit), hadane.count(digit)) for digit in set(hadane)) - bulls  # Správná čísla na špatné pozici
    return bulls, cows

#### Beh hry #############################

vygenerovana_cisla = generovani_cisel()  # Vygenerování tajného čísla

cara = '-' * 50
hra_bezi = True

print("Hi there!")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(cara)

# Hlavní smyčka hry
pokusy = 0
while hra_bezi:
    hadana_cisla = zadani_cislic()  # Získání vstupu
    pokusy += 1

    bulls, cows = vyhodnoceni(vygenerovana_cisla, hadana_cisla)
    print(f"{bulls} {'Bull' if bulls == 1 else 'Bulls'}, {cows} {'Cow' if cows == 1 else 'Cows'}")
    print(cara)

    if bulls == 4:
        print(f"Gratuluji! Uhádl jsi číslo {''.join(map(str, vygenerovana_cisla))} za {pokusy} pokusů.")
        hra_bezi = False

    