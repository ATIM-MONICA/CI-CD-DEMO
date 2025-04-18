from django.test import TestCase, client
from django.urls import reverse

# Create your tests here.pip
class GreetingTests(TestCase):
    def setUp(self):
        self.client = client()
        
    def text_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello')
        self.assertTemplateUsed(response, 'index.html')
        
class GreetingFunctionalityTests(TestCase):
    def test_greeting(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['greeting'], 'Hello')
        
