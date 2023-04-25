from datetime import datetime, timedelta
import requests


class Stackoverflow:

    def get_all_question_by_tag(self, tag, days):
        # Получаю дату days назад
        delta_date = datetime.today() - timedelta(days=days)
        # Привожу дату в unix Epoch time
        delta_date = int(delta_date.timestamp())
        url = 'https://api.stackexchange.com/2.3/questions'
        # Параметры:
        # размер страницы: 100 (максимальное значение)
        # сортировка: по дате создания
        params = {
            'pagesize': '100',
            'fromdate': '{}'.format(delta_date),
            'order': 'desc',
            'sort': 'creation',
            'tagged': '{}'.format(tag),
            'site': 'stackoverflow'
        }
        # Делаю запрос к api
        response = requests.get(url=url, params=params)
        # Проверяю статус код
        if response.status_code == 200:
            data = response.json()
        # Если код ошибки завершаю выполнение функции
        else:
            print(f'ОШИБКА КОД: {response.status_code}')
            return f'ОШИБКА КОД: {response.status_code}'
        # Цикл по постам в data
        for post in data['items']:
            print(f'Название: {post["title"]}')
            print(f"Ссылка: {post['link']}")
            print(f"Дата создания: {datetime.utcfromtimestamp(post['creation_date'])}")
            print('------------------------------')


if __name__ == '__main__':
    # Тэг по которому ищу посты. Можно указать несколько через ; Например 'Python;Ide'
    tag = 'Python'
    # За какое кол-во дней
    days = 2
    # Создаю объект класса Stackoverflow
    parser = Stackoverflow()
    # Получаю все вопросы по тегу за кол-во дней
    parser.get_all_question_by_tag(tag, days)
