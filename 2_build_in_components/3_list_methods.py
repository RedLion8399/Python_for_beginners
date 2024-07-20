# append
# Fügt ein Objekt am Ende einer Liste hinzu
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)


# extend
# Fügt eine Liste am Ende einer Liste hinzu
numbers = [1, 2, 3, 4, 5]
numbers.extend([6, 7, 8, 9, 10])
print(numbers)


# insert
# Fügt ein Objekt an einer bestimmten Position in eine Liste ein
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 6)
print(numbers)


# remove
# Entfernt das erste passende Objekt in einer Liste
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)


# pop
# Entfernt das letzte Objekt in einer Liste und gibt es zurück
# Alternativ kann ein Index angegeben werden
numbers = [1, 2, 3, 4, 5]
last_number = numbers.pop()
print(numbers)
print(last_number)


# clear
# Leert eine Liste
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)


# index
# Gibt den Index eines Objekts in einer Liste aus
numbers = [1, 2, 3, 4, 5]
index = numbers.index(3)
print(index)


# count
# Gibt die Anzahl von spezifischen Objekten in einer Liste aus
numbers = [1, 2, 3, 4, 5, 3, 3]
count = numbers.count(3)
print(count)


# sort
# Sortiert eine Liste
numbers = [5, 3, 1, 2, 4]
numbers.sort()
print(numbers)
