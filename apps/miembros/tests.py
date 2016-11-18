from django.test import TestCase
from apps.miembros.models import Member

# Create your tests here.

#Testing models

class MemberTestCase(TestCase):
    def setUp(self):
        Member.objects.create(username='user1', email='k.kevin@gmail.com', first_name='kevin', last_name='velasquez', is_active=True, is_staff=True,
                             date_of_birth='1992-04-01', address = 'la esperanza', category_id=1)
        Member.objects.create(username='user2', email='user2.usuario@gmail.com', first_name='usuario2', last_name='usuario', is_active=True, is_staff=False,
                              date_of_birth='1990-01-03', biography="esta es la biografia del usuario 2", phone_number='55555555', address='xela')

    def test_member_description(self):
        kevin = Member.objects.get(first_name='kevin')
        usuario2 = Member.objects.get(first_name="usuario2")
        self.assertEqual(kevin.presentacion(), 'Soy kevin y me dicen user1, vivo en la esperanza')
        #self.assertTrue(isinstance(kevin, Member))
        self.assertEqual(usuario2.presentacion(), 'Soy usuario2 y me dicen user2, vivo en xela')


#Testing Views

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SingUpTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(SingUpTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SingUpTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get("http://localhost:8000/members/new_member")
        #find the form element
        username = selenium.find_element_by_id('id_username')
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        birthdate = selenium.find_element_by_id('id_date_of_birth')
        email = selenium.find_element_by_id('id_email')
        address = selenium.find_element_by_id('id_address')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_name('save')

        #Fill the form with data
        username.send_keys('fulanito')
        first_name.send_keys('Fulano')
        last_name.send_keys('Something')
        birthdate.send_keys('1995-10-05')
        email.send_keys('chicle.kevin@gmail.com')
        address.send_keys('xela')
        password1.send_keys('Pass_123')
        password2.send_keys('Pass_123')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        self.assertIn('http://localhost:8000/members/new_member', selenium.current_url)
