from django.contrib.auth.management.commands import createsuperuser

from django.contrib.auth.models import User


class Command(createsuperuser.Command):
    def handle(self, *args, **options):
        password = '1'
        username = 'greg.moon'
        options['username'] = username

        super(Command, self).handle(*args, **options)

        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()