from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL of the app to the home view
     path('contact/', views.contact, name='contact'),
     path('form/', views.form, name='form'),
]
