from django import template
from tree_menu.models import *

register = template.Library()


# Шаблон для получения группы меню из url
@register.simple_tag
def starts_with(path, value):
    return path.startswith(value)


# Шаблон для отображения древовидного меню
@register.inclusion_tag('tree_menu/nav_bar.html')
def draw_menu(menu, request):
    # ОДИН запрос в БД
    menu_items = MenuItem.objects.filter(group__name=menu)

    # В этой функции находим детей каждого компонента и определяем какой пункт активный учитывая текущий url
    dict_children = render_menu_items(menu_items, request.path)

    return {'item': dict_children, 'menu': menu}


def render_menu_items(menu_items, path):
    menu_tree = []
    menu_dict = {}

    # Перебираем все компоненты меню
    for item in menu_items:
        name = item.text
        url = item.slug
        parent = item.parent
        # Вписываем в словарь значения
        menu_item = {
            'name': name,
            'url': url,
            'is_active': False,
            'href': item.get_url(),
            'current': False,
            'children': [],
        }
        # Если текущий путь равен компоненту, сделать его активным
        if path == menu_item['href']:
            menu_item['current'] = True
            menu_item['is_active'] = True

        # Записываем в словарь по названию компонента
        menu_dict[name] = menu_item

        # Если у компонента нет родителя записываем его в итоговый лист
        if parent is None:
            menu_tree.append(menu_item)

    # Добавляем родителям их детей
    for item in menu_items:
        name = item.text
        if item.parent:
            parent = item.parent
        else:
            parent = None
        if parent is not None:
            parent_item = menu_dict[parent.text]
            if menu_dict[name]['is_active']:

                # Бежим по предкам и ставим отметку, что они активны
                # Это нужно, чтобы все предки отображались развернутыми.
                while parent:
                    menu_dict[parent.text]['is_active'] = True
                    parent = parent.parent

            parent_item['children'].append(menu_dict[name])

    return menu_tree
