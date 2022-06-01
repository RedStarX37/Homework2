from colorama import init, Fore, Style

name = 'cucumber'
taste = 'like water'
color_green = True
type_fruit = False
length_cm = 10
radius_cm = float(1.5)
calories = 16

#ради интереса поработал с форматом вывода
#непосредственно переменные, в отношении которых указан тип, подсвечены красным

init()

print('A' + Fore.RED, name + Style.RESET_ALL + ': ')
print(type(name))
print('it tastes', Fore.RED + taste + Style.RESET_ALL)
print(type(taste))
print('it is colored green -' + Fore.RED,  color_green, Style.RESET_ALL)
print(type(color_green))
print('it is a freuit -' + Fore.RED, type_fruit, Style.RESET_ALL)
print(type(type_fruit))
print('it is' + Fore.RED, length_cm, Style.RESET_ALL + 'cm long')
print(type(length_cm))
print('its radius is' + Fore.RED, radius_cm, Style.RESET_ALL + 'cm')
print(type(radius_cm))
print('it contains' + Fore.RED, calories, Style.RESET_ALL + 'calories')
print(type(calories))
print('End')
