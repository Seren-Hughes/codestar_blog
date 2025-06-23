from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Name',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    
    def test_form_is_invalid(self):
        """ Test for missing fields"""
        form = CollaborateForm({
            'name': '',
            'email': '',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Fields are missing but form is valid")


    def test_name_is_required(self):
        """ Test for name field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'testing'
        })
        self.assertFalse(form.is_valid(), msg="Name is missing but form is valid")

    def test_email_is_required(self):
       """ Test for email field"""
       form = CollaborateForm({
           'name': 'Name',
           'email': '',
           'message': 'testing'
       })
       self.assertFalse(form.is_valid(), msg="Email is missing but form is valid")

    def test_message_is_required(self):
       """ Test for message field"""
       form = CollaborateForm({
           'name': 'Name',
           'email': 'test@test.com',
           'message': ''
       })
       self.assertFalse(form.is_valid(), msg="Message is missing but form is valid")
