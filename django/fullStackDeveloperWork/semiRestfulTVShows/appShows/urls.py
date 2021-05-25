from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('showsNew', views.showsNewPage),
    path('createShow', views.recordShow),
    path('updateShow/<int:showId>', views.updateShow),
    path('shows/<int:showId>', views.displayShow),
    path('edit/<int:showId>', views.editShow),
    path('delete/<int:showId>', views.deleteShow),
    
    path('clean', views.cleanAllData),
]