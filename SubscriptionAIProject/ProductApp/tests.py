from django.urls import reverse
from django.test import TestCase, Client

from ProductApp.models import ProductModel


class ProductViewTests(TestCase):
    def setUp(self):
        self.product = ProductModel.objects.create(
            title="Title Product",
            subtitle="SubTitle Product",
            price=123.33
        )

    def test_get_products_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_get_products_view_template(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/items.html')

    def test_get_products_view_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_product_view(self):
        response = self.client.get(reverse('product', kwargs={"product_id": self.product.id}))
        self.assertEqual(response.status_code, 200)

    def test_get_product_view_url_exists(self):
        response = self.client.get(f'/product/{self.product.id}')
        self.assertEqual(response.status_code, 200)

    def test_get_product_view_template(self):
        response = self.client.get(reverse('product', kwargs={"product_id": self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/item.html')

    def test_get_product_view_not_found_template(self):
        response = self.client.get(reverse('product', kwargs={"product_id": 120}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'not-found.html')


class ProductModelTests(TestCase):
    def test_title_replace_br(self):
        product = ProductModel.objects.create(
            title="Title<br/>Product",
            subtitle="SubTitle Product",
            price=123.33
        )
        replaced_title = product.title_replace_br()
        self.assertEqual(replaced_title, "Title Product")

    def test_product_model_fields(self):
        model_fields = ProductModel._meta.get_fields()
        fields = [field.name for field in model_fields]
        expected_fields = [
            'ordermodel', 'id', 'uuid', 'badge', 'card_featured', 'title',
            'term', 'subtitle', 'price', 'features_html', 'description_html',
            'image', 'url', 'active'
        ]
        self.assertEqual(fields, expected_fields)

    def test_badges_choices(self):
        BADGE_CHOICES = (
            (1, "Пусто"),
            (2, "Лучший выбор"),
            (3, "Безлимит"),
            (4, "Новинка"),
            (5, "Хит"),
        )
        self.assertEqual(ProductModel.BADGE_CHOICES, BADGE_CHOICES)

    def test_terms_choices(self):
        TERM_CHOICES = (
            (1, "1 МЕСЯЦ"),
            (2, "2 МЕСЯЦА"),
            (3, "3 МЕСЯЦА"),
            (4, "4 МЕСЯЦА"),
            (5, "5 МЕСЯЦЕВ"),
            (6, "6 МЕСЯЦЕВ"),
            (7, "1 ГОД"),
            (8, "2 ГОДА"),
            (9, "3 ГОДА"),
        )
        self.assertEqual(ProductModel.TERM_CHOICES, TERM_CHOICES)
