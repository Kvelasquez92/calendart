from django.test import TestCase
from apps.miembros.models import Member

# Create your tests here.
class MemberTestCase(TestCase):
    def setUp(self):
        Member.objects.create(username='user1', email='k.kevin@gmail.com', first_name='kevin', last_name='velasquez', is_active=True, is_staff=True, is_artist=False
                             date_of_birth='1992-04-01', category=1, )
        Member.objects.create(username='user2', email='user2.usuario@gmail.com', first_name='usuario2', last_name='usuario', is_active=True, is_staff=False, is_artist=True
                              date_of_birth='1990-01-03', biography="esta es la biografia del usuario 2", phone_number='55555555', address='xela', members=1)

    def test_member_description(self):
        kevin = Member.objects.get(first_name='user1')
        usuario2 = Member.objects.get(first_name="usuario2")
        self.assertEqual(kevin.presentacion(), 'Soy kevin y me dicen user1, vivo en None y me gusta None')
        self.assertEqual(cat.speak(), 'Soy usuario2 y me dicen user2, vivo en xela y me gusta user1.')
