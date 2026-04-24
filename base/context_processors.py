from .models import Category, Product
from .models import Notification


def category_renderer(request):
    return {
        'categories': Category.objects.all(),
    }


def notification_renderer(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            user=request.user).order_by('-created_at')[:5]
        return {'notifications': notifications}
    return {}
