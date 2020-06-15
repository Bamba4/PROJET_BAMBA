from django.urls import path
from . import views
urlpatterns = [
    path('contact/', views.nouveau_contact, name='contact'),
    path('article', views.addArticle, name='add_article'),
    path('voir_article', views.voir_contact, name="voir_contact")
]
