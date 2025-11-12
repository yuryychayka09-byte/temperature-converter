def celsius_to_fahrenheit(celsius):
    """Конвертує Цельсій у Фаренгейт"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Конвертує Фаренгейт у Цельсій"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Конвертує Цельсій у Кельвін"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Конвертує Кельвін у Цельсій"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Конвертує Фаренгейт у Кельвін"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

print("=== Конвертер температур ===")
print("1. Цельсій -> Фаренгейт")
print("2. Фаренгейт -> Цельсій")
print("3. Цельсій -> Кельвін")
print("4. Кельвін -> Цельсій")
print("5. Фаренгейт -> Кельвін")

choice = input("\nВиберіть операцію (1-5): ")
# Temperature Converter v1.1
try:
    temp = float(input("Введіть температуру: "))

    if choice == '1':
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == '2':
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == '3':
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C = {result:.2f}K")
    elif choice == '4':
        result = kelvin_to_celsius(temp)
        print(f"{temp}K = {result:.2f}°C")
    elif choice == '5':
        result = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F = {result:.2f}K")
    else:
        print("Невірний вибір!")

except ValueError:
    print("Помилка: введіть коректне число!")
