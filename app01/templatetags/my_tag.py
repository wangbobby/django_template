from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def my_add100(v1):
    return v1+100

@register.simple_tag
def my_add(v1,v2,v3):
    return v1+v2+v3

@register.filter
def my_add200(v1, v2):
    return v1+v2

# def my_input(id, arg):
#     result = "<input type='text' id='%s' class='%s' />" % (id, arg,)
#     return mark_safe(result)