from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
    """Модель для хранения данных о содержимом блога"""
    STATUS_CHOICES = (  # Список из которого можно выбрать вариант, обозначается вначале класса
        ('status_draft', 'Черновик'),
        ('status_published', 'Опубликовано'),
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок сататьи'  # Максимальная длинна поля и
                             # человекопонятное наименование поля в административном сайте
                             )
    slug = models.SlugField(max_length=250, verbose_name='Слаг',  # slug набор символов для формирования urls
                            unique_for_date='publish', # Уникальное поле в разрезе даты создания.
                            # "publish"-указываем как строку, а не как переменную т.к. данная переменная будет объявлена
                            # ниже данного поля которое на нее ссылается.
                            )
    author = models.ForeignKey(User,  # Объявляем как переменную(класс) который импортируем вначале, данный класс
                               # отвечает за авторизацию пользователей в блоге(на сайте) данное поле является
                               # "ключевым", т.к. создает связь
                               # между пользователями и записями блога
                               on_delete=models.CASCADE,  # Обязательно в данном случае. Обозначает метод удаления
                               # записи данного автора при удалении самого автораю CASCADE- при удалении автора,
                               # удалять все его записи
                               related_name='blog_posts'  # Имя обратной связи от User к Post для получения доступак
                               # связанным объектам автора
                               )
    body = models.TextField(verbose_name='Содержание статьи')
    publish = models.DateTimeField(default=timezone.now)  # Дата публикации- обновляемая
    created = models.DateTimeField(auto_now_add=True)  # Дата создания- неизменяемая
    updated = models.DateTimeField(auto_now=True)  # Дата обновления- обновляемая
    status = models.CharField(max_length=25,
                              choices=STATUS_CHOICES,  # Предоставляем выбор из списка
                              default='draft')  # значение по умолчанию

    class Meta:
        """Позволяет изменить метаданные родительского класса возможно указать сортировку, названия и тп"""
        ordering = ('-publish',)  # Сортировка по дате- свежая в самом верху
        verbose_name = 'Статью'  # Человекопонятное название на админ сайте в единственном числе
        verbose_name_plural = 'Статьи'  # Человекопонятное название на админ сайте во множественном числе

    def __str__(self):
        """Строковое представление модели понятное человеку, например на админг сайте"""
        return self.title  # Выводим заголовок в строковом формате
