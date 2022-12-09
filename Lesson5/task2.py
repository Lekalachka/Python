# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def take_candies(player: str, candies: int):
    max_candies = 28
    if candies < 28:
        max_candies = candies
    n_candies: int = 0
    while True:
        n_candies = int(input(f'игрок {player}, возьмите конфеты (от 1 до {max_candies}): '))
        if 0 < n_candies <= max_candies:
            break
    candies -= n_candies
    print(f'игрок {player} взял {n_candies} конфет')
    if candies == 0:
        print(f'игрок {player} победил!')
    return candies


def game_two_players():
    candies = 121
    print('Правила:\nНа столе лежит 2021 конфета.'
          ' Играют два игрока делая ход друг после друга.\n'
          ' Первый ход определяется жеребьёвкой.\n'
          ' За один ход можно забрать не более чем 28 конфет.')
    player_1 = input('Введите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')

    player = random.choice((player_1, player_2))
    print(f'Первым ходит игрок {player}')
    player_dict = {1: player}
    if player == player_1:
        player_dict[-1] = player_2
    else:
        player_dict[-1] = player_1
    # print(player_dict)
    # print(player_dict.get(1))
    count = 1
    while candies > 0:
        candies = take_candies(player, candies)
        print(f'на столе осталось {candies}')
        count *= -1
        player = player_dict.get(count)


def game_vs_bot():
    candies_total = 121
    max_take = 28
    player_1 = input('\nВведите ваше имя: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
  
    lucky = random.randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nНа кону {candies_total}.')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = random.randint(1,28)
            print(step)
        else:
            step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total} :  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')


def func():
    print('func from candy.py')
    print(__name__)

if __name__ == '__main__':
    user_choise = input(
        'Выберите вариант 1 - два игрока, 2 - игра с ботом, q - для выхода: ')
    if user_choise == '1':
        game_two_players()
    elif user_choise == '2':
        game_vs_bot()
    elif user_choise == 'q':
        exit()
