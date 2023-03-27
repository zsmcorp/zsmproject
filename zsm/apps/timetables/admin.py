from django.contrib import admin
from .models import Category, Timetable


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


class TimetableAdmin(admin.ModelAdmin):
    list_display = ['class_init', 'first_lesson', 'second_lesson', 'third_lesson', 'fourth_lesson', 'fifth_lesson',
                    'sixth_lesson', 'seventh_lesson', 'timetable_date', 'short_lesson', 'short_break']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Timetable, TimetableAdmin)
