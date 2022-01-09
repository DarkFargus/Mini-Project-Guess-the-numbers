from random import *

user_number = 0
attempts = 0

print('Добро пожаловать в числовую угадайку!')
print('Суть игры - угадать целое число от 1 до "n", которое загадала программа.')
print('Введите правую границу, для случайного выбора числа - "n"')

right_border = int(input())
random_number = randint(1, right_border)

#Функция для проверки вводимого числа.
def is_valid(num):
    if 1 <= user_number <= right_border:
        return True
    else:
        return False

while user_number != random_number:
    user_number = int(input())
    if is_valid(user_number) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    elif user_number < random_number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        attempts += 1
    elif user_number > random_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
        attempts += 1
    elif user_number == random_number:
        print('Вы угадали, поздравляем!')
        print('Количество попыток -', attempts)
        print('Спасибо, что играли в числовую угадайку! Еще увидимся...')
        print('Введите правую границу, для случайного выбора числа - "n", чтобы начать новую игру.')
        right_border = int(input())
        random_number = randint(1, right_border)
        attempts = 0
        continue