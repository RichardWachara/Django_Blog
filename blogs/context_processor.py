
from blogs.models import About, Category, Social_Links


def get_categories(request):
    categories = Category.objects.all()
    abouts = About.objects.all()
    social_links = Social_Links.objects.all()
    return dict(categories=categories, abouts=abouts,social_links=social_links)