from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'testdevtt/home.html')
    def test_user_view(self):
        from .models import users
        user = users.objects.create(name='John Doe', age=30)
        response = self.client.get(reverse('view_records'))
        self.assertContains(response, user.name)        
        self.assertContains(response, user.age)
    def view_records_template(self):
        response = self.client.get(reverse('view_records'))
        self.assertTemplateUsed(response, 'testdevtt/view_records.html')