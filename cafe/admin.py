from django.contrib import admin

# Register your models here.
from . models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'age', 'rating']


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['food', 'name', 'phone','city', 'address','house', 'pay_method']


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'massage']


admin.site.register(Team, TeamAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Order, OrderAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Rating)
