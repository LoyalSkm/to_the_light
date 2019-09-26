from game_mechanism import Player, read_json, Monster, Action, LevelUp
from random import choice, randint
import sys


def game():
    player = input("Привет странник, как тебя звать? ")
    print(Player.reg(player))  # Проверка регистрации/регистрация игрока
    while True:
        monster = Monster.choice_monster(player, 'heroes')  # Выбор монстра по уровню игрока
        Monster.have_som_monster(monster)  # Проверка на то, есть ли противник подходящий по уровню
        monster_HP = monster[1]['HP']  # Здоровье монстра
        const_monster_HP = monster_HP  # Не изменяемое значение здоровтя монстра
        player_HP = read_json('heroes')[player]['HP']  # Здоровье Игрока
        const_player_HP = player_HP  # Не изменяемое значение здоровтя игрока
        go = Action.your_choice(monster)  # Выбор монстра по уровню Игрока
        if go == "убить":
            print('{:^70}'.format(f'{player} {player_HP}HP VS {monster[0]} {monster_HP}HP'))
        while True:
            if go == "убить":
                participants = choice([monster, player])  # Рандомный выбор игрока либо монстра для получения урона
                if monster_HP <= 0:  # Победа!!!
                    print(f'''
                    Ура, вы убили {monster[0]}''')
                    print(LevelUp.stat_up(player))
                    break
                if player_HP <= 0:  # О НЕТ!!!
                    print(f'''
                    {monster[0]} оказался сильнее. Тебе пришлось отступить!!''')
                    break
                elif (participants == monster) and (monster_HP < const_monster_HP*0.35):  # Увеличенный шанс выпадения hill для этого условия 3/4
                    act = Action.critical_action()
                    print('{:^100}'.format('Монстр в ярости, регенерация увеличенна!'))
                else:
                    act = Action.normal_action()  # Шансовое выпадание low, high, hill 1/3
                if participants == monster:  # Урон монстру
                    if act == 'low':
                        dem = randint(15, 25)
                        monster_HP -= dem
                        print('{:>100}'.format(f'ВЫ нанесли меленький урон {dem} у монстра осталось {monster_HP} НР >>>'))
                    elif act == 'high':
                        dem = randint(10, 35)
                        monster_HP -= dem
                        print('{:>100}'.format(f'ВЫ нанесли большой урон {dem} у монстра осталось {monster_HP} НР >>>'))
                    elif act == "heal":
                        dem = randint(15, 25)
                        monster_HP += dem
                        if monster_HP >= const_monster_HP:  # Проверка на случай если регенерация выйдет за рамки заданного HP
                            monster_HP = const_monster_HP
                        print('{:>100}'.format(f'МОНСТР востановил {dem}, у монстра стало {monster_HP} НР >>>'))
                if participants == player:  # Урон игроку
                    if act == 'low':
                        dem = randint(15, 25)
                        player_HP -= dem
                        print(f"<<< МОНСТР нанес меленький урон {dem} у вас осталось {player_HP} НР")
                    elif act == 'high':
                        dem = randint(10, 35)
                        player_HP -= dem
                        print(f"<<< МОНСТР нанес большой урон {dem}  у вас осталось {player_HP} НР")
                    elif act == "heal":
                        dem = randint(15, 25)
                        player_HP += dem
                        if player_HP >= const_player_HP:
                            player_HP = const_player_HP
                        print(f"<<< ВЫ востановил {dem}, у вас осталось {player_HP} НР")

            if go == "бежать":
                print(f"{player} убежал сверкая пятками... ")
                sys.exit(0)

game()
