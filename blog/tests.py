from django.test import TestCase
from django.utils import timezone
from .models import Author, Post
from django.contrib.auth.models import User

class PostModelTests(TestCase):

    def test_post_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        author = Author.objects.create(user=user)  # Create an author

        post = Post.objects.create(
            author=author,
            title="Test Post",
            content="This is a test post.",
            published_date=timezone.now()
        )
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "This is a test post.")
        self.assertIsNotNone(post.published_date)

    def test_post_string_representation(self):
        user = User.objects.create_user(username='testuser2', password='testpassword')
        author = Author.objects.create(user=user)
        post = Post.objects.create(
            author=author,
            title="Another Test Post",
            content="Another test post content."
        )
        self.assertEqual(str(post), "Another Test Post")  # Check __str__ method
