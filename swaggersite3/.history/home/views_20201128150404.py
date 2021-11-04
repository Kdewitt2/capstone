from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, HomePost, Order
from .forms import OrderModelForm

def home(request):
    context = {
        'title': "Home",
        'posts': HomePost.objects.all()
    }
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html', {'title': "About"})

def contact(request):
    return render(request, 'home/contact.html', {'title': "Contact"})

def shop(request):
    context = {
        'title': "Shop",
        'products': Product.objects.all()
    }
    return render(request, 'home/shop.html', context)

def redir(request):
    return redirect('shop')

class ProductDetailView(DetailView):
    model = Product    

def blog(request):
    return render(request, 'home/blog.html', {'title': "Blog"})

class OrderCreateView(LoginRequiredMixin, CreateView, request):
    model = Order
    form = OrderModelForm
    template_name = 'home/order_form.html'
    context_object_name = 'orders'
    user = request.user


#    success_url = 'shop'
    fields = ['GrapefruitSoap', 
            'LemongrassSugarScrub', 
            'CharcoalClayFacialScrub', 
            'LavenderSoap',
            'AloeVeraGoatMilkSoap', 
            'PeppermintSoap', 
            'EucalyptusSoap', 
            'RawSoap', 
            'CalendulaBurdockSalve', 
            'SootheMeSalve', 
            'LavenderLoofahSoap', 
            'LemonPoppySeedSoap']


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return User.objects.filter(user=self.request.user)