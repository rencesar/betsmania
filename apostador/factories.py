import factory
from django.contrib.auth.models import User

class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user%d' % n)
    password = ('123456')
    first_name = 'Bruno'
    last_name = 'Mandela'

    class Meta:
        model = User
