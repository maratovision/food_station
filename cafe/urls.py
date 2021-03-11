from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('food/', food, name='food_page'),
    path('food_details/<int:food_id>/', food_details, name='food_details'),
    path('team/', team, name='team_page'),
    path('about/', about, name='about_page'),
    path('order/<int:food_id>', order, name='order'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('blog_details/<int:blog_id>/', blog_details, name='blog_details'),
    path('products/', listing, name='products'),
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('logout_page/', logout_page, name='logout_page'),
    path('testimonials/', testimonials, name='testimonials')
]
