"""
Question 3: By default, do Django signals run in the same database transaction as the caller?

By default, Django signals do not run in the same database transaction as the caller. 
This means the signal is triggered after the transaction is committed, 
and changes made inside the signal handler are not rolled back if the transaction fails.

"""

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler triggered")

try:
    with transaction.atomic():
        user = User.objects.create_user(username='testuser', password='testpass')
        print("User created, but transaction will be rolled back")
        raise Exception("Rolling back transaction")
except Exception:
    print("Transaction rolled back")

