from django.test import TestCase
from django.urls import reverse
from .models import Category

class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_str_representation(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_get_url(self):
        url = self.category.get_url()
        expected_url = reverse("product_slug", args=[self.category.slug])
        self.assertEqual(url, expected_url)

    def test_get_absolute_url(self):
        url = self.category.get_absolute_url()
        expected_url = reverse("category_detail", args=[self.category.slug])
        self.assertEqual(url, expected_url)

    def test_get_image_url_with_image(self):
        self.category.image = 'path/to/image.jpg'
        self.category.save()
        url = self.category.get_image_url()
        self.assertEqual(url, self.category.image.url)

    def test_get_image_url_without_image(self):
        url = self.category.get_image_url()
        self.assertEqual(url, '/path/to/default/image.jpg')

    def test_get_total_products(self):
        # Create some mock products
        for i in range(3):
            self.category.product_set.create(name=f'Test Product {i}')

        total_products = self.category.get_total_products()
        self.assertEqual(total_products, 3)