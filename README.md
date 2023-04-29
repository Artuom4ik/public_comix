# public_comix
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

___
#### Это программа которая отправляет в группу во Вкантакте любой комикс вместе с комментарием к нему.
___
### Содержание:
* [Требования]()
* [Как пользоваться программой]()
* [Пример использования]()
* [Переменные окружения]()
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
* Для запуска программы требуется указать [переменные окружения]():
    * В корневой папке программы создайте файл ```.env```
    * В созданном файле запишите нужные [переменные окружения]().
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
### Если не занете как получить TOKEN или ID группы:
* [Инструкция](https://vk.com/dev/implicit_flow_user) для получения токена во Вкантакте.
* Сайт для получения [id](https://regvk.com/id/) группы.
___
### Пример работы скрипта:
___
### Цель проекта:
* Код написан в образовательных целях.

