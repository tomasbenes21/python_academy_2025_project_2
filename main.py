"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls & Cows

Author: Tomáš Beneš
Email: tomasbenes21@gmail.com
"""
from typing import Union
from random import choice, sample

CARA = '-' * 50


# ===================== Definované funkce ===================== #

def generovani_cisel() -> list[int]:
    """
    Vygeneruje 4místné číslo ke hře, bez opakujících se číslic a bez nuly na začátku.
    """
    cisla = list(range(10))
    prvni_cislo = choice(cisla[1:])
    cisla.remove(prvni_cislo)
    dalsi_cisla = sample(cisla, 3)
    dalsi_cisla.insert(0, prvni_cislo)
    return dalsi_cisla


def zadani_cislic() -> Union[list, str]:
    """
    Získá vstup od uživatele a ověří, že odpovídá pravidlům 
    (4 číslice, žádné duplikáty, nezačíná nulou).
    """
    while True:
        user_input = input("Zadejte 4místný kód (čísla 0-9, bez duplikátů, první nesmí být 0): ")
        if (
            len(user_input) == 4
            and user_input.isdigit()
            and len(set(user_input)) == 4
            and user_input[0] != '0'
        ):
            return [int(c) for c in user_input]
        print("Neplatný vstup, zkuste to znovu.")


def vyhodnoceni(vygenerovane: list[int], hadane: list[int]) -> tuple[int, int]:
    """
    Vyhodnotí počet správně uhodnutých číslic na správném místě (bulls)
    a správné číslice na špatném místě (cows).
    """
    bulls = sum(v == h for v, h in zip(vygenerovane, hadane))
    cows = (
        sum(min(vygenerovane.count(d), hadane.count(d)) for d in set(hadane)) - bulls
    )
    return bulls, cows


def uvod() -> None:
    """
    Vypíše úvodní zprávu hry.
    """
    print(f"""
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{CARA}
""")


def hra() -> None:
    """
    Řídí průběh hry.
    """
    vygenerovana_cisla = generovani_cisel()
    pokusy = 0

    while True:
        hadana_cisla = zadani_cislic()
        pokusy += 1

        bulls, cows = vyhodnoceni(vygenerovana_cisla, hadana_cisla)
        print(f"{bulls} {'Bull' if bulls == 1 else 'Bulls'}, "
              f"{cows} {'Cow' if cows == 1 else 'Cows'}")
        print(CARA)

        if bulls == 4:
            print(f"Gratuluji! Uhádl jsi číslo "
                  f"{''.join(map(str, vygenerovana_cisla))} za {pokusy} pokusů.")
            break


def main() -> None:
    """
    Spustí úvod a samotnou hru.
    """
    uvod()
    hra()


# ===================== Spuštění programu ===================== #

if __name__ == "__main__":
    main()
