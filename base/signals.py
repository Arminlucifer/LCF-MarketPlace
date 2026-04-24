from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

from .models import Notification, Comment, CommentLike


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):

    if created:
        product = instance.product
        if instance.owner != instance.product.seller:
            content_type = ContentType.objects.get_for_model(product)
            Notification.objects.create(
                user=instance.product.seller,
                text=f'{instance.owner.username} commented for "{instance.product.name}" {instance.body[:10]}...',
                content_type=content_type,
                object_id=instance.product.id

            )
