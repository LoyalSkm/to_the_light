import json
from random import choice
import numpy as np
import sys


def read_json(file):
    return json.load(open(f'{file}.json'))


def write_json(person_dict, file):
    json.dump(person_dict, open(f'{file}.json', 'w'), ensure_ascii=False, indent=6)


class Player:  # Регистрация игрока/проверка наличия игрока в списках играков
    @staticmethod
    def reg(name):
        player = read_json("heroes")
        keys_all = player.keys()
        keys_main = name
        if name in keys_all: # Проверка того зарегистрированный ли игрок
            return f'о, привет {name}, круть, мы тебя ждали'
        else:
            player[keys_main] = {   # Регистрация игрока в heroes.json
                'HP': 120,
                'Level': 1,
                'kills': 0
            }
            write_json(player, "heroes")
            return f'{name} ты в игре!'


class Monster:  # Монстр будит выбиратся из списка монстров и выдаватся игроку для битвы

    @staticmethod
    def choice_monster(name, person):
        monster = read_json('monsters')
        player = read_json(person)
        matching_monsters = []  # Список монстров
        try:
            for i in monster.keys():  # Выбераем монстров соответствующего уровню икрока
                if monster[i]['Level'] == player[name]['Level']:
                    matching_monsters.append(i)
            monster_name = choice(matching_monsters)
            return [monster_name, monster[monster_name]]
        except IndexError:
            return False
    @staticmethod
    def have_som_monster(monster):  # Проверка на то, есть ли подходящий по уровню монстр
        if monster == False:
            print("Вы перебили всех существующих монстров*(")
            sys.exit(0)



class Action:  # Наносимый урон или регенерируем здоровья

    @staticmethod
    def normal_action():
        act = np.random.choice(['low', 'high', 'heal'], p=[1/3, 1/3, 1/3])  # Выпадение урона или хила с шансом 1/3
        return act
    @staticmethod
    def critical_action():
        act = np.random.choice(['low', 'high', 'heal'], p=[0.5/4, 0.5/4, 3/4])  # увеличенный шанс выпадения хила
        return act
    @staticmethod
    def your_choice(monster):
        go = ''
        action_list = ['бежать', 'убить']
        while go not in action_list:  # Проверка правильности ввода
            go = input(f'''
                    У тебя на пути стоит {monster[0]} {monster[1]['Level']} уровня.
                    Cтрашно, но что делать? бежать/убить :
                                    ''').lower().strip()
            if go in action_list:  # Если go в списке, то проверка удачная и цыкл прекращается
                break
            else:
                print('''
    Напишите либо \"бежать\" либо \"убить\"''')
        return go


class LevelUp:  # Повышение статистики Игрока
    @staticmethod
    def stat_up(name):
        player = read_json("heroes")
        player[name]["kills"] += 1
        if player[name]["kills"] % 2 == 0:  # Если число убийств кратно 2м то идет увеличение уровня
            player[name]["Level"] += 1
            player[name]["HP"] += 50
            write_json(player, "heroes")
            return f" !!!!Урааа {name} ты крут, теперь ты {player[name]['Level']} уровня!!!"
        write_json(player, "heroes")

