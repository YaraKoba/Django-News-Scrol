[![](https://img.shields.io/pypi/pyversions/django-admin-interface.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)

# Django NEWS app
`Stack:` `Python` `Django` `PostgreSQL` `js` `django-rest-framework`

Проект состоит из 4 страниц. Все Новости, Страница Поста, Новости по Тегу, Статитстика Новостей.


## Основные фичи

### Бесконечная прокрутка
Установил обработчик событий на скрол и если наша позиция на экране больше чем ширина блока с постами, то подгружаем новые 3 поста.
Этот процесс почти не заметен, но если поставить timeSleep, то видно хорошо.

![infinite-scrol.gif](media%2Finfinite-scrol.gif)

### Возможность ставить Лайк, Дизлайк под новостью
Счетчик лайков/дизлайков всегда возвращает актуальное кол-во, т-к делает запрос на сервер после нажатия на кнопку.
Также есть возможность поменять свое решение или отменить вовсе.

![like.gif](media%2Flike.gif)

### Сортировка по тегам
Модели новости и тега связаны через ManyToMany, это позволяет быстро отфильтровать новости по тегам.
Чем больше тегов выбрать, тем больше совпадений с новостями, следовательно больше результатов.

![tags2.gif](media%2Ftags2.gif)

### Страница статистики
Тут я реализовал диаграмму постов, где можно выбрать разные фильтры для анализа Новостей. 
Доступны фильтры:
1. По кол-ву лайков
2. По кол-ву дизлайков
3. По кол-ву просмотров
Просмотры растут при каждом посещении страницы новости.

![diagram.gif](media%2Fdiagram.gif)

### Джанго админка
Стандартная джанго админка, в которой можно упровлять базой данных.

![admin.gif](media%2Fadmin.gif)

## API
Доступны базовые операции с постами новостей `CRUD`
```commandline
{
    'api overview': 'api/',
    'Read pagination news with search by tags': 'news/?page=<page_num>&tags=<tag1>,<tag2>,<tag3>',
    'Create': '/news/create',
    'Update': '/news/<pk>/update',
    'Delete': '/news/<pk>/delete'
}
```
Так же есть более узко направленные `API`
```commandline
{
    'Read all news with order by filter': 'api/news/statistics/?filter=<filter>',
    'Read all tags': 'api/news/tags',
    'Read one news': 'api/news/<int:pk>/',
    'Update likes or dislike': 'api/news/<int:pk>/change-likes',
}
```

## Установка
Клонируйте мой репозиторий, создайте виртуально окружение и файл `.env`, ниже поля для `.env`
```commandline
NAME_DB = <name postgres db>
USER_DB = <name postgres user db>
PASS_DB = <password postgres db>
```


### Установка зависимостей
Для быстрой настройки проекта рекомендую воспользоваться утилитой `Make`

```commandline
make install_requirements
```

### Запуск миграций

```commandline
make migrate
```
### Создать супер юзера

```commandline
make createsuperuser
```

### Запустить сервер

```commandline
make runserver
```

## Как использовать

### Фронтенд

```commandline
http://127.0.0.1:8000/
```

### Джанго админка

```commandline
http://127.0.0.1:8000/admin
```
### API

```commandline
http://127.0.0.1:8000/api
```

