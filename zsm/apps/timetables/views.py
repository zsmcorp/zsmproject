from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Timetable, Category
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .utils import *
from .models import *
from .forms import *

def index(request):
    class_list = Category.objects.all()
    return render(request, 'timetables/list.html', {'class_list': class_list})


# def detail(request, timetable_slug):
#     class_id = Category.objects.filter(slug=timetable_slug)
#     timetables_list = Timetable.objects.filter(class_init=class_id)[:10]
#     return render(request, 'timetables/detail.html', {'timetables_list':timetables_list})

def detail(request, tt_slug):
    try:
        class_id = Category.objects.get(slug=tt_slug)
    except:
        raise Http404("Class not found!")
    # class_id = get_object_or_404(Category, slug = timetable_slug)
    # class_id = Category.objects.get(slug=timetable_slug)
    timetables_list = Timetable.objects.filter(class_init_id=class_id.id)

    return render(request, 'timetables/detail.html', {'timetables_list': timetables_list, 'class_id': class_id})


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'timetables/register.html'
    succss_url = reverse_lazy('login')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


def login(request):
    return HttpResponse('Hello world')