from django.contrib.auth.management.commands.createsuperuser import Command as BaseCreateSuperuserCommand
from django.core.management import CommandError

class Command(BaseCreateSuperuserCommand):
    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        database = options.get('database')
        email = options.get('email')
        password = None  # You can set the password here if you want, but it's safer to set it interactively

        if not email:
            raise CommandError("You must provide an email address")

        user_data = {
            'email': email,
            'password': password
        }

        self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)
        if options.get('verbosity', 0) >= 1:
            self.stdout.write("Superuser created successfully.")
