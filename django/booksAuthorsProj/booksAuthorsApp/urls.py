from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('authors', views.authorsPage),

    path('addingBook', views.addingsomeBook),
    path('addingAuthor', views.addingNewAuthor),

    path('books/<bookNumber>', views.showBookData),
    path('authors/<authId>', views.showauthorData),
    
    path('clear', views.cleanAll),
]