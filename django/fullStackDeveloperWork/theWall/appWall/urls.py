from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addPost', views.methodAddingPost),
    path('delPost/<int:postId>', views.deletingPost),
    
    path('cleanSession', views.cleanTheSession),

]