from django.urls import path
from . import views

urlpatterns = [
    path('', views.Getname, name='get_name'),
    path('authors/'  , views.get_users, name='get_users'),
    path('author/<int:author_id>/', views.getauthor, name='get_author'),
]
