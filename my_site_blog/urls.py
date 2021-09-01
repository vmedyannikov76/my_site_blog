"""my_site_blog URL Configuration

Список urlpatterns направляет URL-адреса в представления. Для получения дополнительной информации см .:
    https: docs.djangoproject.comen3.2topicshttpurls
Примеры:
Представления функций
    1. Добавьте импорт: из представлений импорта my_app
    2. Добавьте URL-адрес в urlpatterns: path ('', views.home, name = 'home')
Представления на основе классов
    1. Добавьте импорт: from other_app.views import Home
    2. Добавьте URL-адрес в urlpatterns: path ('', Home.as_view (), name = 'home')
Включение другого URLconf
    1. Импортируйте функцию include (): из импорта django.urls include, path
    2. Добавьте URL-адрес в urlpatterns: path ('blog', include ('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls', namespace='urls_blog')),
    path('admin/', admin.site.urls),
]
