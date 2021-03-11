from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CommentForm, OrderForm, SignupForm, TestimonialsForm, RateForm
from .models import *


def index(request):
    product = Food.objects.all()[:3]
    blog = Blog.objects.all()[:3]
    context = {'product': product, 'blog': blog}
    return render(request, 'cafe/index.html', context)


def food(request):
    food = Food.objects.all()
    context = {'food': food}
    return render(request, 'cafe/food.html', context)


def food_details(request, food_id):
    food = Food.objects.get(id = food_id)
    rates = food.rating_set.all()
    total = 0
    for i in rates:
        total += i.rate
    form = RateForm(initial={'food': food, 'user': request.user})
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            if 0 <= form.cleaned_data['rate'] <= 10:
                form.save()
            else:
                return HttpResponse("Not good")
    context = {'food': food, 'rates': round(total/len(rates), 1), 'form': form}
    return render(request, 'cafe/product-details.html', context)



def about(request):
    return render(request, 'cafe/about.html')


def order(request, food_id):
    food = Food.objects.get(id = food_id)
    form = OrderForm(initial={'food': food, 'user': request.user})
    total_price = 0
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            total_price = food.price * form.cleaned_data['quantity']
            form.save()
            return redirect('/')
    return render(request, 'cafe/checkout.html', {'form': form, 'total_price': total_price})


def contact(request):
    testimonials = Testimonials.objects.all()
    form = TestimonialsForm(initial={'name': request.user})
    if request.method == 'POST':
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'cafe/contact.html', {'testimonials': testimonials, 'form': form})


def blog(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 3)  # Show 3 contacts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"blogs": blog, 'page_obj': page_obj}
    return render(request, 'cafe/blog.html', context)


def blog_details(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    comments = blog.comment_set.all()
    form = CommentForm(initial={'blog': blog})
    if request.method == 'POST':
        form = CommentForm(request.POST,initial={'blog':blog})
        if form.is_valid():
            form.blog = blog
            form.save()
    context = {'blog': blog, 'form': form, 'comments': comments}
    return render(request, 'cafe/blog-details.html', context)


def team(request):
    team = Team.objects.all()
    paginator = Paginator(team, 3)  # Show 3 contacts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"team": team, 'page_obj': page_obj}
    return render(request, 'cafe/team.html', context)


def products(request):
    food = Food.objects.all()
    context = {'food': food}
    return render(request, 'cafe/products.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        login(request, user)
        return redirect('index')
    return render(request, 'cafe/login.html')


def register(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'cafe/register.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('/')


def testimonials(request):
    testimonial = Testimonials.objects.all()
    context = {'testimonial': testimonial}
    return render(request, 'cafe/testimonials.html', context)


def listing(request):
    contact_list = Food.objects.all()
    paginator = Paginator(contact_list, 6)  # Show 6 contacts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cafe/products.html', {'page_obj': page_obj})