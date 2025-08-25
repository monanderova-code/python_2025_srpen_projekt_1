from collections import Counter  # nainportovani Counteru

# texty k analyze. Pridan dummy text na hodnotu 0, ktery neni k dispozici uzivatelum.

TEXTS = [
    """Dummy text at index 0 - not to be used for analysis""",
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.""",
]

last_index_texts = len(TEXTS) - 1  # promenna s hodnotou/indexem posledniho textu

# prihlaseni uzivatelu

user_name = input("Uživatelské jméno: ")
user_password = input("Heslo: ")

# prihlasovaci udaje uzivatel aplikace. Zvolen dict pro snadne pridani uzivatelu v budoucnu

user_credentials = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

divider = "----------------------------------------"

# podminka kontrolujici prihlasujici se uzivatele

if user_name in user_credentials and user_credentials[user_name] == user_password:
    print(divider)
    print(
        f"Welcome to the app, {user_name}\nWe have {last_index_texts} texts to be analyzed."
    )
    print(divider)
    
    # zde uzivatel vybira z dostupnych textu

    text_selection = int(
        input(f"Enter a number btw. 1 and {last_index_texts} to select: ")
    )

    if (
        1 <= text_selection < len(TEXTS)
    ):  # podminka na vybrani pouze z dostupnych cisel textu
        selected_text = TEXTS[
            text_selection
        ]  # vytvoreni promenne, se kterou muzeme dale pocitat a rozdelit slova
        words = [
            word.strip(",.") for word in selected_text.split()
        ]  # rozdeleni slov z vybraneho text

        # promenne na pocitani pozadovanych statistik

        word_count = len(words)
        titlecase_count = sum(1 for w in words if w.istitle())
        uppercase_count = sum(1 for w in words if w.isupper() and w.isalpha())
        lowercase_count = sum(1 for w in words if w.islower())
        numeric_strings_count = sum(1 for w in words if w.isdigit())
        numeric_sum = sum(int(w) for w in words if w.isdigit())
        lengths = [len(w) for w in words]
        length_counter = Counter(lengths)  # promenna Counteru na pocitani delek slov

        # print jednotolivych statistik za pouziti vyse nastavenych promennych

        print(divider)
        print(f"There are {word_count} words in the selected text.")
        print(f"There are {titlecase_count} titlecase words.")
        print(f"There are {uppercase_count} uppercase words.")
        print(f"There are {lowercase_count} lowercase words.")
        print(f"There are {numeric_strings_count} numeric strings.")
        print(f"The sum of all the numbers {numeric_sum}")
        print(divider)
        print("LEN|  OCCURRENCES  |NR.")
        print(divider)
        for length in sorted(length_counter):
            count = length_counter[length]
            stars = "*" * count
            print(f"{length:3}|{stars:<18}|{count}")
    else:  # upozoreni po volbe text mimo dostupny rozsah
        print(
            f"selected text number: {text_selection}\ninvalid text number, terminating the program.."
        )
else:  # upozorneni po nespravnem uziv. jmeno nebo hesle
    print(
        f"username:{user_name}\npassword:{user_password}\nunregistered user, terminating the program.."
    )