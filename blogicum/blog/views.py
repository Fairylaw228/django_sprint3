from django.shortcuts import render
from .models import Location, Post, Category
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Category, Post
from django.http import Http404

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]


def index(request):
    # Получаем публикации, которые опубликованы и не позже текущего времени
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),  # Публикации, опубликованные не позже текущего времени
        is_published=True,  # Публикации, которые опубликованы
        category__is_published=True  # Публикации в опубликованных категориях
    ).order_by('-pub_date')[:5]  # Получаем 5 последних публикаций
    
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if post.pub_date > timezone.now() or not post.is_published or not post.category.is_published:
        raise Http404("Публикация недоступна.")
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404("Категория не опубликована.")
    
    # Убедитесь, что у вас есть локации в базе данных
    location, created = Location.objects.get_or_create(name='Остров отчаянья', is_published=True)

    # Теперь создаем посты или привязываем их к локации
    posts = Post.objects.filter(category=category, pub_date__lte=timezone.now(), is_published=True)
    for post in posts:
        post.location = location  # Привязываем локацию к каждому посту
        post.save()

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})