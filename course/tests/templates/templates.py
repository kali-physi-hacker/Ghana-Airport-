import os

from django.test import SimpleTestCase
from django.conf import settings

BASE_DIR = os.path.join()


class TestCourseList(SimpleTestCase):
    @staticmethod
    def open_html_file():
        with open(settings.BASE_DIR0)