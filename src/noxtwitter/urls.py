from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from rest_framework import routers

from noxtwitter import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login_form.html'), name='login'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
	path('posts/', views.PostListView.as_view(), name='post_list'),
	path('posts/like', views.ToggleLikeView.as_view(), name='toggle_like'),
    path('api/', include(router.urls)),
]

if settings.DEV_MODE:
    urlpatterns = [path('dev/', include(urlpatterns))]
