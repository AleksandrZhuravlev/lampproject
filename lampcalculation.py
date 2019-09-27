## Project 1. Расчет характериситик лампочки.
#Задача: Из введенной мощности лампочки в ваттах расчитать 1.Мощность света 2.Цвет 3.время работы лампочки
# 4.стоимость оного часа работы лампочки

import math as m
power=int(input('Веедите мощность лампочки в Ваттах:'))
lightpower=0.15*power**0.9
wavelength= 0.00750588*power*0.85
durabilitytime=10**3*m.e**(-50/power)
costperhour=power/1000*2.68

print('Мощность испускаемого света:',lightpower)
print('Продолжительность работы:',durabilitytime)
print('Цена электроэнергии за час работы лампочки:',costperhour,'рублей')
if wavelength < 0.3:
    print("\033[1;36;40m Ультрафиолетовый        ")
if 0.3<=wavelength<0.4:
    print("\033[1;35;40m Фиолетовый         ")
if 0.4<=wavelength<0.5:
    print("\033[1;34;40m Синий         ")
if 0.5<=wavelength<0.6:
    print("\033[1;32;40m Зеленый         ")
if 0.6<=wavelength<0.65:
    print("\033[1;33;40m Желтый         ")
if 0.65<=wavelength<0.8:
    print('\033[1;31;40m Красный     ')
if wavelength>0.81:
    print("\033[1;31;40m Инфракрасный        ")
