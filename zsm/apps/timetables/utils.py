from .models import *
menu = [{'title': 'Authorization', 'url_name': 'home-index'},
        {'title': 'Class seletor', 'url_name': 'index'},
        {'title': 'Contact', 'url_name': 'index'},
        {'title': 'About', 'url_name': 'index'},
        {'title': 'Authorization', 'url_name': 'login'},
        {'title': 'Registration', 'url_name': 'login'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        classes = Category.objects.all()
        context['menu'] = menu
        context['classes'] = classes
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context