from .models import Category, Product


def category_renderer(request):
    return {
        'categories': Category.objects.all(),
    }
