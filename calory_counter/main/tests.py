from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from django.contrib.auth.models import User
from .models import Profile
import base64

def create_user(username, password):
    return User.objects.create_user(username=username, password=password)

class ViewTests(TestCase):
    def test_reg(self):

        photo = SimpleUploadedFile("p.jpg",  base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAUA" + "AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO" + "9TXL0Y4OHwAAAABJRU5ErkJggg=="), content_type="image/jpeg")

        response = self.client.post(reverse("registration"), {"username": "test123", "password1": "Hello4327", "password2": "Hello4327", "name": "polina", "age": 19, "height": 180, "weight": 65, "photo": photo})
        self.assertEqual(response.status_code, 302)

    def test_index(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Зарегистрироваться")

        create_user(username="test", password= "Hello4327")
        response = self.client.post(reverse("authentication"), {"username": "test", "password": "Hello4327"})

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Профиль")

    def test_profile(self):

        user = create_user(username="test", password= "Hello4327")
        photo = SimpleUploadedFile("p.jpg",  base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAUA" + "AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO" + "9TXL0Y4OHwAAAABJRU5ErkJggg=="), content_type="image/jpeg")
        Profile.objects.create(user_id = user, name = 'polina', age = 19, height = 180, weight = 65, photo = photo)

        response = self.client.post(reverse("authentication"), {"username": "test", "password": "Hello4327"})

        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "polina")
