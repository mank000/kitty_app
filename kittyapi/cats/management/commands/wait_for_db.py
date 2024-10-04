import time

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'подождать)'

    def handle(self, *args, **kwargs):
        time.sleep(0)
