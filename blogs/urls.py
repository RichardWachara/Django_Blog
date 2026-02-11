from django.urls import path, include
from . import views


urlpatterns = [
    # accepting the category id here to be passed and used by the views
    # function. The name receiving the value should be the same name as one passed
    # into the views function
    
    path('<int:category_id>/',views.posts_by_category, name="posts_by_category"),
]