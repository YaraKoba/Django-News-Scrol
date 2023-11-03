from django.db import models
from django.urls import reverse


# Эта модель для разных групп меню, например: Главное меню, Боковое меню и тд...
class MenuGroup(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'


# Модель для компонентов меню и их предков
class MenuItem(models.Model):
    text = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55, unique=True, db_index=True, verbose_name='URL')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    group = models.ForeignKey(MenuGroup, related_name='menuitem', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}, {self.group}'

    # Метод возвращает всех детей компонента
    def get_children(self):
        return ", ".join([child.text for child in self.children.all()])

    get_children.short_description = "Children"

    class Meta:
        verbose_name_plural = "Menu Items"

    # Возвращает слаг для компонента, он состоит из двух частей 1. группа, 2. компонент
    def get_url(self):
        return reverse('menu', kwargs={'menu_item_slug': self.slug})
