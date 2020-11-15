from django.test import Client, TestCase

from Budgeter.views import *

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    