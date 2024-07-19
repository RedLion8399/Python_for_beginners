from colorama import Fore, Style


print(Fore.RED + "Endlosschheile" + Style.RESET_ALL)

# Endlosschleife
while True:
    user_input = input("GIb etwas ein: ")
    print(f"Du hast {user_input} eingegeben.")

    # Abbruchbedingung (aktueell irrelevant)
    if user_input == "break":
        break


print()
print(Fore.RED + "While-Schleife mit Abbruchbedingung" + Style.RESET_ALL)


# While-loop mit Abbruchbedingung im Schleifenkopf
zahl = 0
while zahl < 100:
    print(f"Zahl: {zahl}")
    user_input = int(input("Gib eine Zahl ein: "))
    zahl += user_input


print()
print(Fore.RED + "While-Schleife mit break" + Style.RESET_ALL)


# While-loop mit break als Abbruchbedingung
while True:
    user_input = input("Gib etwas ein: ")
    if user_input == "break":
        break
    print(f"Du hast {user_input} eingegeben.")


print()
print(Fore.RED + "While-Schleife mit continue" + Style.RESET_ALL)


# While-loop mit Überspringen eimes Schleifendurchgangs
while True:
    user_input = input("Gib deinen Namen ein: ")
    if user_input == "break":
        break
    if len(user_input) < 3:
        print(f"{user_input} ist kein gültiger Name.")
        print("Du musst mindestens 3 Zeichen angeben.")
        continue

    # Hier passiert irgentetwas
    print("Hier passiert irgentetwas mir dem Namen")