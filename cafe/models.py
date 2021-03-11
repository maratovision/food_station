from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Team(models.Model):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, default='team_image.png')
    position = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    rating = models.IntegerField(blank=True, null=True)


class Food(models.Model):
    food_choices = [
        ('Восточная кухня', 'Восточная кухня'),
        ('Европейская кухня', "Европейская кухня"),
        ('Десерты', 'Десерты'),
        ('Напитки', 'Напитки'),
        ('Салаты', 'Салаты')
    ]
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField(max_length=10)
    category = models.CharField(max_length=30, choices=food_choices)
    image = models.ImageField(blank=True, null=True, default='food_default.png')

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=50)
    large_title = models.TextField(max_length=200)
    image = models.ImageField()
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=20)
    text = models.CharField(max_length=250)


class Order(models.Model):
    p_method = (
        ('VISA/Bank account', 'VISA/Bank account'),
        ('PayPal', 'PayPal'),
        ('Cash', 'Cash')
    )
    name = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(max_length=10)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    house = models.CharField(max_length=10)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pay_method = models.CharField(choices=p_method, max_length=30)


class Testimonials(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    massage = models.TextField()


class Rating(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rate = models.PositiveIntegerField(default=0)
