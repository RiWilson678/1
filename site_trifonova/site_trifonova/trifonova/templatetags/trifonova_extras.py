from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Умножает значение на аргумент"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''

@register.filter
def total_price(order):
    """Вычисляет общую стоимость заказа"""
    try:
        return order.quantity * order.Service.price
    except (TypeError, AttributeError):
        return 0