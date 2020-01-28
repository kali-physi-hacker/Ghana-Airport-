from django import template 
from django.utils import timezone 

register = template.Library()


@register.filter
def index(indexable, index):
    return indexable[index]


@register.filter
def get_course_name(iteratable):
    return iteratable[1].name


@register.filter
def get_course_description(iteratable):
    return iteratable[1].description


@register.filter 
def get_course(iteratable):
    return iteratable[1]


@register.filter 
def get_percentage_done(iterable):
    course = iterable[1]
    percentage_done = (course.duration_used()/course.duration_in_days())*100
    return int(percentage_done)
