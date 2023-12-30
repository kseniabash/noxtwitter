from django.contrib.auth.models import User
from django.urls import reverse_lazy

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status

from noxtwitter import models
from noxtwitter import serializers
from noxtwitter.views import PostViewSet


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = models.Post.objects.create(content="Test post", creator=self.user)
        self.view = PostViewSet.as_view({'get': 'list', 'post': 'create'})
        self.url = reverse_lazy('post-list')

    def test_post_list(self):
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request)
        serializer = serializers.PostSerializer(models.Post.objects.all(), many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_authenticated(self):
        data = {'content': 'New test post'}
        request = self.factory.post(self.url, data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_unauthenticated(self):
        data = {'content': 'New test post'}
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
