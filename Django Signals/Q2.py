"""
Question 2: Do Django signals run in the same thread as the caller?

Yes, by default, Django signals run in the same thread as the caller. 

"""

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.get_ident()}")

print(f"Caller thread: {threading.get_ident()}")
user = User.objects.create_user(username='testuser', password='testpass')
