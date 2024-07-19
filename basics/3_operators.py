# Imports nicht releavant für den Kurs
from colorama import Fore, Style


print(Fore.RED + "Arithmetische Operatoren" + Style.RESET_ALL)


# Arithmetische Operatoren
print(3 + 4)  # 7

print(3 - 4)  # -1

print(3 * 4)  # 12

print(3 / 4)  # 0.75

print(3 % 4)  # 3

print(3 ** 4)  # 81

print(3 // 4)  # 0

print()
print(Fore.RED + "Vergleichsoperatoren" + Style.RESET_ALL)


# Vergleichsoperatoren
print(1 == 1)  # True

print(1 != 1)  # False

print(1 > 2)  # False

print(1 < 2)  # True

print(1 >= 2)  # False

print(1 <= 2)  # True


print()
print(Fore.RED + "Logische Operatoren" + Style.RESET_ALL)


# Logische Operatoren
print(True and True)  # True

print(True or True)  # True

print(not True)  # False


print()
print(Fore.RED + "Zuweisungsoperatoren" + Style.RESET_ALL)


# Zuweisungsoperatoren
a = 2

a += 3  # a = a + 3
print(a)

a -= 3  # a = a - 3
print(a)

a *= 3  # a = a * 3
print(a)

a /= 3  # a = a / 3
print(a)

a %= 3  # a = a % 3
print(a)

a **= 3  # a = a ** 3
print(a)

a //= 3  # a = a // 3
print(a)