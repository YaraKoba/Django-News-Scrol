[![](https://img.shields.io/pypi/pyversions/django-admin-interface.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)

# Django-tree-menu
`Stack:` `Python` `Django` `PostgreSQL`
## Все делал самостоятельно, лишь взял скелет Django проекта.
Вся логика описана в комментариях в коде.

Жду с нетерпением обратную связь

### Важные файлы:
1) Шаблон с созданием меню `tree_menu/templates/tree_menu/children.html`
2) Теги, запрос в БД `tree_menu/templatetags/menu_tags.py`
3) Модели: `tree_menu/models.py`


## Show how it works

### Everything that is on the dedicated point is deployed

![sow.gif](media%2Fsow.gif)

### When clicking on the menu, there is a transition at the URL specified in it.

![sow2.gif](media%2Fsow2.gif)

### Is edited in the standard Django admin panel

![admin_panel.gif](media%2Fadmin_panel.gif)

![update.gif](media%2Fupdate.gif)

## Installation

```commandline
git clone git@github.com:YaraKoba/django_tree_menu.git
cd django_tree_menu
python -m venv venv
source venv/bin/activate
```

### Install requirements

```commandline
make install_requirements
```

### Run migrations

```commandline
make migrate
```
### Run createsuperuser

```commandline
make createsuperuser
```

### Run server

```commandline
make runserver
```

## Usage

### Fronted available at

```commandline
http://127.0.0.1:8000/
```

### Admin panel available at

```commandline
http://127.0.0.1:8000/admin
```
