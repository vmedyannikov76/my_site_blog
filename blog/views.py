from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):  # Обработчик для отделной статьи принимает на вход 4 аргумента
    # слаг и дату публикации
    post = get_object_or_404(Post,
                             slug=post,
                             status='status_published',
                             publich__year=year,
                             publish__month=month,
                             publish__day=day,
                             )
    return render(request, 'blog/post/detail.html', {'post': post})
