from django.contrib import admin

from blog.models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)  # список полей на экране
    list_editable = ('status',)
    list_filter = ('status', 'created', 'publish', 'author',)  # фильтр
    search_fields = ('title', 'body',)  # поиск
    prepopulated_fields = {'slug': ('title',)}  # Для формирования slug автоматически из  title
    raw_id_fields = ('author',)  # выбор автора по id
    date_hierarchy = 'publish'  # иерархия вывода
    ordering = ('status', 'publish')  # сортировка

