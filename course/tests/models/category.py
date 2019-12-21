from django.test import TestCase

from course.models.category import Category


class CategoryTest(TestCase):
    def setUp(self):
        name = "Category Test Name"
        description = "Category Test Description"

        Category.objects.create(
            name=name,
            description=description
        )

    def test_content_in_data(self):
        category = Category.objects.get(name=self.name)
        self.assertEquals(category.name, self.name)
        self.assertEquals(category.description, self.description)