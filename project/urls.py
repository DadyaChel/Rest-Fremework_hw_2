import django.contrib
from django.urls import path, include
from posts import views
from rest_framework import routers


urlpatterns = [
    path('admin/', django.contrib.admin.site.urls),
    path('api/pos/', views.create_positions),
    path('api/emp/', views.create_employee)
]
