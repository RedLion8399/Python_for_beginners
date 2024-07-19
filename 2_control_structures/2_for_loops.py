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