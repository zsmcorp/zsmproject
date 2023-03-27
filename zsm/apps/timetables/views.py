from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import Timetable, Category
from django.views.generic.list import ListView

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

class Search(ListView):
    
    paginate_by = 1

    def get_queryset(self):
        return  Timetable.objects.filter(class_init__icontains=self.request.GET.get('q')) 
    
    def get_context_data(self, *args, **kwargs): 
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context
 