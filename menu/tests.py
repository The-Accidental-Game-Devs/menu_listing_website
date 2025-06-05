
from django.test import TestCase
from .models import Currency, Category, Item
from django.contrib.auth.models import User


class CurrencyModelTest(TestCase):
    def setUp(self):
        Currency.objects.create(name="Dollar", symbol="$")
        Currency.objects.create(name="Euro", symbol="€")

    def test_currency_creation(self):
        dollar = Currency.objects.get(name="Dollar")
        euro = Currency.objects.get(name="Euro")
        self.assertEqual(dollar.symbol, "$")
        self.assertEqual(euro.symbol, "€")

    def test_str_representation(self):
        dollar = Currency.objects.get(name="Dollar")
        self.assertEqual(str(dollar), "Dollar")

    def test_ordering_by_name(self):
        currencies = Currency.objects.all()
        self.assertEqual(list(currencies.values_list('name', flat=True)), ["Dollar", "Euro"])

    def test_meta_verbose_name_plural(self):
        self.assertEqual(Currency._meta.verbose_name_plural, "Currencies")

    def test_meta_permissions(self):
        perms = Currency._meta.permissions
        self.assertIn(('can_create_currency', 'Can create currency'), perms)
        self.assertIn(('can_edit_currency', 'Can edit currency'), perms)
        self.assertIn(('can_delete_currency', 'Can delete currency'), perms)

class CategoryModelTest(TestCase):
    def setUp(self):
        self.parent = Category.objects.create(name="Food")
        self.child = Category.objects.create(name="Desserts", parent=self.parent)

    def test_category_creation(self):
        self.assertEqual(self.parent.name, "Food")
        self.assertEqual(self.child.parent, self.parent)

    def test_str_representation(self):
        self.assertEqual(str(self.child), "Desserts")

    def test_ordering_by_name(self):
        categories = Category.objects.all()
        self.assertEqual(list(categories.values_list('name', flat=True)), ["Desserts", "Food"])

    def test_meta_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, "Categories")

    def test_meta_permissions(self):
        perms = Category._meta.permissions
        self.assertIn(('can_create_category', 'Can create category'), perms)
        self.assertIn(('can_edit_category', 'Can edit category'), perms)
        self.assertIn(('can_delete_category', 'Can delete category'), perms)

class ItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.currency = Currency.objects.create(name="Dollar", symbol="$")
        self.category = Category.objects.create(name="Main Course")
        self.item1 = Item.objects.create(
            name="Burger",
            category=self.category,
            price=10.00,
            currency=self.currency,
            created_by=self.user
        )
        self.item2 = Item.objects.create(
            name="Pizza",
            category=self.category,
            price=12.00,
            currency=self.currency,
            created_by=self.user
        )

    def test_item_creation(self):
        self.assertEqual(self.item1.name, "Burger")
        self.assertEqual(self.item1.category, self.category)
        self.assertEqual(self.item1.currency, self.currency)
        self.assertEqual(self.item1.created_by, self.user)

    def test_str_representation(self):
        expected = f"{self.item1.name} - {self.user} - {self.item1.created_at}"
        self.assertEqual(str(self.item1), expected)

    def test_ordering_by_created_at(self):
        items = Item.objects.all()
        self.assertEqual(items[0], self.item2)  # item2 created after item1

    def test_meta_permissions(self):
        perms = Item._meta.permissions
        self.assertIn(('can_create_item', 'Can create item'), perms)
        self.assertIn(('can_edit_item', 'Can edit item'), perms)
        self.assertIn(('can_delete_item', 'Can delete item'), perms)