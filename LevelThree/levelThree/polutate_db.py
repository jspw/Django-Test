import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","levelThree.settings")

import django
django.setup()

from appThree.models import Users
from faker import Faker

fakgen = Faker()

def populate(n):
    for _ in range(n):
        fake_name=fakgen.name()
        fake_email=fakgen.email()
        fake_location=fakgen.address()


        user = Users.objects.get_or_create(name=fake_name,email=fake_email,country=fake_location)


if __name__ == '__main__':
    populate(20)