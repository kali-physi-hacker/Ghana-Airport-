from django import template 
register = template.Library()


@register.filter
def define(val=None):
    return val 