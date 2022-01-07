from random import *
#from math import trunс

random_number = randint(1, 100)
user_number = 0
print('Добро пожаловать в числовую угадайку!')

#Функция для проверки вводимого числа.??
def is_valid(num):
    if 1 <= user_number <= 100:
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
    elif user_number > random_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif user_number == random_number:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку! Еще увидимся...')