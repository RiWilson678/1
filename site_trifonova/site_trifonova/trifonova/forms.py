from django import forms
from .models import User, Service, Performer, Order

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['FIO', 'namber']
        widgets = {
            'FIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО'}),
            'namber': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер'}),
        }
        labels = {
            'FIO': 'ФИО',
            'namber': 'Номер телефона',
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'attribute_2', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название услуги'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'attribute_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Длительность/Сложность', 'step': '0.01'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'attribute_2': 'Длительность (часы)',
            'price': 'Цена (руб)',
        }

class PerformerForm(forms.ModelForm):
    class Meta:
        model = Performer
        fields = ['FIO', 'description', 'name']
        widgets = {
            'FIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО преподавателя'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'name': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'FIO': 'ФИО',
            'description': 'Описание',
            'name': 'Направление',
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'Performer', 'Service', 'User']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество занятий'}),
            'Performer': forms.Select(attrs={'class': 'form-control'}),
            'Service': forms.Select(attrs={'class': 'form-control'}),
            'User': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'quantity': 'Количество',
            'Performer': 'Преподаватель',
            'Service': 'Услуга',
            'User': 'Ученик',
        }