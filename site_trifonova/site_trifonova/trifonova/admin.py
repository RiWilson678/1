from django.contrib import admin
from .models import User, Service, Performer, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['FIO', 'namber']
    search_fields = ['FIO']
    list_filter = ['namber']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'attribute_2', 'price']
    search_fields = ['name']
    list_filter = ['price']

@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    list_display = ['FIO', 'description', 'name']
    search_fields = ['FIO']
    list_filter = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'User', 'Service', 'Performer', 'quantity']
    search_fields = ['User__FIO', 'Service__name']
    list_filter = ['Service', 'Performer']