from django import template 

register = template.Library() 

@register.filter
def addclass(field, class_name):
    return field.as_widget(attrs={'class': class_name}) 