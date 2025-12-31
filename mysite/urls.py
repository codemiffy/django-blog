from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from blog import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', blog_views.custom_logout, name='logout'),
    path('', include('blog.urls')),
]
