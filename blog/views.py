from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from django.views.generic import ListView

class PostListView(ListView):
    """Класс обработчик списков, позволяет отображать несколько объектов любого типа"""
    queryset = Post.published.all()  # Указываем обработчик, по умолчанию Post.objects.all(), можно так же указать
    #  model=Post, тогда обработчик будет подтянут из модели в которой мы его определили
    context_object_name = 'posts'  # Используем в качестве переменной контекста
    paginate_by = 3
    template_name = "blog/post/list.html"


#  Функция обработчик вызова
# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)  # По 3 статьи на странице
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:  #  Если страница не является целым числом, возвращаем первую страницу.
#         posts = paginator.page(1)
#     except EmptyPage:  # Если номер страницы больше чем общее кол-во страниц, возвращаем последнюю страницу
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):  # Обработчик для отделной статьи принимает на вход 4 аргумента
    # слаг и дату публикации
    post = get_object_or_404(Post,
                             slug=post,
                             status='status_published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             )
    return render(request, 'blog/post/detail.html', {'post': post})
