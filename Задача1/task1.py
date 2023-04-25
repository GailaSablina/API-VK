import requests

def get_max_intelligency_hero(names):
    # url api
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    # Получаю всех супергероев
    response = requests.get(url)
    # Записываю в data содержимое json со всеми героями
    data = response.json()
    intelligency = 0
    hero_name = ''
    # Цикл по всем героям
    for hero in data:
        # Если герой в списке для сравнения
        if hero['name'] in names:
            # Если интеллект героя больше - переопределяю intelligency и hero_name
            if hero["powerstats"]["intelligence"] > intelligency:
                intelligency = hero["powerstats"]["intelligence"]
                hero_name = hero["name"]
    # Возвращаю героя с максимальным интеллектом
    return f'Самый умный: {hero_name} с интеллектом {intelligency}'


def main():
    names = ['Hulk', 'Captain America', 'Thanos']
    print(get_max_intelligency_hero(names))


if __name__ == '__main__':
    main()
