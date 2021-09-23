from celery import shared_task
from .models import TelegramUser


@shared_task
def notify_user(user_id: int, message: str, *args, **kwargs):
    user = TelegramUser.objects.get(pk=user_id)
    user.notify(message, *args, **kwargs)
