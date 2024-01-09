from django.core.management.base import BaseCommand, CommandError
from main.models import Profile
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Деактивирует профиль пользователя'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for user_id in options['user_id']:
            try:
                user = User.objects.get(pk=user_id)
                print(user)
                profile = Profile.objects.get(user_id=user)
            except Exception as e:
                print(e)
                raise CommandError('При выполнении возникла ошибка, user_id="%s"' % user_id)

            profile.is_active = False
            profile.save()

            self.stdout.write(self.style.SUCCESS('Профиль с user_id="%s" деактивирован' % user_id))