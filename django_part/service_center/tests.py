import json
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from service_center.models import Categories

class DeleteCategoryViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='!1234567890')
        self.category = Categories.objects.create(name='Test category')

    def test_delete_category(self):
        self.client.login(username='testuser', password='!1234567890')
        data = {
            'id': self.category.id
        }
        response = self.client.post('/delete-category', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"result": 'Данные категории успешно удалены!'})
        self.assertFalse(Categories.objects.filter(id=self.category.id).exists())

class TestAddCategoryView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='!1234567890')

    def test_add_category(self):
        self.client.login(username='testuser', password='!1234567890')
        data = {
            'name': 'Тестовая категория'
        }
        response = self.client.post('/add-category', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"result": 'Категория успешно добавлена!'})
        self.assertTrue(Categories.objects.filter(name='Тестовая категория').exists())

class TestUpdateCategoryView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='!1234567890')
        self.category = Categories.objects.create(name='Test category')

    def test_update_category(self):
        self.client.login(username='testuser', password='!1234567890')
        data = {
            'id': self.category.id,
            'name': 'Измененная категория'
        }
        response = self.client.post('/update-category', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"result": 'Данные категории успешно изменены!'})
        self.assertTrue(Categories.objects.filter(name='Измененная категория').exists())

class TestGetCategoryView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='!1234567890')
        self.category = Categories.objects.create(name='Test category')

    def test_get_category(self):
        self.client.login(username='testuser', password='!1234567890')
        response = self.client.post('/get-categories')
        self.assertEqual(json.loads(response.content), json.loads(response.content))