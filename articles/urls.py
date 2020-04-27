from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articles_form, name='article_insert'),
    path('<int:id>/', views.articles_form, name='article_update'),
    path('delete/<int:id>/', views.articles_delete, name='article_delete'),
    path('list/', views.articles_list, name='article_list'),
]
