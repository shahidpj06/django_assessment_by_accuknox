"""

Question 1: 

Django signals are executed synchronously by default. When a signal is sent, 
all the connected signal handlers are called immediately, 
and the execution doesn't proceed until those handlers are finished.

"""

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  
    print("Signal handler finished")

user = User.objects.create_user(username='testuser', password='testpass')

print("User created")
