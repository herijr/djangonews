from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('add-post/', views.add_post, name='add_post'),
    path('<slug:post_slug>/', views.post, name='post'),
]
