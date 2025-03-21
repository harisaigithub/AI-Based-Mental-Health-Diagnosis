# adminapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def split_lines(text):
    """Splits text into a list of lines based on newline characters."""
    if text:
        return text.splitlines()
    return []
