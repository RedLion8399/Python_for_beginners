# print
# Gibt einen Text au der Konsole aus
print("Hello, World!")


# input
# Fragt den Benutzer nach einer Eingabe
name = input("What is your name? ")
print("Hello, " + name + "!")


# len
# Gibt die Länge eines Objekts zurück
print(len("Hello, World!"))


# type
# Gibt den Typ eines Objekts aus
print(type(1))
print(type("Hello, World!"))
print(type(True))
print(type(None))


# min und max
# Gibt den kleinsten und den groessten Wert eines Objekts aus
numbers = [1, 2, 3, 4, 5]
print(min(numbers))
print(max(numbers))


# sum
# Gibt die Summe der Elemente eines Objekts aus
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))


# round
# Rundet eine Zahl auf eine bestimmte Anzahl an Nachkommastellen
number = 1.23456789
print(round(number, 2))


# abs
# Gibt den Betrag eines Objekts aus
number = -1
print(abs(number))


# enumerate
# Gibt eine Liste mit Index und Objekt aus
numbers = [1, 2, 3, 4, 5]
for index, number in enumerate(numbers):
    print(index, number)


# zip
# Gibt eine Liste mit Tupeln aus
numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d", "e"]
for number, letter in zip(numbers, letters):
    print(number, letter)


# sorted
# Gibt eine sortierte Liste aus
numbers = [5, 3, 1, 2, 4]
print(sorted(numbers))


# reversed
# Gibt eine umgekehrte Liste aus
numbers = [1, 2, 3, 4, 5]
print(list(reversed(numbers)))


# Beispielhaft
# Konvertieren von Datentypen
number = 1
print(type(number))

number = str(number)
print(type(number))