from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
        
    def test_successful_collaboration_request(self):
        """Tests for posting a collaboration request"""
        post_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'I would like to collaborate on a project.'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request submitted successfully',
            response.content
        )