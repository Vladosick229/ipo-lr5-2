spis1=input("Введите первую строку:")
spis2=input("Введите вторую строку:")

sort_spis1 = sorted(spis1.lower())
sort_spis2 = sorted(spis2.lower())

if sort_spis1 == sort_spis2:
    print('Списки анаграммы')
else:
    print('Списки не анаграммы')