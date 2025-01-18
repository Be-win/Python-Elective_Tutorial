binary = input("Enter a binary number: ")

decimal = 0
power = 0

for char in binary[::-1]:
    decimal += int(char) * 2 ** power
    power += 1

print("Decimal:", decimal)