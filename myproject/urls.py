from django.contrib import admin
from django.urls import path, include  # Import include to include app-specific URLs
from myapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the URLs from `myapp`
    path('products/', views.products, name='products'),
]
