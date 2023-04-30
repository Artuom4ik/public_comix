# Public_comix
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

___
#### Это программа которая отправляет в группу во Вкантакте любой комикс вместе с комментарием к нему.
___
### Содержание:
* [Требования](https://github.com/Artuom4ik/public_comix#%D0%B4%D0%BB%D1%8F-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B0-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D1%82%D1%80%D0%B5%D0%B1%D1%83%D0%B5%D1%82%D1%81%D1%8F)
* [Как пользоваться программой](https://github.com/Artuom4ik/public_comix#%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BE%D0%B9)
* [Пример использования](https://github.com/Artuom4ik/public_comix#%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B0)
* [Переменные окружения](https://github.com/Artuom4ik/public_comix#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
___
### Для запуска программы требуется:
 * Скачать [Python](https://www.python.org/) версии 3.1 или выше.
 * Операционная система macOS, linux, windows 7 или выше.
 * установить все нужные библиотеки Python командой:
```
pip install -r requirements.txt
```
___
### Как пользоваться программой:
* Для запуска программы требуется указать [переменные окружения](https://github.com/Artuom4ik/public_comix#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F):
    * В корневой папке программы создайте файл ```.env```
    * В созданном файле запишите нужные [переменные окружения](https://github.com/Artuom4ik/public_comix#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F).
* В консоль прописываем команду для запуска программы:
```
python main.py
```
___
### Переменные окружения:
* VK_TOKEN - токен который вы получите при предоставлении доступа своей группе.
* VK_GROUP_ID - ```id``` вашей группы во Вкантакте.
* VK_CLIENT_ID - ```id``` клиент вашего приложения.
___
### Если не знаете как получить TOKEN или ID группы:
* [Инструкция](https://vk.com/dev/implicit_flow_user) для получения токена во Вкантакте:
    * Убрать параметр `redirect_uri` у запроса на ключ
    * Параметр `scope` указать через запятую, вот так: `scope=photos, groups`
    * В ответ вы получите ссылку, в ней требуется найти строку `access_token` - это и есть ваш `token`.
* [Сайт](https://regvk.com/id/) для получения `id` группы.
___
### Пример работы скрипта:
![image](image/Снимок.png)
___
### Цель проекта:
* Код написан в образовательных целях.

