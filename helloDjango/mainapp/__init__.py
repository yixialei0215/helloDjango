from django.template.defaultfilters import register
import os


@register.filter('ellisp')
def ellisp(value):
    return os.path.splitext(value)[-1]
