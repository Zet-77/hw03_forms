from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )
    def test_models_have_correct_object_names(self):
        '''Проверка длины __str__ post'''
        error_name = f"Вывод не имеет {15} символов"
        self.assertEqual(self.post.__str__(),
                         self.post.text[:15],
                         error_name)


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()                  
        
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )              
    def test_models_have_correct_object_names(self):
        '''Проверка длины __str__ post'''
        error_name = f"Вывод не соответствует 'Текстовая группа' ."
        self.assertEqual(self.group.__str__(),
                        self.group.title,
                        error_name)
