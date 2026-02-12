"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as blog_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="Home"),
    path('category/', include('blogs.urls')),
    path('blog/<slug:slug>/', blog_view.single_post_view, name='single_post_view'),
    path('blogs/search/',blog_view.search, name="search"),
    path('register/', views.register,name='register')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Used to tell django development server how to handle any incoming media files: where to store them and which url to use during serving the media uploaded.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
