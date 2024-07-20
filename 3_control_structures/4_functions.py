from colorama import Fore, Style


print(Fore.RED + "Hello world functions" + Style.RESET_ALL)

# Grundlegende Syntax
def hello_world():
    print("Hello, World!")
    print("Hier passiert irgentetwas, das immer wieder verwendet werden kann.")

print("1. Durchlauf")
hello_world()

print("2. durchlauf")
hello_world()


print()
print(Fore.RED + "Funktion mit Parametern" + Style.RESET_ALL)


# Funktion mit Parametern
def greeting(name: str):
    print(f"Hello, {name}!")


greeting("Jana")
greeting("Hanna")
greeting("Max")


print()
print(Fore.RED + "Funktion mit Return" + Style.RESET_ALL)


# Funktion mit Return
def square(number: int) -> int:
    return number * number


print(square(5))
print(square(10))
print(square(15))
