from django.urls import path
from . import views

app_name = 'trifonova'

urlpatterns = [
    path('', views.index, name='index'),
    
    # URL для User
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/create/', views.UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    
    # URL для Service
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('service/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('service/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service_update'),
    
    # URL для Performer
    path('performers/', views.PerformerListView.as_view(), name='performer_list'),
    path('performer/<int:pk>/', views.PerformerDetailView.as_view(), name='performer_detail'),
    path('performer/create/', views.PerformerCreateView.as_view(), name='performer_create'),
    path('performer/<int:pk>/update/', views.PerformerUpdateView.as_view(), name='performer_update'),
    
    # URL для Order
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
]