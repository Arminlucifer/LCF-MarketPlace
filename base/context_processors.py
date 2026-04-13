from .models import Category, Product


def category_renderer(request):
    return {
        'all_categories': Category.objects.all(),
    }
