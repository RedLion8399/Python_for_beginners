from colorama import Fore, Style

print(Fore.RED + "Iteration über Elemente in einer Liste" + Style.RESET_ALL)


# Itterieren über Elemente in einer Liste
names: list[str] = ["Jana", "Hanna", "Max", "Lisa", "Tim"]

for name in names:
    message: str = "Hello, " + name + "!"
    print(message)


print()
print(Fore.RED + "Iteration über eine Range " + Style.RESET_ALL)


# Itterieren über eine Range
for i in range(1, 11):
    print(i * i)


print()
print(Fore.RED + "Überspringen einer Iteration")
print("" + Style.RESET_ALL)


# Iteration überspringen
# Aufzuganzeige ohne 13. Etage
for floor_number in range(1, 16):
    if floor_number == 13:
        continue
    print(f"You are on floor: {floor_number}")

# Bei beendigung wir der else Block ausgeführt
else:
    print("You have reached the top floor.")
