# Импортирую из файла mytoken переменную TOKEN
from mytokenmytoken  importTOKEN
import requests
import osos

 classYaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        # Получаю название файла
        filename = filename.split('/')[-1]
        # Получаю ссылку для загрузки файла
        href = self.get_link_file_upload(filename)
        # Открываю загружаемый файл
        with open(file_path, 'rb') as file:
            # Загружаю открытый файл методом put
            response = requests.put(url=href, headers=self.headers, files={'file':file})
        # Проверяю статус код
        if response.status_code  ==201:
            print(f'Файл {filename} успешно загружен на Яндекс Диск')
            return 'OK'
        else:
            print(f'Что-то пошло не так. Ошибка {response.status_code}')
            return 'ERROR'

    # Функция получения ссылки для загрузки файла
    def get_link_file_uploadget_link_file_upload(self,filename):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            'path': '{}'.format(filename),
            'overwrite': 'True'}
        response = requests.get(url,headers=self.headers,params=params)
        href = response.json()['href']
        return href


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'task_2/files/1.txt'
    # Беру токен из файла mytoken (файл игнорируется git)
    token = TOKEN
    # Создаю объект класса YaUploader
    uploader = YaUploader(token)
    # Загружаю файл и получаю ответ вида: ОК или ERROR
    result = uploader.upload(path_to_file)
    print(result)

    # Загрузка всех файлов из папки files
    #
    # Путь до папки, где лежат файлы для загрузки
    path_to_files = 'task_2/files/'
    # Создаю список файлов лежащих в папке
    file_list = [path_to_files + file for file in os.listdir(path_to_files) if os.path.isfile(f'{path_to_files}/{file}')]
    # Цикл загрузки файлов на Яндекс Диск
    for file_path in file_list:
        uploader.upload(file_path