from django.test import TestCase

class HelloWorldTestCase(TestCase):
    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")

# Create your tests here.
