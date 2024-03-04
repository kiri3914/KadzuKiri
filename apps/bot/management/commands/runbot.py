from django.core.management.base import BaseCommand
from apps.bot.bot import main

class Command(BaseCommand):
    help = 'Run bot'

    def handle(self, *args, **options):
        main()