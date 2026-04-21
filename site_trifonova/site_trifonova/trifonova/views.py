from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User, Service, Performer, Order
from .forms import UserForm, ServiceForm, PerformerForm, OrderForm

def index(request):
    return render(request, 'trifonova/index.html')

# User Views
class UserListView(ListView):
    model = User
    template_name = 'trifonova/user_list.html'
    context_object_name = 'users'
    ordering = ['FIO']

class UserDetailView(DetailView):
    model = User
    template_name = 'trifonova/user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'trifonova/user_form.html'
    success_url = reverse_lazy('trifonova:user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'trifonova/user_form.html'
    success_url = reverse_lazy('trifonova:user_list')

# Service Views
class ServiceListView(ListView):
    model = Service
    template_name = 'trifonova/service_list.html'
    context_object_name = 'services'
    ordering = ['name']

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'trifonova/service_detail.html'
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'trifonova/service_form.html'
    success_url = reverse_lazy('trifonova:service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'trifonova/service_form.html'
    success_url = reverse_lazy('trifonova:service_list')

# Performer Views
class PerformerListView(ListView):
    model = Performer
    template_name = 'trifonova/performer_list.html'
    context_object_name = 'performers'
    ordering = ['FIO']

class PerformerDetailView(DetailView):
    model = Performer
    template_name = 'trifonova/performer_detail.html'
    context_object_name = 'performer'

class PerformerCreateView(CreateView):
    model = Performer
    form_class = PerformerForm
    template_name = 'trifonova/performer_form.html'
    success_url = reverse_lazy('trifonova:performer_list')

class PerformerUpdateView(UpdateView):
    model = Performer
    form_class = PerformerForm
    template_name = 'trifonova/performer_form.html'
    success_url = reverse_lazy('trifonova:performer_list')

# Order Views
class OrderListView(ListView):
    model = Order
    template_name = 'trifonova/order_list.html'
    context_object_name = 'orders'
    ordering = ['-id']

class OrderDetailView(DetailView):
    model = Order
    template_name = 'trifonova/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'trifonova/order_form.html'
    success_url = reverse_lazy('trifonova:order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'trifonova/order_form.html'
    success_url = reverse_lazy('trifonova:order_list')