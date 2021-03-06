from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('edit/<int:pk>', views.edittask, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]