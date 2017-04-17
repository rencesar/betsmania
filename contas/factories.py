import factory
from django.contrib.auth.models import User

class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user%d' % n)
    password = ('pbkdf2_sha256$36000$coyali1VbyDf$NxTF20AH2KRIcz8DXCpwF2WRM/69FhQrPJZEc7hGSos=') # senha123
    first_name = 'Bruno'
    last_name = 'Mandela'

    class Meta:
        model = User
