'''ПЕРВАЯ КОНСТРУКЦИЯ'''
# try:
f = open('example.txt', 'r')  # открыть файл из рабочей директории , encoding = "utf-8"
# print(f.read(7)) # читает 7 символов
# print(f.read(7))
# print(f.readline(3))
# print(f.readlines())
# try:
#     print(*f) # со звездой обращаемся к содержимому файла
#     print(f)
# finally:
f.close()  # закрытие файла, сделать сразу после открытия

''' ВТОРАЯ- БОЛЕЕ ЛУЧШАЯ. ЗДЕСЬ ВШИТЫ ВСЕ ИСКЛЮЧЕНИЯ'''

'''В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел. 
'''
# a = open('examp.txt','r')
# a1 = str(a)
# print()
# s = 0
# for i in a1:
#     if i.isdigit():
#         i = int(i)
#         s += i
# print(f'Сумма всех цифр в файле составляет:{s}')
# a.close()

""" Файл содержит числа и буквы. Каждый записан в отдельной строке. 
Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию, 
а потом слова по возрастанию их длины.   
"""
# try:
#     with open('task3.txt','w', encoding='utf-8') as d:
#         d.write('Каждый записан \n  8,4,1,2,2,6 \n чтобы сначала шли \n 0 8 9 4 2 6 \n 452678 \n')
# except FileNotFoundError:
#     print('File could not be open')


# num = []
# word = []
# d = open('task3.txt', 'r', encoding='utf-8')
#
# for i in d:  # сделал код с цифрами , отсортировал, работает. Начал со словами
#     for j in i:
#         if j.isdigit():
#             j = int(j)
#             num.append(j)
#
#         elif not j.isdigit():
#             word.append(j)
#
# word1 = ''.join(word)
# ls_word = word1.split(' ')
# ln_word = []
# for i in range(len(ls_word)):
#     if ls_word[i].isalpha():
#         ls_word[i] = str(ls_word[i])
#         ln_word.append(ls_word[i])
# ln_word.sort(key=len)
#
# num.sort()
#
# print(num + ln_word)
#
#
# d.close()


''' Создать текстовый файл, записать в него построчно данные,
 которые вводит пользователь. Окончанием ввода пусть служит пустая строка.'''
# try:
#     with open('newf.txt', 'w') as f:
#         try:
#             while True:
#                 a = input()
#                 print(a, file=f) # ввод данных построчно
#                 # f.writelines(a)
#                 if a == '':  #завершение ввода пустая строка
#                     break
#         finally:
#             f.close()
# except:
#     print('Файл невозможно открыть')

''' В текстовом файле посчитать количество строк, 
а также для каждой отдельной строки определить количество в ней символов.
'''

# try:
#     with open('newf.txt', 'r') as d:
#         n = []
#         m = []
#         for i in d:
#             i = list(i)
#             n.append(i)
#             for j in i:
#                 m.append(j)
#
#         print(n, len(n),m,len(m) )
# except:
#     print('Ошибка файла')


# try:
#     with open('newf.txt', 'r+') as z:
#         print(*z, type(z))
#
# except:
#     print('Ошибка файла')

# with open('example.txt') as f:
# a = open('examp.txt','w')
# a.write('Hello \n world')

# print(a.readlines())


"""
списки
индексы и срезы
методы 
картежи
"""

'''В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел. 
'''
