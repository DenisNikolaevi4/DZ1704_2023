# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. 
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12
# word = input("Введите слово: ")
# i = 0
# summa = 0 
# while i in range(len(word)):
#     if word[i] == 'А'or 'В'or 'Е'or 'И'or 'H'or 'О'or 'Р'or 'С'or 'Т':
#         summa+=1
#     elif word[i] == 'D'or'G':
#         summa+=2
#     elif word[i] == 'B'or'C'or 'M'or 'P':
#         summa+=3
#     elif word[i] == 'F'or 'H'or 'V'or 'W'or 'Y':
#         summa+=4
#     elif word[i] == 'K':
#         summa+=5
#     elif word[i] == 
word =input("Введите слово: ")
word = word.upper()
sum = 0
dictionary1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т' ]
dictionary2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
dictionary3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
dictionary4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
dictionary5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
dictionary8 = ['J', 'X', 'Ш', 'Э', 'Ю']
dictionary10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
for i in range(len(word)):
    if word[i] in dictionary1:
        sum = sum + 1
    elif word[i] in dictionary2:
        sum = sum + 2
    elif word[i] in dictionary3:
        sum = sum + 3
    elif word[i] in dictionary4:
        sum = sum + 4
    elif word[i] in dictionary5:
        sum = sum + 5
    elif word[i] in dictionary8:
        sum = sum + 8
    elif word[i] in dictionary10:
        sum = sum + 10
print(sum)



